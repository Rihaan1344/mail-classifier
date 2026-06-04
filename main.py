# temporary streamlit interface

import streamlit as st

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

