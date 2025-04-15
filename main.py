from fastapi import FastAPI
from pydantic import BaseModel
from pymilvus import connections, Collection, utility
import uuid

app = FastAPI()

# Prisijungiam prie Milvus
connections.connect("default", host="localhost", port="19530")

@app.get("/")
def read_root():
    return {"message": "Sveiki iš FastAPI!"}

@app.get("/collections")
def list_collections():
    return {"collections": utility.list_collections()}

@app.post("/create_collection")
def create_collection(name: str):
    from pymilvus import FieldSchema, CollectionSchema, DataType

    fields = [
        FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
        FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=128)
    ]
    schema = CollectionSchema(fields=fields, description="Test collection")
    Collection(name, schema)
    return {"message": f"Kolekcija '{name}' sukurta."}
