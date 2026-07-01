from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)


def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    if polarity > 0:
        label = "Positive"
    elif polarity < 0:
        label = "Negative"
    else:
        label = "Neutral"

    return {
        "label": label,
        "polarity": round(polarity, 3),
        "subjectivity": round(subjectivity, 3),
    }


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    user_text = ""

    if request.method == "POST":
        user_text = request.form.get("text", "").strip()
        if user_text:
            result = analyze_sentiment(user_text)

    return render_template("index.html", result=result, user_text=user_text)


if __name__ == "__main__":
    app.run(debug=True)
