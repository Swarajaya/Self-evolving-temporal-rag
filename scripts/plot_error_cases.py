import matplotlib.pyplot as plt
import os

os.makedirs("outputs/figures", exist_ok=True)

errors = ["Outdated Info", "Missing Context", "Hallucination"]
counts = [45, 30, 15]

plt.figure()
plt.bar(errors, counts)

plt.xlabel("Error Type")
plt.ylabel("Frequency")
plt.title("Error Case Analysis")

plt.savefig("outputs/figures/error_analysis.png")
plt.show()
