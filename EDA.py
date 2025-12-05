# Heatmap
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
ts1 = pd.DataFrame({
    'A': [1, 12, 33, 41, 58],
    'B': [22, 40, 16, 8, 100],
    'C': [33, 69, 29, 12, 105]
})

plt.figure(figsize=(10, 8))
sns.heatmap(ts1.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.show()
