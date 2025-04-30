from src.splitter.chunk import chunkDocuments
from src.loader.load_transcripts import load_transcript
from src.vector_store.storage import get_vector_store
from src.generator.generate import generate_flashcards_for_topics

def run_pipeline():
    docs   = load_transcript("transcripts/lec1.txt")
    chunks = chunkDocuments(docs)
    vector_store = get_vector_store()
    vector_store.add_documents(chunks)


if __name__=="__main__":
    input_str = input("Enter topics (comma-separated): ")
    topics = [t.strip() for t in input_str.split(",")]
    cards = generate_flashcards_for_topics(topics)
    for card in cards:
        print(f"Topic: {card['topic']}\nQ: {card['question']}\nA: {card['answer']}\n")