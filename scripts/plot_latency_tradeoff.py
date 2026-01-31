import matplotlib.pyplot as plt
import os

os.makedirs("outputs/figures", exist_ok=True)

latency = [0.8, 1.1, 1.6]
performance = [0.60, 0.75, 0.88]
models = ["Baseline", "Temporal", "Self-Evolving"]

plt.figure()
plt.scatter(latency, performance)

for i, m in enumerate(models):
    plt.text(latency[i], performance[i], m)

plt.xlabel("Latency (seconds)")
plt.ylabel("Performance Score")
plt.title("Latency vs Performance Trade-off")

plt.savefig("outputs/figures/latency_tradeoff.png")
plt.show()
