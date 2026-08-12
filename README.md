# 🤖 AI Product Review Sentiment Analyzer

An AI-powered web application that analyzes product reviews and automatically classifies them as **Positive, Neutral, or Negative** using Natural Language Processing (NLP) and Machine Learning.

The application provides sentiment prediction, confidence score, probability visualization, keyword extraction, prediction history, PDF report generation, and voice input through a modern Flask-based interface.

---

## 🚀 Features

- 🤖 AI-based sentiment prediction
- 😊 Positive / 😐 Neutral / 😞 Negative classification
- 🎯 Prediction confidence score
- 📊 Sentiment probability chart
- 🔑 Top keyword extraction
- 🕒 Prediction history
- 📄 Downloadable PDF prediction report
- 🎤 Voice-based review input
- 🌙 Dark / Light mode
- ⚡ Processing-time measurement
- 📝 Word-count analysis
- ✨ Animated AI analysis interface
- 🌌 Interactive particle background
- 📱 Responsive user interface

---

## 🧠 Machine Learning

The sentiment analysis model uses:

- **TF-IDF Vectorization**
- **Unigrams + Bigrams**
- **Logistic Regression**
- **NLTK Stopword Removal**
- **Text Cleaning**
- **Balanced Dataset**

### Text Processing Pipeline

```text
Raw Review
     ↓
Lowercase Conversion
     ↓
URL Removal
     ↓
Special Character Removal
     ↓
Stopword Removal
     ↓
Cleaned Text
     ↓
TF-IDF Vectorization
     ↓
Logistic Regression
     ↓
Sentiment Prediction

📊 Model Performance

The original dataset was highly imbalanced, with significantly more positive reviews than neutral and negative reviews.

To improve class representation, the training dataset was balanced using oversampling.

Balanced Dataset
Sentiment	Samples
Negative	5,000
Neutral	5,000
Positive	5,000
Total	15,000
Training Configuration
Training samples: 12,000
Testing samples: 3,000
Maximum TF-IDF features: 10,000
N-gram range: (1, 2)
Logistic Regression iterations: 1,000
Class weighting: Balanced
Accuracy

87.8%

Classification Report
Sentiment	Precision	Recall	F1-Score
Negative	0.91	    0.95	    0.93
Neutral 	0.85	    0.85	    0.85
Positive	0.88	    0.83	    0.85
Macro Avg	0.88	    0.88	    0.88

🛠️ Tech Stack

Programming Language
Python

Machine Learning
Scikit-learn
Logistic Regression
TF-IDF

Natural Language Processing
NLTK
Text preprocessing
Stopword removal

Backend
Flask

Database
SQLite

Frontend
HTML5
CSS3
JavaScript
Chart.js

Additional Tools
ReportLab
Particles.js
Web Speech API
Git & GitHub