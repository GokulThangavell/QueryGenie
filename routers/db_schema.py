from fastapi import APIRouter
from pydantic import BaseModel
from model import schema_model
from services.qdrant_service import save_schema,get_all_schemas, search_schema, delete_schema, delete_all_schemas


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

@schema_router.delete("/delete_schema")
def delete(table:str):
    return delete_schema(table)

@schema_router.delete("/delete_all_schema")
def delete_all():
    return delete_all_schemas()
    



