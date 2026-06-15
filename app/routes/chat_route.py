from fastapi import APIRouter

from app.schemas.chat_schema import ChatRequest
from app.services.chat_service import generate_response

router = APIRouter()


@router.post("/chat")
def chat(data: ChatRequest):

    answer = generate_response(data.question)

    return {
        "question": data.question,
        "answer": answer
    }