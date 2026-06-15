from fastapi import APIRouter, UploadFile
import os
import uuid

from app.services.pdf_service import save_pdf
from app.services.vector_db import collection

router = APIRouter()


UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/upload-pdf")
async def upload_pdf(file: UploadFile):

    file_id = str(uuid.uuid4())

    file_path = f"{UPLOAD_FOLDER}/{file_id}.pdf"

    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)

    text = save_pdf(file)

    collection.add(
        documents=[text],
        ids=[file_id]
    )

    return {
        "message": "PDF uploaded successfully"
    }