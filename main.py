from __future__ import print_function
import sys
import string
import nltk
from nltk.corpus import brown
from nltk.corpus import webtext
from nltk.corpus import inaugural
from nltk.corpus import gutenberg
from nltk.corpus import genesis
from nltk.probability import FreqDist #(or ConditionalFDist()?)

def main():
#store FreqDist's
#index is the length of the word, 0 is for all words
  samples = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

  brown_letters = FreqDist()
  web_letters = FreqDist()
  inaugural_letters = FreqDist()
  gutenberg_letters = FreqDist()
  genesis_letters = FreqDist()

  for file in gutenberg.fileids():
    for word in gutenberg.words(file):
      for character in word:
        if(character in string.letters):
            gutenberg_letters[character.upper()] += 1

  for file in brown.fileids():
    for word in brown.words(file):
      for character in word:
        if(character in string.letters):
            brown_letters[character.upper()] += 1

  for file in webtext.fileids():
    for word in webtext.words(file):
      for character in word:
        if(character in string.letters):
            web_letters[character.upper()] += 1

  for file in inaugural.fileids():
    for word in inaugural.words(file):
      for character in word:
        if(character in string.letters):
            inaugural_letters[character.upper()] += 1

  for file in genesis.fileids():
    for word in genesis.words(file):
      for character in word:
        if(character in string.letters):
            genesis_letters[character.upper()] += 1

  with open("results.txt",'w') as f:
    sys.stdout = f
    f.write("GENESIS\n")
    f.write("---------------------\n")
    for let in samples:
        f.write(let + "\t\t")
    f.write("\n")
    for let in samples:
        print("%.5f\t" % genesis_letters.freq(let), end='')
    f.write("\n\n\n")
    f.write("GUTENBERG\n")
    f.write("---------------------\n")
    for let in samples:
        f.write(let + "\t\t")
    f.write("\n")
    for let in samples:
        print("%.5f\t" % gutenberg_letters.freq(let), end='')
    f.write("\n\n\n")
    f.write("WEBTEXT\n")
    f.write("---------------------\n")
    for let in samples:
        f.write(let + "\t\t")
    f.write("\n")
    for let in samples:
        print("%.5f\t" % web_letters.freq(let), end='')

    f.write("\n\n\n")
    f.write("INAUGURAL\n")
    f.write("---------------------\n")
    for let in samples:
        f.write(let + "\t\t")
    f.write("\n")
    for let in samples:
        print("%.5f\t" % inaugural_letters.freq(let), end='')

    f.write("\n\n\n")
    f.write("BROWN\n")
    f.write("---------------------\n")
    for let in samples:
        f.write(let + "\t\t")
    f.write("\n")
    for let in samples:
        print("%.5f\t" % brown_letters.freq(let), end='')

    f.write("\n\n\n")


if __name__=="__main__":
  main()

