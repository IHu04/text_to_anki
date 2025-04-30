from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunkDocuments(doc):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    all_splits = text_splitter.split_documents(doc)

    return all_splits



