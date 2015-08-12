import os
import re
import sys

from contextlib import contextmanager

# according to stackoverflow, this is available on most unix systems
# any list of words will do though
WORDPATH = os.path.join("/", "usr", "share", "dict", "words")
EXPORTPATH = ""

def ascii_to_alphabet_pos(char):
  """ 
  Take a lowercase character and return the integer value
  of its position in the alphabet 
  """
  return ord(char) - 97

def alphabet_pos_to_ascii(pos):
  """ 
  Take a position in the alphabet and translate to an ascii character.
  """
  return chr(pos + 97)

def caesar_shift_word(word, shift_amount):
  """ Shift the word. Please use positive shifts. """
  oldcharlist = list(word.lower())
  newcharlist = []

  for char in oldcharlist:
    shifted_char_pos = (ascii_to_alphabet_pos(char) + shift_amount) % 26
    shifted_char = alphabet_pos_to_ascii(shifted_char_pos)
    newcharlist.append(shifted_char)

  return "".join(newcharlist)

def generate_shiftable_words(words):
  """
  generates a list of shiftable words in a commaseparated csv.
  
  :param words: set of words.
  :param file_name: file to write output to. defaults to stdout.
  :return [[word, shifted_word, shift_amount],...]: List of 3 element lists
  """
  shiftable_words = []
  for shift_amount in range(1,26):
    for word in words:
      shifted_word = caesar_shift_word(word, shift_amount)
      if shifted_word in words:
        shiftable_words.append([word, shifted_word, shift_amount])

  return shiftable_words

def print_shiftable_words(words):
  """ Prints list comma-separated shiftable words to stdout. """
  shiftable_words = generate_shiftable_words(words)
  for entry in shiftable_words:
    print "".join([entry[0],",",entry[1],",",str(entry[2])])

def export_shiftable_words(words, file_name=None):
  """
  Exports list of shiftable words in the form of a comma-separated csv.
  col1 is the word, col2 is the word it shifts to, col3 is the positive shift number.

  :param words: set of words.
  :param file_name: file to write output to. defaults to stdout.
  """
  shiftable_words = generate_shiftable_words(words)
  with open(file_name, 'w') as output:
    for entry in shiftable_words:
      output.write("".join([entry[0],",",entry[1],",",str(entry[2]),"\n"]))

def main():
  with open(WORDPATH) as wordfile:
    # extract the words from the file
    wordlist = wordfile.read()
    wordlist = re.split('\W', wordlist)
    wordlist = filter(None, wordlist)

    # set because we will be checking for memebership
    words = set(wordlist)

    print_shiftable_words(words)

if __name__ == "__main__": main()