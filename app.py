import streamlit as st
import pickle

model = pickle.load(open("spam_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

st.title("Spam Message Detector")

message = st.text_area("Enter a message:")

if st.button("Predict"):
    if message.strip() == "":
        st.warning("Please enter a message")
    else:
        data = vectorizer.transform([message])
        prediction = model.predict(data)[0]

        if prediction == 1:
            st.error("🚨 Spam Message")
        else:
            st.success("✅ Not Spam")
