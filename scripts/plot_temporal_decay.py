import matplotlib.pyplot as plt
import numpy as np
import os

os.makedirs("outputs/figures", exist_ok=True)

days = np.arange(0, 2000, 50)
lambda_decay = 0.001
weights = np.exp(-lambda_decay * days)

plt.figure()
plt.plot(days, weights)
plt.xlabel("Document Age (days)")
plt.ylabel("Temporal Weight")
plt.title("Temporal Decay Function")

plt.savefig("outputs/figures/temporal_decay_curve.png")
plt.show()
