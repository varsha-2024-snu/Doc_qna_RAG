from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from typing import List
from langchain.schema import Document
from .config import INDEX_DIR, COLLECTION_NAME, EMBED_MODEL

def get_embeddings():
    # Uses GOOGLE_API_KEY from your .env in the environment
    return GoogleGenerativeAIEmbeddings(model=EMBED_MODEL)

def get_chroma():
    return Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=get_embeddings(),
        persist_directory=str(INDEX_DIR),
    )

def add_documents(docs: List[Document]):
    db = get_chroma()
    db.add_documents(docs)
    # Chroma auto-persists when using persist_directory
    return db

def get_retriever(k: int = 5):
    db = get_chroma()
    return db.as_retriever(search_kwargs={"k": k})
