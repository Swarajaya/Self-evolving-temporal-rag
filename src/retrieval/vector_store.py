import faiss
import numpy as np

class VectorStore:
    def __init__(self, dim):
        self.index = faiss.IndexFlatL2(dim)
        self.meta = []

    def add(self, vectors, metadata):
        self.index.add(np.array(vectors).astype("float32"))
        self.meta.extend(metadata)

    def search(self, query_vec, k=5):
        dists, idxs = self.index.search(
            np.array([query_vec]).astype("float32"), k
        )
        return [(self.meta[i], d) for i, d in zip(idxs[0], dists[0])]
