
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams
from sentence_transformers import SentenceTransformer
from model import schema_model
from qdrant_client.models import FieldCondition, Filter, MatchValue


qdrant_client = QdrantClient("localhost", port=6333)
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

collection_name = "schema_collection"


if not qdrant_client.collection_exists(collection_name):
    qdrant_client.create_collection(
        collection_name=collection_name,
        vectors_config=VectorParams(size=384, distance="Cosine")
    )

def save_schema(schema:schema_model):
    payload = {
        "message" : "Schema uploaded successfully",
        "table":schema.table,
        "columns":[col.dict() for col in schema.columns]
    }
    schema_text = f"Table {schema.table} with columns: " +\
                    ", ".join([f"{col.name} ({col.type})" for col in schema.columns ])
    
    vector = embedding_model.encode(schema_text).tolist()
    qdrant_client.upsert(
        collection_name=collection_name,
        points=[{
            "id":hash(schema.table),
            "vector":vector,
            "payload":payload
        }]
    )
    return payload

def get_all_schemas():
    results, _= qdrant_client.scroll(
        collection_name= collection_name,
        limit=100,
        with_payload=True,
        with_vectors= False
    )
    return [point.payload for point in results]


def search_schema(query:str):
    query = query.lower().strip()
    query_vector = embedding_model.encode(query).tolist()
   
    results = qdrant_client.search(
        collection_name=collection_name,
        query_vector= query_vector,
        limit=3,
        with_payload= True
    )
    filtered = []
    for res in results:
        table= res.payload.get("table", "")
        if(table.lower() == query):
            filtered.append(res.payload)


    return filtered


#def search_schema(query:str):
#    query = query.lower().strip()
#    query_vector = embedding_model.encode(query).tolist()
#    payload_filter = Filter(
#        must=[
#            FieldCondition(key="table", match=MatchValue(value=query)),
#            # OR add columns filtering if needed
#        ]
#    )
#    results = qdrant_client.search(
#        collection_name=collection_name,
#        query_vector= query_vector,
#        limit=3,
#        with_payload= True,
#        query_filter=payload_filter
#    )
#    return[res.payload for res in results]


