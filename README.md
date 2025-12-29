# Spam Message Detector

Spam Message Detector is a machine learning web application that classifies text messages as Spam or Not Spam using Natural Language Processing (NLP).

The model is trained on the SMS Spam Collection dataset and uses TF-IDF vectorization to convert text into numerical features, followed by a Multinomial Naive Bayes classifier. The trained model is deployed as an interactive web app using Streamlit, allowing users to enter custom messages and receive instant predictions.

The system accurately identifies common spam patterns such as promotional language (e.g., “Congratulations”, “win”, “free”, “click link”). Like most real-world ML models, it may occasionally misclassify messages with unusual spelling, formatting, or unseen word patterns, which reflects realistic limitations of data-driven models.

This project demonstrates the end-to-end machine learning workflow, including data preprocessing, model training, evaluation, model persistence, and cloud deployment
