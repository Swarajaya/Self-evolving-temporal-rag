from pathlib import Path

def load_documents(root_dir: str):
    docs = []
    for file in Path(root_dir).rglob("*.txt"):
        text = file.read_text(encoding="utf-8", errors="ignore")
        docs.append({
            "text": text,
            "source": str(file)
        })
    return docs
