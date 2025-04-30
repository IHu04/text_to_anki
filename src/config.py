from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()  

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = "transcripts_to_anki"
COLLECTION_NAME = "chunks"

client = MongoClient(MONGO_URI)
MONGODB_COLLECTION = client[DB_NAME][COLLECTION_NAME]

ATLAS_INDEX = "vector_index"
