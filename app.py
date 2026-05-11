# ==========================================
# PHISHING WEBSITE DETECTOR - STREAMLIT APP
# ==========================================

# STEP 1 — IMPORT LIBRARIES

import streamlit as st
import pandas as pd
import pickle


# ==========================================
# STEP 2 — LOAD TRAINED MODEL
# ==========================================

with open("model.pkl", "rb") as file:
    model = pickle.load(file)


# ==========================================
# STEP 3 — PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Phishing Website Detector",
    page_icon="🔒",
    layout="centered"
)


# ==========================================
# STEP 4 — CUSTOM CYBERSECURITY UI
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
# STEP 6 — FEATURE EXTRACTION FUNCTION
# ==========================================

def extract_features(url):

    features = {}

    # URL Length
    features['URL_Length'] = len(url)

    # Number of dots
    features['Num_Dots'] = url.count('.')

    # HTTPS presence
    features['HTTPS'] = 1 if "https" in url else 0

    # Number of hyphens
    features['Num_Hyphens'] = url.count('-')

    # Contains @ symbol
    features['Contains_At'] = 1 if '@' in url else 0

    # Number of slashes
    features['Num_Slashes'] = url.count('/')

    # Contains suspicious words
    suspicious_words = [
        "login",
        "verify",
        "secure",
        "account",
        "update",
        "bank",
        "free",
        "bonus"
    ]

    features['Suspicious_Words'] = sum(
        word in url.lower() for word in suspicious_words
    )

    return features


# ==========================================
# STEP 7 — USER INPUT
# ==========================================

url = st.text_input(
    "Enter Website URL",
    placeholder="https://example.com"
)


# ==========================================
# STEP 8 — SCAN BUTTON
# ==========================================

if st.button("🚨 Scan URL"):

    if url == "":

        st.warning("Please enter a URL.")

    else:

        # Extract Features
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
        # THREAT ANALYSIS PANEL
        # ==========================================

        st.markdown("## 🔍 Threat Analysis")

        st.markdown(
            f"""
            <div class="feature-box">

            <b>URL Length:</b> {features['URL_Length']} <br><br>

            <b>Number of Dots:</b> {features['Num_Dots']} <br><br>

            <b>HTTPS Enabled:</b> {features['HTTPS']} <br><br>

            <b>Hyphen Count:</b> {features['Num_Hyphens']} <br><br>

            <b>Contains @ Symbol:</b> {features['Contains_At']} <br><br>

            <b>Slash Count:</b> {features['Num_Slashes']} <br><br>

            <b>Suspicious Keywords:</b> {features['Suspicious_Words']}

            </div>
            """,
            unsafe_allow_html=True
        )

        # ==========================================
        # THREAT LEVEL METER
        # ==========================================

        risk_score = (
            features['Num_Hyphens']
            + features['Contains_At']
            + features['Suspicious_Words']
            + features['Num_Dots']
        )

        st.markdown("## 📊 Threat Level")

        st.progress(min(risk_score / 10, 1.0))

        if risk_score <= 2:
            st.success("Low Risk")

        elif risk_score <= 5:
            st.warning("Medium Risk")

        else:
            st.error("High Risk")
