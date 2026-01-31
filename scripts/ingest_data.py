import os
import json
from datetime import datetime
from tqdm import tqdm

RAW_DIR = "data/raw"
OUT_DIR = "data/processed"
CHUNK_SIZE = 400

os.makedirs(OUT_DIR, exist_ok=True)

def clean_text(text):
    return text.replace("\n", " ").strip()

def chunk_text(text, size=400):
    words = text.split()
    return [" ".join(words[i:i+size]) for i in range(0, len(words), size)]

processed_docs = []

for source in os.listdir(RAW_DIR):
    source_path = os.path.join(RAW_DIR, source)
    if not os.path.isdir(source_path):
        continue

    for file in tqdm(os.listdir(source_path), desc=f"Processing {source}"):
        if not file.endswith(".txt"):
            continue

        with open(os.path.join(source_path, file), "r", encoding="utf-8") as f:
            text = clean_text(f.read())

        chunks = chunk_text(text)
        timestamp = datetime.now().date().isoformat()  # simple timestamp

        for chunk in chunks:
            processed_docs.append({
                "text": chunk,
                "timestamp": timestamp,
                "source": source,
                "file": file
            })

with open(os.path.join(OUT_DIR, "documents.json"), "w", encoding="utf-8") as f:
    json.dump(processed_docs, f, indent=2)

print(f"Processed {len(processed_docs)} chunks")
