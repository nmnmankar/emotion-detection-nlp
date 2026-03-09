import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')

stop_words = set(stopwords.words('english'))

# Load saved files
model = pickle.load(open("emotion_model.pkl","rb"))
vectorizer = pickle.load(open("tfidf_vectorizer.pkl","rb"))
emotion_dict = pickle.load(open("emotion_dict.pkl","rb"))

# Reverse dictionary
num_to_emotion = {v:k for k,v in emotion_dict.items()}

# Text cleaning function
def clean_text(text):

    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = ''.join([i for i in text if not i.isdigit()])
    text = ''.join([i for i in text if i.isascii()])

    words = word_tokenize(text)
    words = [i for i in words if i not in stop_words]

    return " ".join(words)

st.title("Emotion Detection App")

user_input = st.text_input("Enter text")

if st.button("Predict Emotion"):

    cleaned_text = clean_text(user_input)

    text_vector = vectorizer.transform([cleaned_text])

    prediction = model.predict(text_vector)[0]

    emotion = num_to_emotion[prediction]

    st.success(f"Predicted Emotion: {emotion}")