import matplotlib.pyplot as plt
import os

os.makedirs("outputs/figures", exist_ok=True)

before = [0.35,0.40,0.45,0.38,0.42,0.39]
after = [0.55,0.60,0.65,0.62,0.68,0.70]

plt.figure()
plt.hist(before, bins=5, alpha=0.7, label="Before Evolution")
plt.hist(after, bins=5, alpha=0.7, label="After Evolution")

plt.xlabel("Confidence Score")
plt.ylabel("Frequency")
plt.title("Confidence Distribution Before vs After Self-Evolution")
plt.legend()

plt.savefig("outputs/figures/confidence_distribution.png")
plt.show()
