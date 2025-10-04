from fastapi import FastAPI

app = FastAPI(title="RAG DocQA API")

@app.get("/health")
def health():
    return {"status": "ok"}
