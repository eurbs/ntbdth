import os, sys
from PIL import Image, ImageDraw

# brick element ids
b2x2 = 300326   # black 2x2
b2x4 = 300126   # black 2x4
w2x2 = 300301   # white 2x2
w2x4 = 300101   # white 2x4

def clue_to_image(clue, outfile):
  """
  :param list clue: The list of lists containing all variables.
  :param string outfile: Path to output file.
  """

  square_side = len(clue) * 40
  qr = Image.new("RGBA", (square_side, square_side), (255, 255, 255, 0))
  qrctx = ImageDraw.Draw(qr)

  y = 0
  x = 0
  x_off = 0   # to account for the 2x4's while indexed by length of list
  for y in range(len(clue)):
    for x in range(len(clue[y])):
      x1 = (x + x_off) * 40
      y1 = y * 40
      y2 = ((y + 1) * 40) - 1

      if clue[y][x] == b2x2:
        x2 = ((x + x_off + 1) * 40) - 1
        fill_color = "black"
      elif clue[y][x] == b2x4:
        x2 = ((x + x_off + 2) * 40) - 1
        x_off += 1
        fill_color = "black"
      elif clue[y][x] == w2x2:
        x2 = ((x + x_off + 1) * 40) - 1
        fill_color = "white"
      elif clue[y][x] == w2x4:
        x2 = ((x + x_off + 2) * 40) - 1
        x_off += 1
        fill_color = "white"

      # draw the rectangle!
      qrctx.rectangle([(x1, y1), (x2, y2)], fill=fill_color)
    x_off = 0

  qr.save(outfile, "PNG")

def clue_to_text(clue):
  """List as lego element IDs in a text file"""
  to_print = []
  for row in clue:
    for piece in row:
      to_print.append("(#" + str(piece) + ")")
    print " ".join(to_print)
    to_print = []

def clue_to_html(clue):
  """Output for ntbdth_web webapp answers CSV"""
  to_print = []
  for row in clue:
    for piece in row:
      # to_print.append("&#40;&#35;" + str(piece) + "&#41;")
      to_print.append("(#" + str(piece) + ")")
    to_print.append(" <br>")
  print " ".join(to_print)

def get_clue():
  """Hard coded in all its glory"""
  row1 = [b2x4, b2x2, b2x4, b2x4, w2x2, b2x2, w2x2, w2x4, b2x2, w2x2, b2x2, b2x4, b2x4, b2x4]
  row2 = [b2x2, w2x4, w2x2, w2x4, b2x2, w2x2, b2x2, w2x4, b2x4, w2x2, b2x2, w2x2, w2x4, w2x4, b2x2]
  row3 = [b2x2, w2x2, b2x2, b2x4, w2x2, b2x2, w2x4, w2x2, b2x2, w2x2, b2x2, w2x2, b2x2, w2x2, b2x4, b2x2, w2x2, b2x2]
  row4 = [b2x2, w2x2, b2x4, b2x2, w2x2, b2x2, w2x2, b2x4, w2x2, b2x4, w2x2, b2x2, w2x2, b2x4, b2x2, w2x2, b2x2]
  row5 = [b2x2, w2x2, b2x4, b2x2, w2x2, b2x2, w2x4, b2x4, b2x4, w2x2, b2x2, w2x2, b2x2, b2x4, w2x2, b2x2]
  row6 = [b2x2, w2x4, w2x4, w2x2, b2x2, w2x2, b2x2, w2x4, b2x2, w2x4, b2x2, w2x2, w2x4, w2x4, b2x2]
  row7 = [b2x4, b2x4, b2x2, b2x4, w2x2, b2x2, w2x2, b2x2, w2x2, b2x2, w2x2, b2x4, b2x2, b2x4, b2x4]
  row8 = [w2x4, w2x4, w2x4, w2x4, w2x2, b2x2, w2x2, b2x4, w2x4, w2x4, w2x4, w2x4]
  row9 = [b2x4, b2x2, b2x4, w2x2, b2x4, b2x4, b2x2, b2x4, w2x2, b2x4, w2x2, b2x2, w2x2, b2x2, w2x2]
  row10 = [w2x2, b2x4, b2x4, w2x2, b2x4, w2x2, b2x4, w2x4, b2x2, w2x4, b2x4, w2x2, b2x2, w2x2]
  row11 = [b2x2, w2x2, b2x2, w2x4, w2x2, b2x2, w2x2, b2x4, w2x2, b2x2, w2x4, b2x2, w2x4, w2x2, b2x4, b2x2]
  row12 = [w2x2, b2x2, w2x2, b2x4, w2x2, b2x2, w2x4, b2x2, w2x2, b2x4, w2x4, b2x2, w2x4, b2x2, w2x2, b2x2]
  row13 = [b2x4, b2x4, w2x2, w2x4, b2x4, b2x4, b2x2, w2x4, b2x2, w2x2, b2x4, b2x4, b2x2]
  row14 = [w2x2, b2x2, w2x2, b2x4, w2x2, b2x2, w2x4, b2x2, w2x2, b2x4, w2x4, w2x4, w2x4, w2x4]
  row15 = [w2x2, b2x4, b2x2, w2x4, w2x4, w2x2, b2x4, b2x2, w2x4, b2x4, b2x2, b2x4, b2x4]
  row16 = [b2x2, w2x2, b2x2, w2x4, b2x2, w2x2, b2x4, w2x2, b2x2, w2x2, b2x2, w2x2, b2x2, w2x2, w2x4, w2x4, b2x2]
  row17 = [w2x4, w2x4, b2x2, b2x4, w2x2, w2x4, w2x4, w2x4, b2x2, w2x2, b2x4, b2x2, w2x2, b2x2]
  row18 = [w2x2, b2x2, w2x2, b2x2, w2x4, w2x4, w2x4, w2x4, b2x2, w2x2, b2x2, w2x2, b2x4, b2x2, w2x2, b2x2]
  row19 = [b2x2, w2x2, w2x4, b2x4, b2x4, b2x2, w2x2, b2x4, w2x4, b2x2, w2x2, b2x2, b2x4, w2x2, b2x2]
  row20 = [w2x2, b2x2, w2x4, w2x2, b2x4, w2x4, w2x4, w2x2, b2x2, w2x2, b2x2, w2x4, w2x2, w2x4, b2x2]
  row21 = [w2x4, w2x4, w2x4, w2x4, b2x2, w2x2, b2x4, w2x4, b2x4, b2x4, b2x2, b2x4]

  final_list = [
    row1, row2, row3, row4, row5, row6, row7,
    row8, row9, row10, row11, row12, row13, row14,
    row15, row16, row17, row18, row19, row20, row21,
  ]
  return final_list

def main():


  outfile = os.path.join(".", "solution_example.png")

  clue_to_image(get_clue(), outfile)
  clue_to_text(get_clue())
  # clue_to_html(get_clue())

if __name__ == '__main__':
  main()