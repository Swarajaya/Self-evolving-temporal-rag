import matplotlib.pyplot as plt
import os

os.makedirs("outputs/figures", exist_ok=True)

models = ["Baseline RAG", "Temporal RAG", "Self-Evolving RAG"]
scores = [0.58, 0.74, 0.88]

plt.figure()
plt.bar(models, scores)

plt.xlabel("Model Variant")
plt.ylabel("Overall Performance Score")
plt.title("Ablation Study of Proposed Framework")

plt.savefig("outputs/figures/ablation.png")
plt.show()
