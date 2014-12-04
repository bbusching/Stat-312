import sys
from nltk.corpus import brown
from nltk.corpus import webtext
from nltk.corpus import inaugural
from nltk.corpus import gutenberg
from nltk.corpus import genesis
from nltk.probability import FreqDist


def main():
  # store word lengths
  brown_common_freq = []
  web_common_freq = []
  inaugural_common_freq = []
  gutenberg_common_freq = []
  genesis_common_freq = []

  common = ["the", "be", "to", "of", "and", "a", "in", "that", "have",
            "i", "it", "for", "not", "on", "with", "he", "as", "you",
            "do", "at", "this", "but", "his", "by", "from", "they",
            "we", "say", "her", "she", "or", "an", "will", "my", "one",
            "all", "would", "there", "their", "what", "so", "up", "out",
            "if", "about", "who", "get", "which", "go", "me", "when",
            "make", "can", "like", "time", "no", "just", "him", "know",
            "take", "people", "into", "year", "your", "good", "some",
            "could", "them", "see", "other", "than", "then", "now", "look",
            "only", "come", "its", "over", "think", "also", "back", "after",
            "use", "two", "how", "our", "work", "first", "well", "way",
            "even", "new", "want", "because", "any", "these", "give", "day",
            "most", "us"]
  common.sort()

  for file in gutenberg.fileids():
    total_words = len(gutenberg.words(file))
    total_common = 0
    for word in gutenberg.words(file):
      if word.lower() in common:
        total_common += 1
    gutenberg_common_freq.append(float(total_common)/total_words)

  for file in brown.fileids():
    total_words = len(brown.words(file))
    total_common = 0
    for word in brown.words(file):
      if word.lower() in common:
        total_common += 1
    brown_common_freq.append(float(total_common)/total_words)

  for file in webtext.fileids():
    total_words = len(webtext.words(file))
    total_common = 0
    for word in webtext.words(file):
      if word.lower() in common:
        total_common += 1
    web_common_freq.append(float(total_common)/total_words)

  for file in inaugural.fileids():
    total_words = len(inaugural.words(file))
    total_common = 0
    for word in inaugural.words(file):
      if word.lower() in common:
        total_common += 1
    inaugural_common_freq.append(float(total_common)/total_words)

  for file in genesis.fileids():
    total_words = len(genesis.words(file))
    total_common = 0
    for word in genesis.words(file):
      if word.lower() in common:
        total_common += 1
    genesis_common_freq.append(float(total_common)/total_words)

  with open("common-words.txt", 'w') as f:
    sys.stdout = f
    f.write("GENESIS, INAUGURAL, WEBTEXT, BROWN, GUTENBERG\n")
    for i in xrange(max(len(genesis_common_freq), len(inaugural_common_freq),
                        len(web_common_freq), len(brown_common_freq),
                        len(gutenberg_common_freq))):
      for corpus in [genesis_common_freq, inaugural_common_freq,
                     web_common_freq, brown_common_freq, gutenberg_common_freq]:
        if i >= len(corpus):
          f.write(",")
        else:
          f.write(str(round(corpus[i], 5)) + ",")
      f.write("\n")



if __name__ == "__main__":
  main()

