import random
import sys

def rearrange_words(words):
    random.shuffle(words)
    return ' '.join(words)

if __name__ == '__main__':
    words = sys.argv[1:]
    print(rearrange_words(words))