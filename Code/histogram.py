import re

def histogram (source_text):
    with open(source_text, 'r') as file:
        text = file.read().lower() 
        words = re.findall(r"\b[a-zA-Z']+\b", text) 
        return words  
    

def unique_words (histogram):
    return len(set(histogram))


def frequency (word, histogram):
    return histogram.count(word.lower().strip())

# text = histogram('data/alice_in_wonderland.txt')
# print(f"Unique words: {unique_words(text)}")
# print(f"Frequency: {frequency("wonderland", text)}")