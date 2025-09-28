from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
import routers
from services.ollama_service import to_sql

generate_query_router = APIRouter()
 
class UserQuery(BaseModel):
    question: str

@generate_query_router.get("/generate-query")
def ask_question(user_query: UserQuery):
    schema = {
  "table": "SalesInvoice",
  "columns": [
    { "name": "InvoiceId", "type": "int" },
    { "name": "InvoiceDate", "type": "datetime" },
    { "name": "CustomerId", "type": "int" },
    { "name": "Amount", "type": "decimal" },
    { "name": "Status", "type": "varchar(20)" }
  ]
}
    return to_sql(user_query.question)