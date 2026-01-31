import faiss
import numpy as np
import json
from sentence_transformers import SentenceTransformer

index = faiss.read_index("data/index/faiss.index")
embeddings = np.load("data/embeddings/embeddings.npy")
metadata = json.load(open("data/embeddings/metadata.json"))

model = SentenceTransformer("all-MiniLM-L6-v2")

query = "latest large language models"
q_emb = model.encode([query]).astype("float32")

D, I = index.search(q_emb, k=3)

print("Query:", query)
for idx in I[0]:
    print("-", metadata[idx]["file"], "|", metadata[idx]["source"])
