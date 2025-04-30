from typing import List
from langchain.schema import Document

from src.vector_store.storage import get_vector_store
from src.config import MONGODB_COLLECTION


def retrieve_chunks(query: str, k: int = 5) -> List[Document]:
    """
    Retrieve the top-k most relevant chunks for a given query using the vector store.
    """
    vector_store = get_vector_store()
    return vector_store.similarity_search(query, k)


def get_retriever(k: int = 5):
    """
    Returns a LangChain retriever wrapping the vector store for higher-level chains.
    """
    vector_store = get_vector_store()
    return vector_store.as_retriever(search_kwargs={"k": k})


