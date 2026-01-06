import streamlit as st
import tweepy
import pickle
import re
from nltk.corpus import stopwords
import nltk
from dotenv import load_dotenv
import os

# -------------------- Setup --------------------
nltk.download('stopwords')
stop_words = stopwords.words('english')

# Load environment variables
load_dotenv()
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

# Load ML model and vectorizer
@st.cache_resource
def load_model_and_vectorizer():
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)
    return model, vectorizer

model, vectorizer = load_model_and_vectorizer()

# -------------------- Sentiment Function --------------------
def predict_sentiment(text):
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = text.lower().split()
    text = [w for w in text if w not in stop_words]
    text = ' '.join(text)
    text_vect = vectorizer.transform([text])
    pred = model.predict(text_vect)[0]
    return "Negative" if pred == 0 else "Positive"

# -------------------- Twitter API --------------------
client = tweepy.Client(bearer_token=BEARER_TOKEN)

def fetch_tweets(username, max_tweets=5):
    tweets = []
    try:
        user = client.get_user(username=username)
        if not user.data:
            st.error("Invalid username or user not found")
            return []
        user_id = user.data.id
        resp = client.get_users_tweets(id=user_id, max_results=max_tweets)
        if resp.data:
            for t in resp.data:
                tweets.append(t.text)
    except Exception as e:
        st.error(f"Error fetching tweets: {e}")
    return tweets

# -------------------- UI Card --------------------
def create_card(tweet_text, sentiment):
    color = "#28a745" if sentiment == "Positive" else "#dc3545"
    card_html = f"""
    <div style="background-color: {color}; padding: 10px; border-radius: 5px; margin: 10px 0;">
        <h5 style="color: white;">{sentiment} Sentiment</h5>
        <p style="color: white;">{tweet_text}</p>
    </div>
    """
    return card_html

# -------------------- Streamlit App --------------------
st.title("Twitter Sentiment Analysis")

option = st.selectbox("Choose an option", ["Input text", "Get tweets from user"])

if option == "Input text":
    text_input = st.text_area("Enter text to analyze sentiment")
    if st.button("Analyze"):
        if text_input.strip() == "":
            st.warning("Please enter some text")
        else:
            sentiment = predict_sentiment(text_input)
            st.markdown(create_card(text_input, sentiment), unsafe_allow_html=True)

elif option == "Get tweets from user":
    username = st.text_input("Enter Twitter username")
    if st.button("Fetch Tweets"):
        if username.strip() == "":
            st.warning("Please enter a username")
        else:
            tweets = fetch_tweets(username, max_tweets=5)
            if tweets:
                for t in tweets:
                    sentiment = predict_sentiment(t)
                    st.markdown(create_card(t, sentiment), unsafe_allow_html=True)
            else:
                st.info("No tweets found for this user.")
