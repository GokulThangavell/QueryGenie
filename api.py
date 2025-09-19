from fastapi import FastAPI
from pydantic import BaseModel
from Converter.to_mssql import mssql_helper
from API.schema_api import router as schema_router
 
app = FastAPI()

app.include_router(schema_router, prefix="/schema", tags=["Schema"])

SCHEMA= """
Table:  SalesInvoice,
Table:  SalesOrder
"""

class UserQuery(BaseModel):
    question: str

@app.post("/ask")
def ask_question(user_query: UserQuery):
    mssql = mssql_helper()
    sqlQuery = mssql.to_sql(user_query.question)
    return {"received_question": user_query.question, "query":sqlQuery}