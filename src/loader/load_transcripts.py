from langchain_community.document_loaders import TextLoader

def load_transcript(path="transcripts/lec1.txt"):
    loader = TextLoader(path)
    return loader.load()