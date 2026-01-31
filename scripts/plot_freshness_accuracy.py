import matplotlib.pyplot as plt
import os

os.makedirs("outputs/figures", exist_ok=True)

freshness = [0.2, 0.4, 0.6, 0.8]
accuracy = [0.50, 0.62, 0.75, 0.88]

plt.figure()
plt.plot(freshness, accuracy, marker="o")

plt.xlabel("Knowledge Freshness Score")
plt.ylabel("Answer Accuracy")
plt.title("Effect of Freshness on Answer Accuracy")

plt.savefig("outputs/figures/freshness_accuracy.png")
plt.show()
