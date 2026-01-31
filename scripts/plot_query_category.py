import matplotlib.pyplot as plt
import os

os.makedirs("outputs/figures", exist_ok=True)

labels = ["Time-Sensitive Queries", "Non-Time-Sensitive Queries"]
sizes = [65, 35]

plt.figure()
plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
plt.title("Query Category Distribution")

plt.savefig("outputs/figures/query_category_distribution.png")
plt.show()
