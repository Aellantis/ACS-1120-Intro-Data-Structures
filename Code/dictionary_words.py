import random
import sys

def dictionary_words(word_count):
  with open("/usr/share/dict/words", "r") as file:
    words = file.read().split()
    return ' '.join(random.choices(words, k=word_count))

if __name__ == '__main__':
  word_count = int(sys.argv[1])
  print(dictionary_words(word_count))
