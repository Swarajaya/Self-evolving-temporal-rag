import json
import numpy as np
from pathlib import Path
from sentence_transformers import SentenceTransformer

# ---------------- CONFIG ----------------
RAW_DIR = Path("data/raw")
OUT_DIR = Path("data/embeddings")
MODEL_NAME = "all-MiniLM-L6-v2"
# ----------------------------------------


def load_documents():
    texts = []
    metadata = []

    for source in ["arxiv", "wikipedia", "web"]:
        src_dir = RAW_DIR / source
        if not src_dir.exists():
            continue

        for file in src_dir.glob("*.txt"):
            year = None
            with open(file, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()

                # crude year extraction
                for line in content.splitlines():
                    if "Year:" in line:
                        year = int(line.split("Year:")[1].strip())
                        break

            chunks = content.split("\n\n")
            for chunk in chunks:
                chunk = chunk.strip()
                if len(chunk) > 50:
                    texts.append(chunk)
                    metadata.append({
                        "source": source,
                        "file": file.name,
                        "year": year
                    })

    return texts, metadata


def main():
    print("📄 Loading documents...")
    texts, metadata = load_documents()

    print(f"📊 Total chunks: {len(texts)}")

    embedder = SentenceTransformer(MODEL_NAME)
    embeddings = embedder.encode(texts, show_progress_bar=True)

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    np.save(OUT_DIR / "embeddings.npy", embeddings)
    json.dump(texts, open(OUT_DIR / "texts.json", "w"), indent=2)
    json.dump(metadata, open(OUT_DIR / "metadata.json", "w"), indent=2)

    print("✅ Saved:")
    print(" - embeddings.npy")
    print(" - texts.json")
    print(" - metadata.json")


if __name__ == "__main__":
    main()
