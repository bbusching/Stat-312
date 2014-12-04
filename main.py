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

  with open("genesis-letter-freq.txt",'w') as f:
    sys.stdout = f
    f.write("GENESIS\n")
    for let in samples:
        print(str(genesis_letters[let]))
  
  with open("gutenberg-letter-freq.txt", 'w') as f:
    sys.stdout = f
    f.write("GUTENBERG\n")
    for let in samples:
        print(str(gutenberg_letters[let]))
  with open("webtext-letter-freq.txt", 'w') as f:
    sys.stdout = f
    f.write("WEBTEXT\n")
    for let in samples:
        print(str(web_letters[let]))
  with open("inaugural-letter-freq.txt", 'w') as f:
    sys.stdout = f

    f.write("INAUGURAL\n")
    for let in samples:
        print(str(inaugural_letters[let]))
  with open("brown-letter-freq.txt", 'w') as f:
    sys.stdout = f

    f.write("BROWN\n")
    for let in samples:
        print(str(brown_letters[let]))
  
  with open("letter-freq.txt", 'w') as f:
    corpora = [gutenberg_letters, web_letters, inaugural_letters,
        brown_letters, genesis_letters]
    f.write("GUTENBERG,WEBTEXT,INAUGURAL,BROWN,GENESIS\n")
    for let in samples:
      for corpus in corpora:
        f.write(str(corpus[let]) + ",")
      f.write("\n")


if __name__=="__main__":
  main()

