import os
from dotenv import load_dotenv
from series_manager.db import connect_mongodb

import os
from dotenv import load_dotenv
from series_manager.db import connect_mongodb

load_dotenv(dotenv_path='.env')
uri = os.environ.get("MONGO_URI")
print(f"DEBUG: URI found: {bool(uri)}")
success = connect_mongodb(uri)
print(f"DEBUG: Connection success: {success}")
