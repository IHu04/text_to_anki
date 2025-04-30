from langchain_mongodb import MongoDBAtlasVectorSearch
from src.config import MONGODB_COLLECTION, ATLAS_INDEX
from src.embeddings.get_embedding_model import get_Embedding_Model

def get_vector_store(embedding_model=None):
    embedding_model = get_Embedding_Model()
    return MongoDBAtlasVectorSearch(
        embedding=embedding_model,
        collection=MONGODB_COLLECTION,
        index_name=ATLAS_INDEX,
        relevance_score_fn="cosine",
    )


