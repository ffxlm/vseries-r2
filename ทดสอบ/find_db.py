from pymongo import MongoClient
from urllib.parse import urlparse
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')
uri = os.environ.get("MONGO_URI")

client = MongoClient(uri)

# List all databases and check for 'series' or 'episodes' collections
for db_name in client.list_database_names():
    db = client[db_name]
    collections = db.list_collection_names()
    if 'series' in collections or 'episodes' in collections:
        print(f"FOUND: {db_name}")
        exit(0)

print("NOT_FOUND")
