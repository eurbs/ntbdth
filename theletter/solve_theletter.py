import re
import sys

# naively assumes a good filename is passed
filename = sys.stdin.readline().rstrip()

with open(filename, "r") as textfile:
  # read provided textfile
  unprocessed_text = textfile.read()

  # strip all non alphanumeric characters
  stripped_result = re.sub(r'[^a-zA-Z\s]', "", unprocessed_text)

  # split into list of words
  words = re.split('\W', stripped_result)
  words = filter(None, words)

  # populate dictionary counting number of occurrences of each word 
  word_count = {}
  for word in words:
    lower_word = word.lower()
    if lower_word in word_count:
      word_count[lower_word] += 1
    else:
      word_count[lower_word] = 1

  # iterate over ditionary to collect number of unique words
  num_unique = 0
  num_duplicates = 0
  for key, val in word_count.iteritems():
    if not (key == ''):
      if val == 1:
        num_unique += 1
      else:
        num_duplicates +=1

  # print the number of unique and duplicate words for debugging
  print "num unique: " + str(num_unique)
  print "num duplicates: " + str(num_duplicates)
  print "total: " + str(len(words))

  # print the solution
  print "solution: " + str(num_unique * num_duplicates)