import matplotlib.pyplot as plt
import os

os.makedirs("outputs/figures", exist_ok=True)

models = ["Baseline RAG", "Temporal RAG", "Self-Evolving RAG"]
rates = [0.32, 0.18, 0.08]

plt.figure()
plt.bar(models, rates)

plt.xlabel("Model")
plt.ylabel("Hallucination Rate")
plt.title("Hallucination Rate Comparison")

plt.savefig("outputs/figures/hallucination_rate.png")
plt.show()
