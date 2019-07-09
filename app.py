from flask import Flask, jsonify
import random

from quotes import famous_quotes

app = Flask(__name__)


@app.route("/api/quote")
def serve_famous_quote():
    quotes = famous_quotes()
    num_of_quotes = len(quotes)
    quote = random.choice(quotes)
    return jsonify(quote)

if __name__ == "__main__":
    app.run(debug=True)