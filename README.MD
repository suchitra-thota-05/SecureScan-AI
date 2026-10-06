🛡️ SecureScan AI

## 📌 Project Overview
The AI-Powered Scam and Phishing Detection System is a Machine Learning-based application that helps identify phishing messages, scam emails, suspicious SMS content, and potentially harmful URLs. The system uses Natural Language Processing (NLP) techniques and a Logistic Regression model to classify text as either **Safe** or **Phishing**.

## 🎯 Objectives
- Detect phishing and scam messages.
- Analyze suspicious URLs.
- Scan uploaded text files for phishing content.
- Provide prediction confidence scores.
- Display detection statistics and history.

## 🚀 Features
- 📩 Message Detection
- 🔗 URL Detection
- 📄 File Scanner
- 📊 Statistics Dashboard
- 📈 Confidence Score
- 📝 Prediction History
- ℹ️ About Page
- ❓ Help Page

## 🛠️ Technologies Used
- Python 3.12
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Matplotlib
- Joblib

## 🤖 Machine Learning Algorithm
- TF-IDF Vectorization
- Logistic Regression

## 📂 Project Structure
AI_Phishing_Detection/

├── app.py

├── train_model.py

├── phishing_dataset.csv

├── model.pkl

├── vectorizer.pkl

├── requirements.txt

└── README.md

## ⚙️ Installation

1. Install dependencies:

pip install -r requirements.txt

2. Train the model:

python train_model.py

3. Run the application:

python -m streamlit run app.py

## 📋 Usage
1. Open the application in your browser.
2. Enter a message and click **Analyze Message**.
3. Paste a URL and click **Check URL**.
4. Upload a text file for scanning.
5. View the prediction result and confidence score.

## 🏗️ System Architecture

User Input

↓

Text Preprocessing

↓

TF-IDF Vectorizer

↓

Logistic Regression Model

↓

Prediction Engine

↓

Result Display

## 🔮 Future Enhancements
- Real-time email scanning
- Browser extension for phishing detection
- Mobile application support
- Deep Learning models
- Multi-language phishing detection
- Cloud deployment

## 📚 Conclusion
This project demonstrates the use of Machine Learning and Natural Language Processing to detect phishing attempts and scam messages. It provides a simple and user-friendly interface for users to identify potentially malicious content.

## 👩‍💻 Developed By
Suchitra

B.Tech (AI & ML)