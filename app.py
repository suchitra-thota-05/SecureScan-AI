import streamlit as st
import joblib
import pandas as pd
import matplotlib.pyplot as plt

# Load Model
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Page Config
st.set_page_config(
    page_title="🛡️ ScamShield AI",
    page_icon="🛡️",
    layout="wide"
)

# Session State
if "history" not in st.session_state:
    st.session_state.history = []

# Header
st.title("🛡️ ScamShield AI")
st.subheader("AI-Powered Scam & Phishing Detection System")

# Tabs
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "🏠 Home",
    "📩 Message Detection",
    "📧 Email Detection",
    "🔗 URL Detection",
    "📄 File Scanner",
    "📊 Statistics",
    "❓ Help"
])

# ================= HOME =================
with tab1:

    st.markdown("""
    ## Welcome to ScamShield AI 🚀

    Protect yourself from:

    ✅ Scam Messages  
    ✅ Phishing Emails  
    ✅ Fraudulent URLs  
    ✅ Suspicious Files  

    
    Select a tab above to start.
    """)

# ================= MESSAGE DETECTION =================
with tab2:

    st.header("📩 Message Detection")

    message = st.text_area(
        "Enter Message",
        height=150,
        key="message"
    )

    if st.button("🚀 Analyze Message"):

        if message.strip():

            text = vectorizer.transform([message])

            prediction = model.predict(text)[0]

            confidence = max(
                model.predict_proba(text)[0]
            ) * 100

            category = "General"

            msg = message.lower()

            if "bank" in msg or "account" in msg:
                category = "🏦 Banking Scam"

            elif "winner" in msg or "lottery" in msg:
                category = "🎁 Lottery Scam"

            elif "delivery" in msg or "parcel" in msg:
                category = "📦 Delivery Scam"

            elif "investment" in msg:
                category = "💰 Investment Scam"

            st.info(f"🎯 Threat Category: {category}")

            if str(prediction).lower() == "phishing":
                st.error("⚠️ Phishing / Scam Message Detected")
            else:
                st.success("✅ Safe Message")

            st.info(
                f"📈 Confidence Score: {confidence:.2f}%"
            )

            st.subheader("🚦 Risk Meter")
            st.progress(int(confidence))

            st.session_state.history.append(
                str(prediction).lower()
            )

# ================= EMAIL DETECTION =================
with tab3:

    st.header("📧 Email Detection")

    email_text = st.text_area(
        "Paste Email Content",
        height=250,
        key="email"
    )

    if st.button("📩 Analyze Email"):

        if email_text.strip():

            text = vectorizer.transform(
                [email_text]
            )

            prediction = model.predict(text)[0]

            confidence = max(
                model.predict_proba(text)[0]
            ) * 100

            if str(prediction).lower() == "phishing":
                st.error("🚨 Phishing Email Detected")
            else:
                st.success("✅ Safe Email")

            st.info(
                f"📈 Confidence Score: {confidence:.2f}%"
            )

            st.session_state.history.append(
                str(prediction).lower()
            )

# ================= URL DETECTION =================
with tab4:

    st.header("🔗 URL Detection")

    url = st.text_input(
        "Enter Website URL"
    )

    if st.button("🔍 Check URL"):

        suspicious_words = [
            "login",
            "verify",
            "secure",
            "update",
            "account",
            "bank",
            "winner",
            "free",
            "gift"
        ]

        score = 0

        if "@" in url:
            score += 1

        if "-" in url:
            score += 1

        if len(url) > 50:
            score += 1

        for word in suspicious_words:
            if word in url.lower():
                score += 1

        if score >= 2:
            st.error(
                "⚠️ Suspicious / Possible Phishing URL"
            )
        else:
            st.success(
                "✅ URL Appears Safe"
            )

# ================= FILE SCANNER =================
with tab5:

    st.header("📄 File Scanner")

    uploaded_file = st.file_uploader(
        "Upload TXT File",
        type=["txt"]
    )

    if uploaded_file is not None:

        content = uploaded_file.read().decode(
            "utf-8"
        )

        st.text_area(
            "📃 File Content",
            content,
            height=200
        )

        text = vectorizer.transform([content])

        prediction = model.predict(text)[0]

        confidence = max(
            model.predict_proba(text)[0]
        ) * 100

        if str(prediction).lower() == "phishing":
            st.error("⚠️ Phishing Content Detected")
        else:
            st.success("✅ Safe Content")

        st.info(
            f"📈 Confidence Score: {confidence:.2f}%"
        )

# ================= STATISTICS =================
with tab6:

    st.header("📊 Statistics Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Scans",
        len(st.session_state.history)
    )

    col2.metric(
        "Phishing",
        st.session_state.history.count("phishing")
    )

    col3.metric(
        "Safe",
        st.session_state.history.count("safe")
    )

    if st.session_state.history:

        df = pd.DataFrame(
            st.session_state.history,
            columns=["Prediction"]
        )

        st.dataframe(df)

        csv = df.to_csv(index=False)

        st.download_button(
            "📥 Download Report",
            csv,
            "scam_report.csv",
            "text/csv"
        )

        phishing_count = st.session_state.history.count(
            "phishing"
        )

        safe_count = st.session_state.history.count(
            "safe"
        )

        fig, ax = plt.subplots()

        ax.pie(
            [phishing_count, safe_count],
            labels=["Phishing", "Safe"],
            autopct="%1.1f%%"
        )

        st.pyplot(fig)



# ================= HELP =================
with tab7:

    st.header("❓ Help")

    st.write("""
### How To Use

1️⃣ Open any detection tab

2️⃣ Enter a message, email, URL, or upload a TXT file

3️⃣ Click Analyze

4️⃣ View prediction and confidence score

5️⃣ Check statistics and download reports

### Note

This project is for educational purposes.
""")

st.markdown("---")
st.caption(
    "🛡️ ScamShield AI | Developed using Python, Streamlit & Machine Learning"
)