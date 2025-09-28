import ollama
from model import schema_model
from services.qdrant_service import get_all_schemas


def to_sql(question:str) -> str:
    schema = get_all_schemas()
    prompt =f"""
    You are an expert in MSSQL
    User question: "{question}"
    Database schema: "{schema}"
    Write an MSSQL query  (T-SQL) that answers the question.
    Do not add explanations, only return the sql query.
    """
    response = ollama.chat(model="mistral", messages=[{"role":"user", "content":prompt}])
    return response["message"]["content"]


        