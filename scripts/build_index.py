import faiss
import numpy as np
import os

EMB_FILE = "data/embeddings/embeddings.npy"
OUT_DIR = "data/index"

os.makedirs(OUT_DIR, exist_ok=True)

embeddings = np.load(EMB_FILE).astype("float32")
dim = embeddings.shape[1]

index = faiss.IndexFlatL2(dim)
index.add(embeddings)

faiss.write_index(index, os.path.join(OUT_DIR, "faiss.index"))

print("FAISS index built with vectors:", index.ntotal)
