import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from app.services.vector_db import collection

load_dotenv()


llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_response(question: str):

    results = collection.query(
        query_texts=[question],
        n_results=3
    )

    print(results)

    documents = results.get("documents")

    print(documents)

    if not documents or not documents[0]:
        return "No relevant document found."

    best_note = documents[0][0][:1000]

    prompt = f"""
    You are an AI Notes Assistant.

    Answer the user's question ONLY using the provided context.

    If the answer is not present in the context, say:
    "I could not find this information in the uploaded notes."

    Context:
    {best_note}

    Question:
    {question}

    Answer:
    """

    response = llm.invoke(prompt)

    return response.content