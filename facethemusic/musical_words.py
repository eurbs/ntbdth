import os
import re

# according to stackoverflow, this is available on most unix systems
# any list of words will do though
WORDPATH = os.path.join("/", "usr", "share", "dict", "words")

def main():
  with open(WORDPATH) as wordfile:
    # extract the words from the file
    wordlist = wordfile.read()
    wordlist = re.split('\W', wordlist)
    wordlist = filter(None, wordlist)

    # set because we will be checking for memebership
    words = set(wordlist)

    # populate with muscical words of length 5+
    musical_words = []
    for word in words:
      if len(word) >= 4 and re.match('[a-g](?=[a-g]+$)', word):
        musical_words.append(word)

    # order the list
    musical_words = sorted(musical_words)

    # ouput (in this simple case, just print)
    for word in musical_words:
      print word


if __name__ == "__main__": main()