# ==========================================
# PHISHING WEBSITE DETECTOR - STREAMLIT APP
# ==========================================

# STEP 1 — IMPORT LIBRARIES

import streamlit as st
import pandas as pd
import pickle
import re
import math
from collections import Counter
from urllib.parse import urlparse


# ==========================================
# STEP 2 — LOAD MODEL
# ==========================================

with open("model.pkl", "rb") as file:
    model = pickle.load(file)


# ==========================================
# STEP 3 — PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="AI Phishing Detector",
    page_icon="🔒",
    layout="centered"
)


# ==========================================
# STEP 4 — CUSTOM UI
# ==========================================

st.markdown("""
<style>

body {
    background-color: #0f1117;
}

.main {
    background-color: #0f1117;
    color: white;
}

h1 {
    color: #00ffcc;
    text-align: center;
}

.stButton>button {
    width: 100%;
    background-color: #00ffcc;
    color: black;
    font-weight: bold;
    border-radius: 10px;
    height: 50px;
    border: none;
}

.stTextInput>div>div>input {
    background-color: #1c1f26;
    color: white;
    border-radius: 10px;
}

.result-box {
    padding: 20px;
    border-radius: 12px;
    font-size: 22px;
    text-align: center;
    font-weight: bold;
}

.safe {
    background-color: #003b2f;
    color: #00ff99;
}

.phishing {
    background-color: #3b0000;
    color: #ff4d4d;
}

.feature-box {
    background-color: #1c1f26;
    padding: 15px;
    border-radius: 10px;
    margin-top: 15px;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# STEP 5 — TITLE
# ==========================================

st.title("🔒 AI Phishing Website Detector")

st.write(
    "Analyze suspicious URLs using Machine Learning and cybersecurity indicators."
)

st.divider()


# ==========================================
# STEP 6 — ENTROPY FUNCTION
# ==========================================

def calculate_entropy(text):

    counter = Counter(text)

    length = len(text)

    entropy = 0

    for count in counter.values():

        probability = count / length

        entropy -= probability * math.log2(probability)

    return entropy


# ==========================================
# STEP 7 — FEATURE EXTRACTION
# ==========================================

def extract_features(url):

    parsed_url = urlparse(url)

    suspicious_keywords = [
        "login",
        "verify",
        "secure",
        "account",
        "update",
        "bank",
        "free",
        "bonus",
        "signin",
        "password"
    ]

    features = {

        # URL Length
        "url_length": len(url),

        # Number of dots
        "num_dots": url.count("."),

        # HTTPS presence
        "has_https": 1 if "https" in url else 0,

        # IP Address detection
        "has_ip": 1 if re.search(r"\d+\.\d+\.\d+\.\d+", url) else 0,

        # Number of subdirectories
        "num_subdirs": url.count("/"),

        # Number of parameters
        "num_params": url.count("?"),

        # Suspicious keyword count
        "suspicious_words": sum(
            word in url.lower()
            for word in suspicious_keywords
        ),

        # Special character count
        "special_char_count": len(
            re.findall(r"[^a-zA-Z0-9]", url)
        ),

        # Digit count
        "digits_count": sum(c.isdigit() for c in url),

        # Entropy
        "entropy": calculate_entropy(url)
    }

    return features


# ==========================================
# STEP 8 — USER INPUT
# ==========================================

url = st.text_input(
    "Enter Website URL",
    placeholder="https://example.com"
)


# ==========================================
# STEP 9 — SCAN BUTTON
# ==========================================

if st.button("🚨 Scan URL"):

    if url == "":

        st.warning("Please enter a URL.")

    else:

        # Extract features
        features = extract_features(url)

        # Convert into DataFrame
        input_data = pd.DataFrame([features])

        # Prediction
        prediction = model.predict(input_data)[0]

        st.divider()

        # ==========================================
        # RESULT DISPLAY
        # ==========================================

        if prediction == 1:

            st.markdown(
                """
                <div class="result-box safe">
                ✅ SAFE WEBSITE DETECTED
                </div>
                """,
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                """
                <div class="result-box phishing">
                ⚠️ PHISHING WEBSITE DETECTED
                </div>
                """,
                unsafe_allow_html=True
            )

        # ==========================================
        # THREAT ANALYSIS
        # ==========================================

        st.markdown("## 🔍 Threat Analysis")

        st.markdown(
            f"""
            <div class="feature-box">

            <b>URL Length:</b> {features['url_length']} <br><br>

            <b>Number of Dots:</b> {features['num_dots']} <br><br>

            <b>HTTPS Enabled:</b> {features['has_https']} <br><br>

            <b>IP Address Detected:</b> {features['has_ip']} <br><br>

            <b>Subdirectories:</b> {features['num_subdirs']} <br><br>

            <b>Parameters:</b> {features['num_params']} <br><br>

            <b>Suspicious Keywords:</b> {features['suspicious_words']} <br><br>

            <b>Special Characters:</b> {features['special_char_count']} <br><br>

            <b>Digits Count:</b> {features['digits_count']} <br><br>

            <b>Entropy:</b> {features['entropy']:.2f}

            </div>
            """,
            unsafe_allow_html=True
        )

        # ==========================================
        # THREAT LEVEL
        # ==========================================

        risk_score = (
            features['num_dots']
            + features['has_ip']
            + features['suspicious_words']
            + features['special_char_count'] / 10
        )

        st.markdown("## 📊 Threat Level")

        st.progress(min(risk_score / 10, 1.0))

        if risk_score <= 2:

            st.success("Low Risk")

        elif risk_score <= 5:

            st.warning("Medium Risk")

        else:

            st.error("High Risk")
