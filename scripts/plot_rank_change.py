import matplotlib.pyplot as plt
import os

os.makedirs("outputs/figures", exist_ok=True)

docs = ["Doc A", "Doc B", "Doc C", "Doc D"]
baseline_rank = [1, 2, 3, 4]
temporal_rank = [3, 1, 2, 4]

plt.figure()
plt.plot(docs, baseline_rank, label="Baseline Rank", marker="o")
plt.plot(docs, temporal_rank, label="Temporal Rank", marker="o")

plt.gca().invert_yaxis()
plt.xlabel("Documents")
plt.ylabel("Rank Position")
plt.title("Retrieval Rank Changes with Temporal Scoring")
plt.legend()

plt.savefig("outputs/figures/rank_change.png")
plt.show()
