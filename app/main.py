from fastapi import FastAPI
from app.routes.chat_route import router as chat_router
# from app.routes.notes_route import router as notes_router
from app.routes.upload_route import router as upload_router

app = FastAPI()
   

@app.get("/")
def home():
    return {"message": "AI Notes Assistant"}

app.include_router(chat_router)
# app.include_router(notes_router)
app.include_router(upload_router)



