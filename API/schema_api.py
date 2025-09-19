from fastapi import APIRouter
from pydantic import BaseModel
from Model import schema_model

router = APIRouter()

@router.post("/upload-schema")
def upload_schema(schema:schema_model.Schema):
    return{
        "message":"Schema received",
        "table":schema.table,
        "columns":schema.columns
    }



