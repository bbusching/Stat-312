import sys
from nltk.corpus import brown
from nltk.corpus import webtext
from nltk.corpus import inaugural
from nltk.corpus import gutenberg
from nltk.corpus import genesis
from nltk.probability import FreqDist


def main():
  # store word lengths
  brown_word_lens = []
  web_word_lens = []
  inaugural_word_lens = []
  gutenberg_word_lens = []
  genesis_word_lens = []

  for file in gutenberg.fileids():
    for word in gutenberg.words(file):
      gutenberg_word_lens.append(len(word))

  for file in brown.fileids():
    for word in brown.words(file):
      brown_word_lens.append(len(word))

  for file in webtext.fileids():
    for word in webtext.words(file):
      web_word_lens.append(len(word))

  for file in inaugural.fileids():
    for word in inaugural.words(file):
      inaugural_word_lens.append(len(word))

  for file in genesis.fileids():
    for word in genesis.words(file):
      genesis_word_lens.append(len(word))
  with open("wordlens.txt", 'w') as f:
    sys.stdout = f
    f.write("GENESIS, INAUGURAL, WEBTEXT, BROWN, GUTENBERG\n")
    for i in xrange(max(len(genesis_word_lens), len(inaugural_word_lens), 
        len(web_word_lens), len(brown_word_lens),
        len(gutenberg_word_lens))):
      for corpus in [genesis_word_lens, inaugural_word_lens,
          web_word_lens, brown_word_lens, gutenberg_word_lens]:
        if(i >= len(corpus)):
          f.write(",")
        else:
          f.write(str(corpus[i]) + ",")
      f.write("\n")
#
 # with open("results2.txt", 'w') as f:
 #   sys.stdout = f
  #  f.write("GENESIS\n")
 #   f.write("---------------------\n")
 #   for obs in genesis_word_lens:
 #     f.write(str(obs) + " ")
 #   f.write("\n\n\n")
 #   f.write("GUTENBERG\n")
 #   f.write("---------------------\n")
 #   for obs in gutenberg_word_lens:
 #     f.write(str(obs) + " ")
 #   f.write("\n\n\n")
 #   f.write("WEBTEXT\n")
 #   f.write("---------------------\n")
 #   for obs in web_word_lens:
 #     f.write(str(obs) + " ")
 #   f.write("\n\n\n")
 #   f.write("INAUGURAL\n")
 #   f.write("---------------------\n")
 #   for obs in inaugural_word_lens:
 #     f.write(str(obs) + " ")
 #   f.write("\n\n\n")
 #   f.write("BROWN\n")
 #   f.write("---------------------\n")
 #   for obs in brown_word_lens:
  #    f.write(str(obs) + " ")
  #  f.write("\n\n\n")


if __name__ == "__main__":
  main()

