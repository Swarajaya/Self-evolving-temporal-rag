import matplotlib.pyplot as plt
import os

os.makedirs("outputs/figures", exist_ok=True)

iterations = [0,1,2,3,4]
documents = [100,120,145,170,200]

plt.figure()
plt.plot(iterations, documents, marker="o")

plt.xlabel("Self-Evolution Iterations")
plt.ylabel("Total Documents in Knowledge Base")
plt.title("Knowledge Base Growth Over Time")

plt.savefig("outputs/figures/kb_growth.png")
plt.show()
