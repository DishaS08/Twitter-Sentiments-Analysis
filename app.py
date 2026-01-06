<<<<<<< HEAD
# import streamlit as st
# import pickle
# import re
# import snscrape.modules.twitter as sntwitter
# from sklearn.feature_extraction.text import TfidfVectorizer
# from nltk.corpus import stopwords
# import nltk

# # Download stopwords once
# @st.cache_resource
# def load_stopwords():
#     nltk.download('stopwords')
#     return stopwords.words('english')

# # Load model and vectorizer
# @st.cache_resource
# def load_model_and_vectorizer():
#     with open('model.pkl', 'rb') as model_file:
#         model = pickle.load(model_file)
#     with open('vectorizer.pkl', 'rb') as vectorizer_file:
#         vectorizer = pickle.load(vectorizer_file)
#     return model, vectorizer

# # Predict sentiment
# def predict_sentiment(text, model, vectorizer, stop_words):
#     text = re.sub('[^a-zA-Z]', ' ', text)
#     text = text.lower()
#     text = text.split()
#     text = [word for word in text if word not in stop_words]
#     text = ' '.join(text)
#     text = [text]
#     text = vectorizer.transform(text)
#     sentiment = model.predict(text)
#     return "Negative" if sentiment == 0 else "Positive"

# # Colored card
# def create_card(tweet_text, sentiment):
#     color = "green" if sentiment == "Positive" else "red"
#     card_html = f"""
#     <div style="background-color: {color}; padding: 10px; border-radius: 5px; margin: 10px 0;">
#         <h5 style="color: white;">{sentiment} Sentiment</h5>
#         <p style="color: white;">{tweet_text}</p>
#     </div>
#     """
#     return card_html

# # Main app
# def main():
#     st.title("Twitter Sentiment Analysis (Live)")

#     stop_words = load_stopwords()
#     model, vectorizer = load_model_and_vectorizer()

#     option = st.selectbox("Choose an option", ["Input text", "Get tweets from user"])

#     if option == "Input text":
#         text_input = st.text_area("Enter text to analyze sentiment")
#         if st.button("Analyze"):
#             if text_input.strip() == "":
#                 st.warning("Please enter some text!")
#             else:
#                 sentiment = predict_sentiment(text_input, model, vectorizer, stop_words)
#                 st.write(f"Sentiment: {sentiment}")

#     elif option == "Get tweets from user":
#         username = st.text_input("Enter Twitter username (without @)")
#         count = st.number_input("Number of tweets to fetch", min_value=1, max_value=50, value=5, step=1)
#         if st.button("Fetch Tweets"):
#             try:
#                 tweets_list = []
#                 for i, tweet in enumerate(sntwitter.TwitterUserScraper(username).get_items()):
#                     if i >= count:
#                         break
#                     tweets_list.append(tweet.content)

#                 if not tweets_list:
#                     st.warning("No tweets found for this user!")
#                 else:
#                     for tweet_text in tweets_list:
#                         sentiment = predict_sentiment(tweet_text, model, vectorizer, stop_words)
#                         card_html = create_card(tweet_text, sentiment)
#                         st.markdown(card_html, unsafe_allow_html=True)
#             except Exception as e:
#                 st.error(f"Error fetching tweets: {e}")

# if __name__ == "__main__":
#     main()





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
=======
# import streamlit as st
# import pickle
# import re
# import snscrape.modules.twitter as sntwitter
# from sklearn.feature_extraction.text import TfidfVectorizer
# from nltk.corpus import stopwords
# import nltk

# # Download stopwords once
# @st.cache_resource
# def load_stopwords():
#     nltk.download('stopwords')
#     return stopwords.words('english')

# # Load model and vectorizer
# @st.cache_resource
# def load_model_and_vectorizer():
#     with open('model.pkl', 'rb') as model_file:
#         model = pickle.load(model_file)
#     with open('vectorizer.pkl', 'rb') as vectorizer_file:
#         vectorizer = pickle.load(vectorizer_file)
#     return model, vectorizer

# # Predict sentiment
# def predict_sentiment(text, model, vectorizer, stop_words):
#     text = re.sub('[^a-zA-Z]', ' ', text)
#     text = text.lower()
#     text = text.split()
#     text = [word for word in text if word not in stop_words]
#     text = ' '.join(text)
#     text = [text]
#     text = vectorizer.transform(text)
#     sentiment = model.predict(text)
#     return "Negative" if sentiment == 0 else "Positive"

# # Colored card
# def create_card(tweet_text, sentiment):
#     color = "green" if sentiment == "Positive" else "red"
#     card_html = f"""
#     <div style="background-color: {color}; padding: 10px; border-radius: 5px; margin: 10px 0;">
#         <h5 style="color: white;">{sentiment} Sentiment</h5>
#         <p style="color: white;">{tweet_text}</p>
#     </div>
#     """
#     return card_html

# # Main app
# def main():
#     st.title("Twitter Sentiment Analysis (Live)")

#     stop_words = load_stopwords()
#     model, vectorizer = load_model_and_vectorizer()

#     option = st.selectbox("Choose an option", ["Input text", "Get tweets from user"])

#     if option == "Input text":
#         text_input = st.text_area("Enter text to analyze sentiment")
#         if st.button("Analyze"):
#             if text_input.strip() == "":
#                 st.warning("Please enter some text!")
#             else:
#                 sentiment = predict_sentiment(text_input, model, vectorizer, stop_words)
#                 st.write(f"Sentiment: {sentiment}")

#     elif option == "Get tweets from user":
#         username = st.text_input("Enter Twitter username (without @)")
#         count = st.number_input("Number of tweets to fetch", min_value=1, max_value=50, value=5, step=1)
#         if st.button("Fetch Tweets"):
#             try:
#                 tweets_list = []
#                 for i, tweet in enumerate(sntwitter.TwitterUserScraper(username).get_items()):
#                     if i >= count:
#                         break
#                     tweets_list.append(tweet.content)

#                 if not tweets_list:
#                     st.warning("No tweets found for this user!")
#                 else:
#                     for tweet_text in tweets_list:
#                         sentiment = predict_sentiment(tweet_text, model, vectorizer, stop_words)
#                         card_html = create_card(tweet_text, sentiment)
#                         st.markdown(card_html, unsafe_allow_html=True)
#             except Exception as e:
#                 st.error(f"Error fetching tweets: {e}")

# if __name__ == "__main__":
#     main()





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
>>>>>>> a3bb7e5 (Initial commit)
