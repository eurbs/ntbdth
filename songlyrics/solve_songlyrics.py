import csv
import os

PATH = os.path.abspath('')
THECSV = 'scrambled_links.csv'

def generate_link(video_id, minute, second):
  prefix = "https://youtu.be/"
  
  if not int(minute):
    minute_string = ""
  else:
    minute_string = minute + "m"

  return prefix + video_id + "?t=" + minute_string + second + "s"

with open(os.path.join(PATH, THECSV), 'rt') as csvfile:
  reader = csv.reader(csvfile, delimiter=',')
  for row in reader:
    print generate_link(video_id=row[0], minute=row[1], second=row[2])
