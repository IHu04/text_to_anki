from langchain_huggingface import HuggingFaceEmbeddings

def get_Embedding_Model():
        return HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
