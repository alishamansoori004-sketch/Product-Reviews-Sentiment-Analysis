import pandas as pd
import pickle
import re
import nltk

from nltk.corpus import stopwords

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# ==========================================
# NLTK
# ==========================================

nltk.download("stopwords")


# ==========================================
# LOAD DATASET
# ==========================================

df = pd.read_csv(
    "dataset/reviews.csv",
    low_memory=False
)


# ==========================================
# KEEP REQUIRED COLUMNS
# ==========================================

df = df[
    ["reviews.text", "reviews.rating"]
].dropna()


# ==========================================
# CONVERT RATING TO SENTIMENT
# ==========================================

def convert_sentiment(rating):

    rating = float(rating)

    if rating >= 4:
        return "Positive"

    elif rating == 3:
        return "Neutral"

    else:
        return "Negative"


df["sentiment"] = df[
    "reviews.rating"
].apply(convert_sentiment)


# ==========================================
# STOPWORDS
# ==========================================

stop_words = set(
    stopwords.words("english")
)


# IMPORTANT:
# Keep sentiment-changing words.
# Removing "not" can completely change
# the meaning of a review.

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
# TEXT CLEANING
# ==========================================

def clean_text(text):

    text = str(text).lower()

    # Remove URLs
    text = re.sub(
        r"http\S+",
        "",
        text
    )

    # Keep letters and spaces
    text = re.sub(
        r"[^a-zA-Z\s]",
        "",
        text
    )

    # Remove extra spaces
    text = re.sub(
        r"\s+",
        " ",
        text
    ).strip()

    # Remove stopwords
    words = [
        word
        for word in text.split()
        if word not in stop_words
    ]

    return " ".join(words)


df["reviews.text"] = df[
    "reviews.text"
].apply(clean_text)


# ==========================================
# REMOVE EMPTY REVIEWS
# ==========================================

df = df[
    df["reviews.text"].str.strip() != ""
]


# ==========================================
# FEATURES & TARGET
# ==========================================

X = df["reviews.text"]

y = df["sentiment"]

from sklearn.utils import resample

# Combine text and sentiment
training_df = pd.DataFrame({
    "text": X,
    "sentiment": y
})

# Separate classes
positive_df = training_df[training_df["sentiment"] == "Positive"]
neutral_df = training_df[training_df["sentiment"] == "Neutral"]
negative_df = training_df[training_df["sentiment"] == "Negative"]

# Use 5000 samples from Positive
positive_sample = resample(
    positive_df,
    replace=False,
    n_samples=5000,
    random_state=42
)

# Oversample minority classes
neutral_sample = resample(
    neutral_df,
    replace=True,
    n_samples=5000,
    random_state=42
)

negative_sample = resample(
    negative_df,
    replace=True,
    n_samples=5000,
    random_state=42
)

# Combine balanced dataset
balanced_df = pd.concat([
    positive_sample,
    neutral_sample,
    negative_sample
])

# Shuffle
balanced_df = balanced_df.sample(
    frac=1,
    random_state=42
).reset_index(drop=True)

X = balanced_df["text"]
y = balanced_df["sentiment"]

print("\nBalanced Sentiment Distribution:")
print(y.value_counts())


# ==========================================
# CHECK DATA BALANCE
# ==========================================

print("\nSentiment Distribution:")
print(
    y.value_counts()
)


# ==========================================
# TRAIN / TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,

    test_size=0.20,

    random_state=42,

    stratify=y
)


# ==========================================
# TF-IDF VECTORIZER
# ==========================================

vectorizer = TfidfVectorizer(

    max_features=10000,

    ngram_range=(1, 2),

    sublinear_tf=True
)


# ==========================================
# TRANSFORM TEXT
# ==========================================

X_train_vec = vectorizer.fit_transform(
    X_train
)

X_test_vec = vectorizer.transform(
    X_test
)


print(
    "\nTraining samples:",
    X_train_vec.shape[0]
)

print(
    "Features:",
    X_train_vec.shape[1]
)


# ==========================================
# LOGISTIC REGRESSION
# ==========================================

model = LogisticRegression(

    max_iter=1000,

    class_weight="balanced",

)


# ==========================================
# TRAIN MODEL
# ==========================================

print("\nTraining model...")

model.fit(
    X_train_vec,
    y_train
)


# ==========================================
# PREDICTION
# ==========================================

pred = model.predict(
    X_test_vec
)


# ==========================================
# ACCURACY
# ==========================================

accuracy = accuracy_score(
    y_test,
    pred
)

print(
    "\nAccuracy:",
    round(accuracy * 100, 2),
    "%"
)


# ==========================================
# CLASSIFICATION REPORT
# ==========================================

print("\nClassification Report:")

print(
    classification_report(
        y_test,
        pred
    )
)


# ==========================================
# CONFUSION MATRIX
# ==========================================

print("\nConfusion Matrix:")

print(
    confusion_matrix(
        y_test,
        pred
    )
)


# ==========================================
# SAVE MODEL
# ==========================================

with open(
    "model/sentiment_model.pkl",
    "wb"
) as f:

    pickle.dump(
        model,
        f
    )


# ==========================================
# SAVE VECTORIZER
# ==========================================

with open(
    "model/vectorizer.pkl",
    "wb"
) as f:

    pickle.dump(
        vectorizer,
        f
    )


# ==========================================
# SUCCESS
# ==========================================

print(
    "\n=========================================="
)

print(
    "Model trained successfully!"
)

print(
    "Model saved to:"
)

print(
    "model/sentiment_model.pkl"
)

print(
    "model/vectorizer.pkl"
)

print(
    "=========================================="
)