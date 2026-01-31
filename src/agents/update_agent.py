from ..ingestion.document_loader import load_documents
from ..ingestion.cleaner import clean
from ..ingestion.chunker import chunk
from ..ingestion.timestamp_extractor import extract_timestamp

class UpdateAgent:
    def __init__(self, embedder, store):
        self.embedder = embedder
        self.store = store

    def update_from_sources(self, paths):
        docs = []
        for p in paths:
            text = open(p, encoding="utf-8", errors="ignore").read()
            text = clean(text)
            ts = extract_timestamp(text)
            for c in chunk(text):
                docs.append({
                    "text": c,
                    "timestamp": ts,
                    "source": p
                })

        if not docs:
            return 0

        embeddings = self.embedder.encode([d["text"] for d in docs])
        self.store.add(embeddings, docs)
        return len(docs)
