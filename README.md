Sentiment Analyzer

A simple Flask web app that analyzes the sentiment of text using TextBlob. Enter any text and instantly see whether it's positive, negative, or neutral — along with polarity and subjectivity scores.


Features

Clean, single-page web UI
Real-time sentiment classification: Positive / Negative / Neutral
Polarity score (-1 to +1)
Subjectivity score (0 to 1)
No JavaScript — simple server-rendered form


Tech Stack

Flask — Python web framework
TextBlob — NLP library for sentiment analysis
HTML/CSS — frontend (Jinja2 templating)


Getting Started

Prerequisites

Python 3.8+
pip


Installation

Clone the repository


bash   git clone <your-repo-url>
   cd <your-repo-folder>


(Optional but recommended) Create a virtual environment


bash   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate


Install dependencies


bash   pip install -r requirements.txt


Download TextBlob's NLTK corpora (required for sentiment analysis)


bash   python -m textblob.download_corpora

Running the App

bashpython app.py

Then open your browser and go to:

http://localhost:5000

Usage


Type or paste text into the textarea.
Click Analyze.
View the sentiment label and scores below the form.


Project Structure

.
├── app.py              # Flask backend & sentiment logic
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html      # Frontend template
└── README.md
