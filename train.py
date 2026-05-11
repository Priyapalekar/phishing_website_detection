import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# STEP 2 — LOAD DATASET


df = pd.read_csv(r"C:\Users\usee\Documents\PhishingWebsiteDetection\phising_pred.csv")


# STEP 3 — DATA EXPLORATION


print(df.head())

print(df.info())

print(df.isnull().sum())



# STEP 4 — DEFINE FEATURES AND TARGET

# X = input features
X = df.drop("Result", axis=1)

# y = output/label
y = df["Result"]

# STEP 5 — TRAIN TEST SPLIT

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# STEP 6 — CREATE MODEL

model = LogisticRegression(max_iter=1000)


# STEP 7 — TRAIN MODEL

model.fit(X_train, y_train)

# STEP 8 — MAKE PREDICTION

y_pred = model.predict(X_test)


# STEP 9 — EVALUATE MODEL

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", accuracy)

# STEP 10 — CONFUSION MATRIX

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:\n")

print(cm)

# STEP 11 — SAVE MODEL

with open("model.pkl", "wb") as file:

    pickle.dump(model, file)

print("\nModel Saved Successfully!")
