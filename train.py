import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# LOAD DATASET
df = pd.read_csv("phishing.csv")


# ==========================================
# CREATE CUSTOM FEATURES
# ==========================================

# URL Length
df['URL_Length'] = df['url'].apply(len)

# Number of dots
df['Num_Dots'] = df['url'].apply(lambda x: x.count('.'))

# HTTPS presence
df['HTTPS'] = df['url'].apply(
    lambda x: 1 if "https" in x else 0
)

# Number of hyphens
df['Num_Hyphens'] = df['url'].apply(
    lambda x: x.count('-')
)

# Contains @
df['Contains_At'] = df['url'].apply(
    lambda x: 1 if '@' in x else 0
)

# Number of slashes
df['Num_Slashes'] = df['url'].apply(
    lambda x: x.count('/')
)

# Suspicious words
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

df['Suspicious_Words'] = df['url'].apply(
    lambda x: sum(word in x.lower() for word in suspicious_words)
)


# ==========================================
# FEATURES + TARGET
# ==========================================

X = df[
    [
        'URL_Length',
        'Num_Dots',
        'HTTPS',
        'Num_Hyphens',
        'Contains_At',
        'Num_Slashes',
        'Suspicious_Words'
    ]
]

y = df['Result']


# ==========================================
# TRAIN TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# ==========================================
# TRAIN MODEL
# ==========================================

model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)


# ==========================================
# EVALUATION
# ==========================================

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)


# ==========================================
# SAVE MODEL
# ==========================================

with open("model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model saved successfully!")
