import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
uri = os.environ.get("MONGO_URI")
db_name = os.environ.get("MONGODB_DB")
print(f"DEBUG: URI={bool(uri)}, DB={db_name}")

client = MongoClient(uri)
db = client[db_name]
print(f"Collections: {db.list_collection_names()}")
