from src.splitter.chunk import chunkDocuments
from src.loader.load_transcripts import load_transcript
from src.vector_store.storage import get_vector_store

def run_pipeline():
    docs   = load_transcript("transcripts/lec1.txt")
    chunks = chunkDocuments(docs)
    vector_store = get_vector_store()
    vector_store.add_documents(chunks)
    print("✅ Done!")

run_pipeline();