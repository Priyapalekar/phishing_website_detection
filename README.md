# 🔒 AI Phishing Website Detector

An AI-powered cybersecurity project that detects whether a website URL is safe or phishing using Machine Learning and cybersecurity-based feature analysis.

Built with:
- Python
- Scikit-learn
- Pandas
- Streamlit

---

# 🚀 Features

✅ Real-time phishing URL detection  
✅ Machine Learning classification model  
✅ Cybersecurity-inspired feature engineering  
✅ Threat analysis dashboard  
✅ Risk level meter  
✅ Interactive Streamlit UI  

---

# 🧠 Cybersecurity Concepts Used

- Phishing Detection
- URL Obfuscation Analysis
- Social Engineering Indicators
- Domain Spoofing Detection
- Suspicious Pattern Recognition
- Threat Scoring

---

# 🤖 Machine Learning Concepts Used

- Classification
- Logistic Regression
- Feature Engineering
- Train-Test Split
- Model Evaluation
- Confusion Matrix
- Real-Time Inference

---

# 📂 Project Structure

```bash
PhishingWebsiteDetection/
│
├── phishing.csv
├── train.py
├── app.py
├── model.pkl
├── requirements.txt
├── README.md
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_LINK
```

Move into project folder:

```bash
cd PhishingWebsiteDetection
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Run The Project

## Step 1 — Train Model

```bash
python train.py
```

This creates:

```bash
model.pkl
```

---

## Step 2 — Start Streamlit App

```bash
streamlit run app.py
```

---

# 🔍 How It Works

The system extracts cybersecurity-related features from URLs such as:

- URL Length
- Number of Dots
- HTTPS Usage
- Hyphen Count
- Suspicious Keywords
- @ Symbol Presence
- Slash Count

The Machine Learning model analyzes these features and predicts whether the website is:
- Safe
- Phishing

---

# 📊 Example Suspicious URLs

```text
https://paypal-login-security.xyz
http://192.168.1.1/login
https://google.verify-account-alert.ru
```

---

# 🛡️ Threat Analysis Features

The application provides:
- Threat level meter
- URL risk indicators
- Feature breakdown analysis
- Real-time scan results

---

# 📈 Future Improvements

- WHOIS domain analysis
- DNS lookup integration
- Browser extension version
- Deep learning-based URL analysis
- Real-time blacklist API integration
- Advanced threat intelligence dashboard

---

# 📦 Libraries Used

- pandas
- scikit-learn
- streamlit
- pickle

---

# 👩‍💻 Author

Priya Vijay Palekar

---

# 📌 Disclaimer

This project is developed for educational and cybersecurity learning purposes only.
