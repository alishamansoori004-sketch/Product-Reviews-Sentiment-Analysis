



# 🤖 Product Reviews Sentiment Analysis

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?logo=scikit-learn)
![NLP](https://img.shields.io/badge/NLP-Sentiment%20Analysis-green)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue?logo=sqlite)
![License](https://img.shields.io/badge/License-MIT-yellow)

---
## 🚀 Project Links

| Resource | Link |
|---|---|
| 🌐 Live Demo | [Open Application](https://product-reviews-sentiment-analysis-cmol.onrender.com/) |
| 💻 GitHub Repository | [View Source Code](https://github.com/alishamansoori004-sketch/Product-Reviews-Sentiment-Analysis) |

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

### 🧠 Machine Learning Pipeline

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
```

---

## 📊 Model Performance

The dataset was balanced before training to improve classification performance across all sentiment classes.

### Balanced Dataset

| Sentiment | Samples |
|-----------|---------|
| Negative  | 5,000   |
| Neutral   | 5,000   |
| Positive  | 5,000   |

**Total Samples:** 15,000

### Model Accuracy

**87.8%**

| Class | Precision | Recall | F1-Score |
|-------|-----------|--------|----------|
| Negative | 0.91 | 0.95 | 0.93 |
| Neutral | 0.85 | 0.85 | 0.85 |
| Positive | 0.88 | 0.83 | 0.85 |
| **Macro Average** | **0.88** | **0.88** | **0.88** |

---


## 📂 Project Structure

```text
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
# 🔍 Example Predictions

## Positive Review

```text
"The product is amazing and the quality is excellent."
```

**Prediction:** Positive

**Confidence:** 98.31%

---

## Negative Review

```text
"Very poor quality and I am completely disappointed."
```

**Prediction:** Negative

**Confidence:** 89.11%

---

## Negative Review with Negation

```text
"The product is not good and I do not recommend it."
```

**Prediction:** Negative

**Confidence:** 71.04%

---
# ⭐ Features

- 🧠 **AI-Based Sentiment Analysis**
  - Classifies product reviews into Positive, Neutral, and Negative sentiments.

- 📊 **Confidence Score**
  - Displays the model's prediction confidence percentage.

- 📝 **Text Preprocessing**
  - Cleans reviews using text normalization and stopword processing.

- 🔤 **TF-IDF Feature Extraction**
  - Converts review text into numerical features for machine learning.

- 🤖 **Logistic Regression Model**
  - Uses Logistic Regression for sentiment classification.

- ⚖️ **Balanced Training Dataset**
  - Uses 5,000 samples from each sentiment class to reduce class imbalance.

- 📈 **Interactive Dashboard**
  - Displays sentiment statistics and prediction history.

- 💾 **Prediction History**
  - Stores previous predictions in a SQLite database.

- 📄 **PDF Report Generation**
  - Generates a downloadable PDF report containing prediction details.

- 🎤 **Voice Input**
  - Allows users to enter reviews using voice input.

- 🌙 **Dark/Light Mode**
  - Provides a user-friendly interface with theme switching.

- 📱 **Responsive UI**
  - Designed to work across different screen sizes.

- ⚡ **Fast Flask Backend**
  - Provides real-time sentiment predictions through a Flask web application.

# 📊 Key Insights

- ⚖️ **Balanced Dataset**
  - The original dataset was highly imbalanced toward Positive reviews.
  - The training dataset was balanced using 5,000 samples from each sentiment class.

- 🎯 **Model Accuracy**
  - The Logistic Regression model achieved **87.8% accuracy** on the test dataset.

- 🟢 **Positive Sentiment**
  - The model achieved **83% recall** for Positive reviews.

- 🟡 **Neutral Sentiment**
  - The model achieved **85% precision and 85% recall** for Neutral reviews.

- 🔴 **Negative Sentiment**
  - The model performed strongly on Negative reviews with **91% precision and 95% recall**.

- 🔤 **TF-IDF Effectiveness**
  - TF-IDF with unigram and bigram features effectively captured important words and phrases from product reviews.

- 🚫 **Negation Handling**
  - Reviews containing phrases such as **"not good"** and **"do not recommend"** were correctly classified as Negative.

- 🚀 **Practical Application**
  - The system can help analyze customer feedback and quickly identify overall sentiment from large numbers of product reviews.
# 🗄️ Database

The project uses **SQLite** to store prediction history generated by the sentiment analysis application.

### Database Details

- **Database:** SQLite
- **Database File:** `reviews.db`
- **Database Module:** `database.py`
- **Purpose:** Store and retrieve sentiment prediction history.

### Stored Information

The database stores details such as:

- 📝 Review text
- 🎯 Predicted sentiment
- 📊 Confidence score
- ⏱️ Processing time
- 🔢 Word count
- 📅 Prediction date and time

### Database Operations

The application supports:

- **Insert** — Saves every new sentiment prediction.
- **Retrieve** — Fetches previous predictions for the dashboard/history.
- **Ordering** — Displays recent predictions first.

### Database Security

The generated `reviews.db` file is excluded from GitHub using `.gitignore` because it contains locally generated prediction history.

```text
*.db
```

This keeps the repository clean while allowing the application to automatically create and use the database locally.

# 🚀 How to Run the Project

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/alishamansoori004-sketch/Product-Reviews-Sentiment-Analysis.git
cd Product-Reviews-Sentiment-Analysis
```

## 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

## 3️⃣ Activate the Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 5️⃣ Download NLTK Resources

Run Python:

```bash
python
```

Then execute:

```python
import nltk
nltk.download('stopwords')
```

Exit Python:

```python
exit()
```

## 6️⃣ Train the Machine Learning Model

```bash
python train_model.py
```

This generates the trained model files inside the `model/` directory.

## 7️⃣ Start the Flask Application

```bash
python app.py
```

## 8️⃣ Open the Application

Open your browser and visit:

```text
http://127.0.0.1:5000
```

The application is now ready to analyze product reviews. 🚀
# 📂 Dataset

The project uses a product review dataset containing customer reviews and their corresponding sentiment labels.

### Dataset Information

- **Source:** `dataset/reviews.csv`
- **Type:** CSV
- **Domain:** Product Reviews
- **Target:** Sentiment Classification
- **Classes:**
  - 🟢 Positive
  - 🟡 Neutral
  - 🔴 Negative

### Data Preprocessing

The dataset is processed before training:

1. Remove unnecessary text and formatting.
2. Convert text into a standardized format.
3. Clean the review text.
4. Apply stopword processing.
5. Convert reviews into numerical features using **TF-IDF**.
6. Balance the sentiment classes using resampling.

### Balanced Training Dataset

The final training data contains:

- **5,000 Negative reviews**
- **5,000 Neutral reviews**
- **5,000 Positive reviews**

**Total balanced samples:** 15,000

The balanced dataset helps reduce the effect of class imbalance and improves the model's ability to learn all three sentiment categories.

# 🚀 Future Improvements

The project can be further improved with the following features:

- 🤖 **Advanced Machine Learning Models**
  - Experiment with Random Forest, SVM, XGBoost, and transformer-based models.

- 🧠 **Deep Learning Integration**
  - Implement LSTM, BiLSTM, or BERT-based models for more advanced sentiment analysis.

- 🌐 **Multilingual Sentiment Analysis**
  - Support reviews written in multiple languages.

- 📊 **Advanced Analytics Dashboard**
  - Add interactive charts, filters, sentiment trends, and category-wise analysis.

- 🔍 **Aspect-Based Sentiment Analysis**
  - Identify sentiment related to specific product aspects such as price, quality, delivery, and packaging.

- ☁️ **Cloud Database Integration**
  - Replace local SQLite storage with a cloud database for scalable applications.

- 🔐 **User Authentication**
  - Add secure login and user-specific prediction history.

- 📈 **Model Monitoring**
  - Track model performance and retrain the model when new review data becomes available.

- 🛒 **Real-Time Review Integration**
  - Integrate reviews from e-commerce platforms or other supported data sources.

- 🚀 **Cloud Deployment**
  - Deploy the complete application using platforms such as Render, Railway, or AWS.

- 📱 **Mobile-Friendly Improvements**
  - Further optimize the interface for mobile and tablet devices.

# 👩‍💻 Author

**Alisha Mansoori**

B.Tech — Artificial Intelligence & Data Science

### 🔗 Connect With Me

- 💼 **GitHub:**  
  https://github.com/alishamansoori004-sketch

- 🌐 **Portfolio:**  
  https://aqiqafatima2.wixsite.com/aqiqa-fatima

---

⭐ If you found this project useful, consider giving the repository a **star**!
