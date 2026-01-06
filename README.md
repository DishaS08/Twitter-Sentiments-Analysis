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

![Home Screen 1](https://github.com/user-attachments/assets/3e518dd3-22b3-4f77-9f2e-392c1f466048)

![Sentiment Results 1](https://github.com/user-attachments/assets/33b35315-f014-44ce-a6a7-27b940770156)

![Home Screen 2](https://github.com/user-attachments/assets/d0478dda-d315-475b-b1af-1795b567fbe9)

![Sentiment Results 2](https://github.com/user-attachments/assets/a29e3c42-e0f8-432d-a5b2-337e5041d912)



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



