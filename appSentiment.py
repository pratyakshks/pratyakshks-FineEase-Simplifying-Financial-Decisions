from flask import Flask, render_template, request
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer


app = Flask(__name__)

# Ensure required NLTK data is downloaded
nltk.download('punkt')
nltk.download('vader_lexicon')

@app.route("/", methods=["GET", "POST"])
def index():
    sentiment = ""
    statement = ""
    if request.method == "POST":
        # Get the feedback text from the form
        statement = request.form["feedback"]

        # Perform Sentiment Analysis
        sia = SentimentIntensityAnalyzer()
        scores = sia.polarity_scores(statement)

        # Determine sentiment based on the compound score
        if scores['compound'] >= 0.05:
            sentiment = 'Positive'
        elif scores['compound'] <= -0.05:
            sentiment = 'Negative'
        else:
            sentiment = 'Neutral'

    return render_template("indexSentiment.html", sentiment=sentiment, statement=statement)

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(debug=True, host='0.0.0.0', port=5004)  # This runs the app on port 5001

