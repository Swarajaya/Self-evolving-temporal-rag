import argparse
import json
from datetime import datetime
from pathlib import Path

from sentence_transformers import SentenceTransformer
import numpy as np
import faiss


# ------------------ CONFIG ------------------
DATA_DIR = Path("data")
EMB_DIR = DATA_DIR / "embeddings"
INDEX_DIR = DATA_DIR / "index"
LOG_DIR = Path("logs")
OUT_DIR = Path("experiments")

MODEL_NAME = "all-MiniLM-L6-v2"
TOP_K = 5
# --------------------------------------------


def load_embeddings():
    emb = np.load(EMB_DIR / "embeddings.npy")
    texts = json.load(open(EMB_DIR / "texts.json"))
    meta = json.load(open(EMB_DIR / "metadata.json"))
    return emb, texts, meta


def load_index():
    return faiss.read_index(str(INDEX_DIR / "faiss.index"))


def retrieve(query, embedder, index, texts, meta):
    q_emb = embedder.encode([query])
    D, I = index.search(np.array(q_emb).astype("float32"), TOP_K)

    results = []
    for idx in I[0]:
        results.append({
            "text": texts[idx],
            "source": meta[idx]["source"],
            "year": meta[idx]["year"]
        })
    return results


def run(mode):
    embedder = SentenceTransformer(MODEL_NAME)
    embeddings, texts, meta = load_embeddings()
    index = load_index()

    query = "latest large language models"

    results = retrieve(query, embedder, index, texts, meta)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    save_dir = OUT_DIR / mode
    save_dir.mkdir(parents=True, exist_ok=True)

    with open(save_dir / f"results_{timestamp}.json", "w") as f:
        json.dump(results, f, indent=2)

    LOG_DIR.mkdir(exist_ok=True)
    with open(LOG_DIR / "retrieval.log", "a") as f:
        f.write(f"[{timestamp}] Mode={mode}, Results={len(results)}\n")

    print(f"✅ Pipeline finished | mode={mode}")
    print(f"📁 Results saved to: {save_dir}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["baseline", "temporal", "self_evolving"], required=True)
    args = parser.parse_args()

    run(args.mode)
