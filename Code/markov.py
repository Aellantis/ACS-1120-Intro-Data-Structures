from dictogram import Dictogram
import random

class MarkovChain:
    def __init__(self, word_list=None):
        self.states = {}
        self.word_list = word_list if word_list else []
        self.types = 0
        self.tokens = 0
        if self.word_list:
            self.markov_chain()
    
    def markov_chain(self):
        for i in range(len(self.word_list) - 1):
            word, next_word = self.word_list[i], self.word_list[i + 1]
            if word not in self.states:
                self.states[word] = Dictogram()
                self.types += 1
            self.states[word].add_count(next_word)
            self.tokens += 1
    
    def sample(self, word):
        return self.states[word].sample() if word in self.states else None
    
    def generate_sentence(self, length=10):
        if not self.word_list:
            return ""

        sentence = []
        word = random.choice(self.word_list)
        for _ in range(length):
            sentence.append(word)
            word = self.sample(word)
            if word is None:
                word = random.choice(self.word_list)
        return ' '.join(sentence)
    
    def print_markov_chain(self, word_list):
        print("\nMarkov Chain:")
        for word, histogram in self.states.items():
            print(f"{word}: {dict(histogram)}")
    
    def print_markov_chain_samples(self, markov_chain):
        print('Markov Chain samples:')
        # Sample the Markov chain 10,000 times and count frequency of results
        samples_list = [markov_chain.generate_sentence() for _ in range(10000)]
        samples_hist = Dictogram(samples_list)
        print('samples: {}'.format(samples_hist))
        print()

if __name__ == '__main__':
    word_list = ['I', 'like', 'cats', 'and', 'dogs']
    markov_chain = MarkovChain(word_list)
    
    print("Generated Sentence:")
    print(markov_chain.generate_sentence())
    
    markov_chain.print_markov_chain(word_list)