import sys
import string
import nltk
from nltk.corpus import brown
from nltk.corpus import webtext
from nltk.corpus import inaugural
from nltk.corpus import gutenberg
from nltk.probability import FreqDist #(or ConditionalFDist()?)

def main():
#store FreqDist's
#index is the length of the word, 0 is for all words
  english_letters = LetFreq()
  brown_letters = LetFreq()
  web_letters = LetFreq()
  inaugural_letters = LetFreq()
  gutenberg_letters = LetFreq()

  for file in gutenberg.fileids():
    for word in gutenberg.words(file):
      for character in word:
        if(character in string.letters and len(word) < 30):
          english_letters.add_obsv(len(word), character.lower())
          english_letters.add_obsv(0, character.lower())
          gutenberg_letters.add_obsv(len(word), character.lower())
          gutenberg_letters.add_obsv(0, character.lower())

  for file in brown.fileids():
    for word in brown.words(file):
      for character in word:
        if(character in string.letters and len(word) < 30):
          english_letters.add_obsv(len(word), character.lower())
          english_letters.add_obsv(0, character.lower())
          brown_letters.add_obsv(0, character.lower())
          brown_letters.add_obsv(len(word), character.lower())

  for file in webtext.fileids():
    for word in webtext.words(file):
      for character in word:
        if(character in string.letters) and len(word) < 30:
          english_letters.add_obsv(len(word), character.lower())
          english_letters.add_obsv(0, character.lower())
          web_letters.add_obsv(0, character.lower())
          web_letters.add_obsv(len(word), character.lower())

  for file in inaugural.fileids():
    for word in inaugural.words(file):
      for character in word:
        if(character in string.letters and len(word) < 30):
          english_letters.add_obsv(len(word), character.lower())
          english_letters.add_obsv(0, character.lower())
          inaugural_letters.add_obsv(0, character.lower())
          inaugural_letters.add_obsv(len(word), character.lower())

  with open("results.txt",'w') as f:
    sys.stdout = f
    f.write("ENGLISH\n")
    f.write("---------------------\n")
    english_letters.tabulate()
    f.write("\n\n\n")
    f.write("GUTENBERG\n")
    f.write("---------------------\n")
    gutenberg_letters.tabulate()
    f.write("\n\n\n")
    f.write("WEBTEXT\n")
    f.write("---------------------\n")
    web_letters.tabulate()
    f.write("\n\n\n")
    f.write("INAUGURAL\n")
    f.write("---------------------\n")
    inaugural_letters.tabulate()
    f.write("\n\n\n")
    f.write("BROWN\n")
    f.write("---------------------\n")
    brown_letters.tabulate()
    f.write("\n\n\n")




class LetFreq():
  def __init__(self):
    self.freq_dists = []
    for i in range(30): #(30-1) is the longest length word
      self.freq_dists.append(FreqDist())

  def add_obsv(self, length, obsv):
    self.freq_dists[length][obsv] += 1

  def get_fdist(self, length):
    return self.freq_dists[length]

  def tabulate(self):
    for i in range(len(self.freq_dists)):
      print("Length: " + str(i))
      self.freq_dists[i].tabulate()

  def __repr__(self):
    string_builder = []
    for fdist in self.freq_dists:
      string_builder.append(fdist)
    return "\n".join(string_builder)

  def __str__(self):
    string_builder = []
    for fdist in self.freq_dists:
      string_builder.append(fdist)
    string = "".join(string_builder.__repr__())
    return string


if __name__=="__main__":
  main()

