# ==========================================
# PHISHING WEBSITE DETECTION - TRAINING FILE
# ==========================================

# STEP 1 — IMPORT LIBRARIES

import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix


# ==========================================
# STEP 2 — LOAD DATASET
# ==========================================

df = pd.read_csv(r"C:\Users\usee\Downloads\phishing_features.csv")
# PHISHING WEBSITE DETECTION - TRAINING FILE
# ==========================================

# STEP 1 — IMPORT LIBRARIES

import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix


# ==========================================
# STEP 2 — LOAD DATASET
# ==========================================

df = pd.read_csv("phishing_urls.csv")


# ==========================================
# STEP 3 — DATA CLEANING
# ==========================================

# Remove rows where tld is missing
df = df.dropna()


# ==========================================
# STEP 4 — DEFINE FEATURES AND TARGET
# ==========================================

# Remove non-numerical columns
X = df.drop(["url", "tld", "label"], axis=1)

# Target column
y = df["label"]


# ==========================================
# STEP 5 — TRAIN TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# ==========================================
# STEP 6 — CREATE MODEL
# ==========================================

model = LogisticRegression(max_iter=2000)


# ==========================================
# STEP 7 — TRAIN MODEL
# ==========================================

model.fit(X_train, y_train)


# ==========================================
# STEP 8 — MAKE PREDICTIONS
# ==========================================

y_pred = model.predict(X_test)


# ==========================================
# STEP 9 — EVALUATE MODEL
# ==========================================

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", accuracy)

print("\nConfusion Matrix:\n")

print(confusion_matrix(y_test, y_pred))


# ==========================================
# STEP 10 — SAVE MODEL
# ==========================================

with open("model.pkl", "wb") as file:

    pickle.dump(model, file)

print("\nModel Saved Successfully!").csv")


# ==========================================
# STEP 3 — DATA CLEANING
# ==========================================

# Remove rows where tld is missing
df = df.dropna()


# ==========================================
# STEP 4 — DEFINE FEATURES AND TARGET
# ==========================================

# Remove non-numerical columns
X = df.drop(["url", "tld", "label"], axis=1)

# Target column
y = df["label"]


# ==========================================
# STEP 5 — TRAIN TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# ==========================================
# STEP 6 — CREATE MODEL
# ==========================================

model = LogisticRegression(max_iter=2000)


# ==========================================
# STEP 7 — TRAIN MODEL
# ==========================================

model.fit(X_train, y_train)


# ==========================================
# STEP 8 — MAKE PREDICTIONS
# ==========================================

y_pred = model.predict(X_test)


# ==========================================
# STEP 9 — EVALUATE MODEL
# ==========================================

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", accuracy)

print("\nConfusion Matrix:\n")

print(confusion_matrix(y_test, y_pred))


# ==========================================
# STEP 10 — SAVE MODEL
# ==========================================

with open("model.pkl", "wb") as file:

    pickle.dump(model, file)

print("\nModel Saved Successfully!")
