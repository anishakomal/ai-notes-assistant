import streamlit as st
import requests

st.title("AI Notes Assistant")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    files = {
        "file": uploaded_file
    }

    response = requests.post(
        "http://127.0.0.1:8000/upload-pdf",
        files=files
    )

    st.success("PDF Uploaded Successfully")


question = st.text_input("Ask Question")

if st.button("Get Answer"):

    data = {
        "question": question
    }

    response = requests.post(
        "http://127.0.0.1:8000/chat",
        json=data
    )

    result = response.json()

    st.write("### Answer")
    st.write(result["answer"])