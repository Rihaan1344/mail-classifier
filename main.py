# temporary streamlit interface

import streamlit as st

from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os
import pickle

st.title("Mail Classifier (Prototype)")
st.write("This is a work-in-progress demo. The model is not trained yet.")

st.subheader("Project Status")
st.progress(30)
st.write("• UI built ✔")
st.write("• Dataset collection ❌")
st.write("• Model training ❌")

st.subheader("Next Steps")
st.write("1. Collect labeled emails")
st.write("2. Train Naive Bayes / SVM model")
st.write("3. Improve accuracy + deploy final version")

scope = ["https://www.googleapis.com/auth/gmail.modify"]

login = st.button("Log in to allow my app to access your mail.")

if login:
    creds = None

    if not creds:
        flow = InstalledAppFlow.from_client_secrets_file(
            "credentials.json",
            scope
        )

        creds = flow.run_local_server(port=0)

        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)
    st.write("Logged in!")