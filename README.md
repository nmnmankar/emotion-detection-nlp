# Emotion Detection using NLP

## 📌 Project Overview

This project detects **human emotions from text** using Natural Language Processing (NLP) and Machine Learning.
The model analyzes user input and predicts emotions such as **joy, sadness, anger, fear, love, and surprise**.

The project also includes a **Streamlit web application** where users can enter text and get emotion predictions instantly.

Model Accuracy: 88% ,
Algorithm: Logistic Regression ,
Vectorizer: TF-IDF

---

## 🚀 Technologies Used

* Python
* Natural Language Processing (NLP)
* TF-IDF Vectorization
* Logistic Regression
* NLTK
* Scikit-learn
* Streamlit

---

## 📂 Project Structure

emotion-detection-nlp
│
├── app.py → Streamlit web application
├── model_training.py → Model training script
├── emotion_model.pkl → Trained ML model
├── tfidf_vectorizer.pkl → TF-IDF vectorizer
├── emotion_dict.pkl → Emotion label mapping
├── train.txt → Dataset
└── README.md → Project documentation

---


## ⚙️ Features

* Text preprocessing (lowercase, punctuation removal, stopword removal)
* TF-IDF feature extraction
* Emotion classification using Logistic Regression
* Interactive Streamlit web interface
* Real-time emotion prediction

---

## 🧠 Model Workflow

1. Text preprocessing using NLTK
2. Tokenization and stopword removal
3. Feature extraction using TF-IDF
4. Model training using Logistic Regression
5. Emotion prediction through Streamlit app

---

## ▶️ How to Run the Project

### 1️⃣ Install dependencies

pip install streamlit nltk scikit-learn pandas numpy

### 2️⃣ Run the Streamlit app

streamlit run app.py

### 3️⃣ Enter text in the app and predict emotion

---

## 💡 Example

Input:
`I am very happy today`

Output:
`Predicted Emotion: Joy`

---

## 📊 Dataset

The dataset contains text sentences labeled with emotions such as:

* Joy
* Sadness
* Anger
* Fear
* Love
* Surprise

---

## 👨‍💻 Author

**Naman Mankar**

B.Tech – Artificial Intelligence
Interested in **AI, Machine Learning, and Data Science projects**

---

## 🔗 Future Improvements

* Use Deep Learning (LSTM / BERT)
* Add emotion probability visualization
* Deploy the app online
