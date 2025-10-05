from src.ragdoc.loaders import load_pdfs_from_dir
from src.ragdoc.chunker import split_docs
from src.ragdoc.store import add_documents
from src.ragdoc.config import RAW_DIR

def main():
    docs = load_pdfs_from_dir(RAW_DIR)
    if not docs:
        print(f"No PDFs found in {RAW_DIR}. Put some files there and retry.")
        return
    chunks = split_docs(docs, chunk_size=300, chunk_overlap=50)
    add_documents(chunks)
    print(f"Ingested {len(chunks)} chunks from {len(docs)} PDF pages.")

if __name__ == "__main__":
    main()
