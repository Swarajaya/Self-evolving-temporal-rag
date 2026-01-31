import matplotlib.pyplot as plt
import os

# Make sure output folder exists
os.makedirs("outputs/figures", exist_ok=True)

docs = ["Doc1", "Doc2", "Doc3", "Doc4", "Doc5"]

baseline_scores = [0.92, 0.85, 0.60, 0.52, 0.40]
temporal_scores = [0.75, 0.72, 0.70, 0.68, 0.66]

plt.figure()
plt.plot(docs, baseline_scores, label="Baseline RAG", marker="o")
plt.plot(docs, temporal_scores, label="Temporal RAG", marker="o")

plt.xlabel("Documents")
plt.ylabel("Retrieval Score")
plt.title("Temporal RAG vs Baseline RAG")
plt.legend()

plt.savefig("outputs/figures/retrieval_comparison.png")
plt.show()
