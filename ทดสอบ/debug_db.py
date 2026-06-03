from series_manager.db import connect_mongodb, get_db
import os
from dotenv import load_dotenv

load_dotenv()
print(f"DEBUG: MONGODB_URI={os.environ.get('MONGODB_URI')}")
print(f"DEBUG: MONGODB_DB={os.environ.get('MONGODB_DB')}")

success = connect_mongodb()
print(f"DEBUG: Connect success={success}")
db = get_db()
print(f"DEBUG: DB object={db}")
if db is not None:
    print(f"DEBUG: DB name={db.name}")
    print(f"Collections: {db.list_collection_names()}")
