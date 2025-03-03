"""Main script, uses other modules to generate sentences."""
from flask import Flask
from .histogram import histogram
from .markov import MarkovChain
# import random

app = Flask(__name__)

# hist = histogram("Code/data/alice_in_wonderland.txt")
hist = histogram("Code/data/sample.txt")
word_list = list(hist.keys())
markov_chain = MarkovChain(word_list)

@app.route("/")

def home():
#   words = list(hist.keys()) 
#   sentence_length = random.randint(20, 30)
#   # generating rand words & joining w spaces
#   random_words = [words[random.randint(0, len(words) - 1)] for _ in range(sentence_length)]
#   sentence = " ".join(random_words) 
  sentence = markov_chain.generate_sentence()
  return f"<p>{sentence}</p>"


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
