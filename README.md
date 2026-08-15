# 🤖 Product Reviews Sentiment Analysis

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?logo=scikit-learn)
![NLP](https://img.shields.io/badge/NLP-Sentiment%20Analysis-green)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue?logo=sqlite)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

# 📌 Project Overview

This project is an **AI-powered Product Reviews Sentiment Analysis application** built using Python, Natural Language Processing (NLP), Machine Learning, and Flask.

The application analyzes customer product reviews and classifies them into:

- 😊 Positive
- 😐 Neutral
- 😞 Negative

The project demonstrates practical skills in:

- Natural Language Processing
- Text Preprocessing
- TF-IDF Vectorization
- Machine Learning
- Model Evaluation
- Flask Web Development
- Data Visualization
- SQLite Database Management

---

# 🎯 Business Problem

Online platforms receive thousands of customer reviews every day.

Manually analyzing these reviews is time-consuming and difficult.

The objective of this project is to automatically analyze customer feedback and answer questions like:

- Is the customer satisfied with the product?
- Is the review positive, neutral, or negative?
- How confident is the model in its prediction?
- What are the most common sentiments?
- How well does the machine learning model classify reviews?

---

# 🛠️ Tech Stack

- Python
- Flask
- Pandas
- NumPy
- Scikit-Learn
- NLTK
- TF-IDF
- Logistic Regression
- SQLite
- HTML
- CSS
- JavaScript
- Chart.js
- ReportLab

---

# 🧠 Machine Learning Approach

The project uses **Natural Language Processing (NLP)** and **Logistic Regression** for sentiment classification.

### Machine Learning Pipeline

```text
Customer Review
       ↓
Text Cleaning
       ↓
NLP Preprocessing
       ↓
TF-IDF Vectorization
       ↓
Logistic Regression
       ↓
Sentiment Prediction
       ↓
Confidence Score

##📊 Model Performance

The dataset was balanced before training to improve classification performance across all sentiment classes.
Balanced Dataset
| Sentiment | Samples |
| --------- | ------- |
| Negative  | 5,000   |
| Neutral   | 5,000   |
| Positive  | 5,000   |

Total Samples: 15,000

Model Accuracy

87.8%
| Class             | Precision | Recall   | F1-Score |
| ----------------- | --------- | -------- | -------- |
| Negative          | 0.91      | 0.95     | 0.93     |
| Neutral           | 0.85      | 0.85     | 0.85     |
| Positive          | 0.88      | 0.83     | 0.85     |
| **Macro Average** | **0.88**  | **0.88** | **0.88** |

##📂 Project Structure
```
Product-Reviews-Sentiment-Analysis/
│
├── dataset/
│   └── reviews.csv
│
├── images/
│   ├── confusion_matrix.png
│   ├── model_comparison.png
│   └── sentiment_distribution.png
│
├── model/
│   ├── sentiment_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── notebooks/
│   └── sentiment_analysis.ipynb
│
├── static/
│   ├── css/
│   └── js/
│
├── templates/
│   └── index.html
│
├── app.py
├── database.py
├── train_model.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 📊 Visualizations

## Sentiment Distribution

<img
  src="https://github.com/user-attachments/assets/8837257c-f058-4d08-beac-e051cc9542b5"
  alt="Sentiment Distribution"
  width="800"
/>

---

## Confusion Matrix

<img
  src="https://github.com/user-attachments/assets/70889e95-5298-494d-b5cc-6a4d977343dc"
  alt="Confusion Matrix"
  width="800"
/>

---

## Model Comparison

<img
  src="https://github.com/user-attachments/assets/afcc6e24-cba0-41f4-989a-b446ffb18fff"
  alt="Model Comparison"
  width="800"
/>
---
##🔍 Example Predictions
##Positive Review
```
"The product is amazing and the quality is excellent."
```

Prediction: Positive

Confidence: 98.31%

##Negative Review
```
"Very poor quality and I am completely disappointed."
```
Prediction: Negative

Confidence: 89.11%

##Negative Review with Negation
```
"The product is not good and I do not recommend it."
```
Prediction: Negative

Confidence: 71.04%
---
#✨ Features
📝 Product review analysis
🤖 AI-powered sentiment prediction
😊 Positive / Neutral / Negative classification
📊 Confidence score
📈 Sentiment statistics
📋 Prediction history
🔍 Keyword extraction
📄 PDF report generation
🎤 Voice input
🌙 Dark / Light mode
📊 Interactive charts
💾 SQLite database
---

##📈 Key Insights
The model achieved approximately 87.8% accuracy.
The dataset was balanced using 5,000 samples for each sentiment class.
Negative reviews achieved the highest recall at 0.95.
TF-IDF was used to convert text reviews into numerical features.
Logistic Regression was used as the final sentiment classification model.
The application provides confidence scores along with predictions.
Prediction history is stored using SQLite.
---
##💾 Database

The application uses SQLite to store prediction history.

The database records information such as:

Review
Sentiment
Confidence score
Processing time
Word count
Prediction date and time

The generated database file is excluded from GitHub using .gitignore.
---
##📄 PDF Report

The application provides an option to generate a PDF report containing sentiment prediction information.

Generated PDF files are kept locally and are excluded from GitHub.

##▶️ How to Run
Clone the Repository
```bash
git clone https://github.com/alishamansoori004-sketch/Product-Reviews-Sentiment-Analysis.git
```
Go into the Project Folder
```bash
cd Product-Reviews-Sentiment-Analysis
```
Create Virtual Environment
```bash
python -m venv venv
```
Activate Virtual Environment

Windows:
```bash
venv\Scripts\activate
```
Linux / macOS:
```bash
source venv/bin/activate
```
Install Dependencies
```bash
pip install -r requirements.txt
```
Download NLTK Resources

Open Python and run:
```bash
import nltk
```
```bash
nltk.download('stopwords')
nltk.download('punkt')
```
Train the Model
```
python train_model.py
Run Flask Application
python app.py
```

Open your browser:
```bash
http://127.0.0.1:5000
```
#📁 Dataset

The project uses a Product Reviews Dataset containing customer reviews and sentiment labels.

The dataset is stored in:
```
dataset/reviews.csv
```

---

##🚀 Future Improvements
Improve sentiment classification accuracy
Add BERT-based sentiment analysis
Add deep learning models
Add multilingual sentiment analysis
Add real-time analytics dashboard
Add user authentication
Deploy with a production database
Add more advanced NLP features

---

#👩‍💻 Author

**Alisha Mansoori**

B.Tech – Artificial Intelligence & Data Science

AI & Data Analytics Enthusiast

GitHub:

https://github.com/alishamansoori004-sketch

Portfolio:

https://aqiqafatima2.wixsite.com/aqiqa-fatima
---

##⭐ If you found this project useful

Please consider giving this repository a ⭐ on GitHub.
