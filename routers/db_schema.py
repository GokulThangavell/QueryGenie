from fastapi import APIRouter
from pydantic import BaseModel
from model import schema_model
from services.qdrant_service import save_schema,get_all_schemas, search_schema


schema_router = APIRouter()

@schema_router.post("/upload-schema")
def upload_schema(schema:schema_model.Schema):
    return save_schema(schema)
    

@schema_router.get("/get_all_schemas")
def get_all():
    return get_all_schemas()

@schema_router.get("/search_schema")
def search(query:str):
    return search_schema(query)
    



