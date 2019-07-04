from textblob import TextBlob
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/analyse/sentiment", methods=['POST'])
def analyse_sentiment():
    print(request.get_json())
    sentence = request.get_json()['sentence']
    if sentence:
        polarity = TextBlob(sentence).sentences[0].polarity
        return jsonify(
            sentence=sentence,
            polarity=polarity
        )
    else:
        return jsonify(
            sentence=sentence,
            polarity=0
        )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
