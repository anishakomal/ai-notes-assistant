from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.services.vector_db import collection


def save_pdf(file):

    pdf = PdfReader(file.file)

    text = ""

    for page in pdf.pages:
        text += page.extract_text()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_text(text)

    for i, chunk in enumerate(chunks):

        collection.add(
            documents=[chunk],
            ids=[f"chunk_{i}"]
        )