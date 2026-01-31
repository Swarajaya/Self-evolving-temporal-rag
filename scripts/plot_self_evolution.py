import matplotlib.pyplot as plt
import os

os.makedirs("outputs/figures", exist_ok=True)

iterations = [1, 2, 3, 4, 5]
before = [0.42, 0.40, 0.38, 0.41, 0.39]
after = [0.55, 0.60, 0.65, 0.68, 0.72]

plt.figure()
plt.plot(iterations, before, label="Before Self-Evolution", marker="o")
plt.plot(iterations, after, label="After Self-Evolution", marker="o")

plt.xlabel("Iteration")
plt.ylabel("Confidence Score")
plt.title("Impact of Self-Evolution on Confidence")
plt.legend()

plt.savefig("outputs/figures/self_evolution.png")
plt.show()
