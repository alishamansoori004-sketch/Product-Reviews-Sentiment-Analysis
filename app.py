import sqlite3
from datetime import datetime

from flask import Flask, render_template, request, send_file

import pickle
import re
import nltk
import time

from nltk.corpus import stopwords

from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from database import create_database

# ==========================================
# FLASK APP
# ==========================================

app = Flask(__name__)
create_database()

# ==========================================
# NLTK
# ==========================================

nltk.download("stopwords")

stop_words = set(stopwords.words("english"))

important_words = {
    "not",
    "no",
    "never",
    "nor",
    "neither",
    "hardly",
    "barely",
    "nothing"
}

stop_words = stop_words - important_words


# ==========================================
# DATABASE
# ==========================================

DATABASE = "reviews.db"


def get_db_connection():

    conn = sqlite3.connect(DATABASE)

    conn.row_factory = sqlite3.Row

    return conn


def save_prediction(
    review,
    prediction,
    confidence,
    processing_time,
    word_count
):

    conn = get_db_connection()

    conn.execute(
        """
        INSERT INTO reviews
        (
            review,
            prediction,
            confidence,
            processing_time,
            word_count,
            created_at
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            review,
            prediction,
            confidence,
            processing_time,
            word_count,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
    )

    conn.commit()

    conn.close()


def get_history():

    conn = get_db_connection()

    rows = conn.execute(
        """
        SELECT *
        FROM reviews
        ORDER BY id DESC
        """
    ).fetchall()

    conn.close()

    return rows


# ==========================================
# LOAD MODEL & VECTORIZER
# ==========================================

with open(
    "model/sentiment_model.pkl",
    "rb"
) as f:

    model = pickle.load(f)


with open(
    "model/vectorizer.pkl",
    "rb"
) as f:

    vectorizer = pickle.load(f)


# ==========================================
# LAST PREDICTION
# ==========================================

last_prediction = {}


# ==========================================
# TEXT CLEANING
# ==========================================

def clean_text(text):

    text = text.lower()

    text = re.sub(
        r"http\S+",
        "",
        text
    )

    text = re.sub(
        r"[^a-zA-Z\s]",
        "",
        text
    )

    text = re.sub(
        r"\s+",
        " ",
        text
    ).strip()

    words = text.split()

    words = [
        word
        for word in words
        if word not in stop_words
    ]

    return " ".join(words)


# ==========================================
# HOME PAGE
# ==========================================

@app.route("/")
def home():

    history = get_history()

    positive_count = sum(
        1
        for item in history
        if item["prediction"] == "Positive"
    )

    negative_count = sum(
        1
        for item in history
        if item["prediction"] == "Negative"
    )

    neutral_count = sum(
        1
        for item in history
        if item["prediction"] == "Neutral"
    )

    total_predictions = len(history)

    return render_template(
        "index.html",
        history=history,
        positive_count=positive_count,
        negative_count=negative_count,
        neutral_count=neutral_count,
        total_predictions=total_predictions
    )


# ==========================================
# PREDICTION
# ==========================================

@app.route(
    "/predict",
    methods=["POST"]
)
def predict():

    global last_prediction

    # --------------------------------------
    # Get review
    # --------------------------------------

    review = request.form.get(
        "review",
        ""
    ).strip()

    if not review:

        return render_template(
            "index.html",
            history=get_history()
        )


    # --------------------------------------
    # Start timer
    # --------------------------------------

    start = time.time()


    # --------------------------------------
    # Clean text
    # --------------------------------------

    cleaned = clean_text(review)


    # --------------------------------------
    # Vectorize
    # --------------------------------------

    vector = vectorizer.transform(
        [cleaned]
    )


    # --------------------------------------
    # Prediction
    # --------------------------------------

    prediction = model.predict(
        vector
    )[0]


    # --------------------------------------
    # Probabilities
    # --------------------------------------

    probabilities = model.predict_proba(
        vector
    )[0]


    # --------------------------------------
    # Confidence
    # --------------------------------------

    confidence = round(
        max(probabilities) * 100,
        2
    )


    # --------------------------------------
    # Labels
    # --------------------------------------

    labels = model.classes_.tolist()


    # --------------------------------------
    # Chart scores
    # --------------------------------------

    scores = [
        round(x * 100, 2)
        for x in probabilities
    ]


    # --------------------------------------
    # Processing time
    # --------------------------------------

    processing_time = round(
        time.time() - start,
        3
    )


    # --------------------------------------
    # Word count
    # --------------------------------------

    word_count = len(
        review.split()
    )


    # ======================================
    # KEYWORD EXTRACTION
    # ======================================

    keywords = []

    for word in cleaned.split():

        if (
            len(word) > 3
            and word not in keywords
        ):

            keywords.append(word)


    keywords = keywords[:6]


    # ======================================
    # AI SUGGESTION
    # ======================================

    if prediction == "Positive":

        suggestion = (
            "Customers are highly satisfied "
            "with this product. "
            "Recommended for purchase."
        )

    elif prediction == "Negative":

        suggestion = (
            "This review indicates "
            "dissatisfaction. "
            "Consider checking customer "
            "complaints before purchasing."
        )

    else:

        suggestion = (
            "Mixed opinions detected. "
            "Read more customer reviews "
            "before making a decision."
        )


    # ======================================
    # SAVE TO DATABASE
    # ======================================

    save_prediction(
        review,
        prediction,
        confidence,
        processing_time,
        word_count
    )


   
    
  

   


    # ======================================
    # GET UPDATED HISTORY
    # ======================================

    history = get_history()

    # ======================================
    # DASHBOARD COUNTS
    # ======================================

    positive_count = sum(
        1
        for item in history
        if item["prediction"] == "Positive"
    )

    negative_count = sum(
        1
        for item in history
        if item["prediction"] == "Negative"
    )

    neutral_count = sum(
        1
        for item in history
        if item["prediction"] == "Neutral"
    )

    total_predictions = len(history)

    # ======================================
    # STORE LAST PREDICTION
    # ======================================

    last_prediction = {
        "review": review,
        "prediction": prediction,
        "confidence": confidence,
        "processing_time": processing_time,
        "word_count": word_count,
        "keywords": keywords,
        "suggestion": suggestion
    }

    # ======================================
    # DEBUG OUTPUT
    # ======================================

    print("=" * 60)

    print(
        "Original Review :",
        review
    )

    print(
        "Cleaned Review  :",
        cleaned
    )

    print(
        "Prediction      :",
        prediction
    )

    print(
        "Classes         :",
        labels
    )

    print(
        "Probabilities   :",
        probabilities
    )

    print(
        "Confidence      :",
        confidence
    )

    print(
        "Processing Time :",
        processing_time
    )

    print(
        "Word Count      :",
        word_count
    )

    print(
        "Keywords        :",
        keywords
    )

    print("=" * 60)

    # ======================================
    # RENDER RESULT
    # ======================================

    return render_template(
        "index.html",
        prediction=prediction,
        confidence=confidence,
        labels=labels,
        scores=scores,
        history=history,
        suggestion=suggestion,
        keywords=keywords,
        processing_time=processing_time,
        word_count=word_count,
        positive_count=positive_count,
        negative_count=negative_count,
        neutral_count=neutral_count,
        total_predictions=total_predictions
    )


# ==========================================
# DOWNLOAD PDF
# ==========================================

@app.route("/download_pdf")
def download_pdf():

    if not last_prediction:
        return "No prediction available."

    filename = "prediction_report.pdf"

    doc = SimpleDocTemplate(
        filename,
        rightMargin=50,
        leftMargin=50,
        topMargin=50,
        bottomMargin=50
    )

    styles = getSampleStyleSheet()

    title_style = styles["Title"]
    title_style.fontSize = 22
    title_style.leading = 28
    title_style.spaceAfter = 20

    heading_style = styles["Heading2"]
    heading_style.fontSize = 14
    heading_style.spaceBefore = 15
    heading_style.spaceAfter = 8

    body_style = styles["BodyText"]
    body_style.fontSize = 11
    body_style.leading = 17

    story = []

    # ==========================================
    # TITLE
    # ==========================================

    story.append(
        Paragraph(
            "AI Product Review Sentiment Analyzer",
            title_style
        )
    )

    story.append(
        Paragraph(
            "Machine Learning Sentiment Analysis Report",
            body_style
        )
    )

    story.append(Paragraph("<br/>", body_style))

    # ==========================================
    # REVIEW
    # ==========================================

    story.append(
        Paragraph(
            "Review",
            heading_style
        )
    )

    review_text = last_prediction["review"]

    story.append(
        Paragraph(
            review_text,
            body_style
        )
    )

    # ==========================================
    # SENTIMENT
    # ==========================================

    story.append(
        Paragraph(
            "Prediction Result",
            heading_style
        )
    )

    story.append(
        Paragraph(
            f"<b>Sentiment:</b> {last_prediction['prediction']}",
            body_style
        )
    )

    story.append(
        Paragraph(
            f"<b>Confidence:</b> {last_prediction['confidence']}%",
            body_style
        )
    )

    # ==========================================
    # PROCESSING DETAILS
    # ==========================================

    story.append(
        Paragraph(
            "Analysis Details",
            heading_style
        )
    )

    story.append(
        Paragraph(
            f"<b>Processing Time:</b> "
            f"{last_prediction.get('processing_time', 'N/A')} seconds",
            body_style
        )
    )

    story.append(
        Paragraph(
            f"<b>Word Count:</b> "
            f"{last_prediction.get('word_count', 'N/A')}",
            body_style
        )
    )

    # ==========================================
    # KEYWORDS
    # ==========================================

    if last_prediction.get("keywords"):

        story.append(
            Paragraph(
                "Top Keywords",
                heading_style
            )
        )

        keywords_text = ", ".join(
            last_prediction["keywords"]
        )

        story.append(
            Paragraph(
                keywords_text,
                body_style
            )
        )

    # ==========================================
    # SUGGESTION
    # ==========================================

    if last_prediction.get("suggestion"):

        story.append(
            Paragraph(
                "AI Suggestion",
                heading_style
            )
        )

        story.append(
            Paragraph(
                last_prediction["suggestion"],
                body_style
            )
        )

    # ==========================================
    # FOOTER
    # ==========================================

    story.append(
        Paragraph(
            "<br/><br/>"
            "<b>Developed using Python, Flask, "
            "Scikit-learn and Natural Language Processing.</b>",
            body_style
        )
    )

    doc.build(story)

    return send_file(
        filename,
        as_attachment=True
    )



# ==========================================
# RUN APPLICATION
# ==========================================

if __name__ == "__main__":

    app.run(
        debug=True
    )