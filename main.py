from fastapi import FastAPI
from routers.db_schema import schema_router
from routers.generate_query import generate_query_router

app = FastAPI()

app.include_router(schema_router, prefix="/schema", tags=["Schema"])
app.include_router(generate_query_router, tags=["GenerateQuery"])

