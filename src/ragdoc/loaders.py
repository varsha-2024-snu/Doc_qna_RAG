from pathlib import Path
from typing import List
from langchain_community.document_loaders import PyPDFLoader
from langchain.schema import Document

def load_pdfs_from_dir(raw_dir: Path) -> List[Document]:
    docs: List[Document] = []
    raw_dir = Path(raw_dir)
    for p in sorted(raw_dir.glob("**/*.pdf")):
        loader = PyPDFLoader(str(p))
        docs.extend(loader.load())
    return docs
