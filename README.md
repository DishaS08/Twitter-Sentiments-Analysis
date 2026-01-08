# Twitter Sentiment Analysis Tool

**Real-Time Sentiment Analysis of Tweets and Text**

A **Python & Streamlit application** that performs **real-time sentiment analysis**. Users can **type any text** or **fetch live tweets via Tweepy**, and a **pretrained NLP model** (TF-IDF + Logistic Regression) classifies them as **Positive** or **Negative**, displaying results in **interactive, color-coded cards**.

---

## 🚀 Features

* Analyze **typed text** or **live tweets**
* Real-time **positive/negative sentiment classification**
* Interactive **colored result cards** for easy visualization
* Simple and user-friendly **Streamlit interface**

---

## 🖼️ Demo / Screenshots

<img width="1911" height="968" alt="image" src="https://github.com/user-attachments/assets/1f55d403-a63c-48fc-a7db-fec40d11f0b8" />

<img width="1914" height="952" alt="image" src="https://github.com/user-attachments/assets/ae5bb4c0-5dde-4c51-90c4-3cc19d868521" />

<img width="1916" height="969" alt="image" src="https://github.com/user-attachments/assets/eacf84dc-7e11-4784-be88-175240ee0a2d" />

---

## ⚙️ Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/Twitter-Sentiments-Analysis.git
cd Twitter-Sentiments-Analysis
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the Streamlit app**

```bash
streamlit run app.py
```

---

## 📝 Usage

1. Open the app in your browser.
2. Choose to **type your text** or **fetch live tweets**.
3. View the **sentiment results** in interactive colored cards (Green = Positive, Red = Negative).

---

## 📚 How it Works

* **TF-IDF (Term Frequency-Inverse Document Frequency)**: Converts text into numerical vectors that highlight important words.
* **Logistic Regression**: Uses the TF-IDF features to classify sentiment as Positive or Negative.
* **Streamlit**: Provides the interactive web interface.

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Tweepy (for fetching tweets)
* Scikit-learn (TF-IDF + Logistic Regression)
* Pandas & NumPy

---

## 📂 Dataset

* The app fetches **live tweets** via the Twitter API.
* For offline testing, a sample dataset can be included (link to Kaggle if needed).

---

## 💡 Notes

* Ensure your Twitter API keys are configured in the app to fetch tweets.
* For large CSV datasets, consider hosting externally (Kaggle, Google Drive) to avoid GitHub file size limits.

---

## 🔗 Links

* [GitHub Repository](https://github.com/DishaS08/Twitter-Sentiments-Analysis)
* [Dataset Link](https://www.kaggle.com/datasets/kazanova/sentiment140)

---

If you want, I can also make an **even sleeker GitHub-ready version with badges, nice spacing, and a portfolio feel** — it will look very professional at a glance.

Do you want me to do that?



