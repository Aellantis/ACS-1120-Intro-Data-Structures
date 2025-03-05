"""Main script, uses other modules to generate sentences."""
from flask import Flask, render_template_string
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
  html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Random Sentence Generator</title>
        <style>
            body {
                font-family: Georgia, serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background-color: lightblue;
            }
            .container {
                background-color: white;
                padding: 5rem;
                border-radius: 30px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                text-align: center;
                max-width: 600px;
                width: 90%;
            }
            .sentence {
                font-size: 1.5rm;
                color: #333;
                line-height: 1.6;
                margin-bottom: 20px;
                padding: 10px;
            }
            .source {
                font-size: 0.9em;
                color: #666;
                margin-top: 10px;
                font-style: italic;
                padding: 10px;
            }
            .refresh {
                background-color: lightgreen;
                color: black;
                border: none;
                margin-top: 10px;
                padding: 10px 20px;
                text-decoration: none;
                border-radius: 10px;
                transition: background-color 0.3s ease;
            }
            .refresh:hover {
                background-color: lightgreen;
                color: white;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Random Sentence Generator</h1>
            <p class="source">Green Eggs and Ham by Doctor Suess</p>    
            <p class="sentence">"{{ sentences.upper() }}"</p>
            <a href="/" class="refresh">Generate </a>
        </div>
    </body>
    </html>
    """
  return render_template_string(html_template, sentences=sentence)


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
