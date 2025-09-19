from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserQuery(BaseModel):
    question: str

@app.post("/ask")
def ask_question(user_query: UserQuery):
    return {"received_question": user_query.question}