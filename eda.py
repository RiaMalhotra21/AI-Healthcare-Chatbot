import pandas as pd
import matplotlib.pyplot as plt

# Load your dataset
df = pd.read_csv('Medical Recommendation System\Training.csv')

# Get the count of each disease (prognosis)
disease_counts = df['prognosis'].value_counts().sort_values(ascending=False)

# Plotting the distribution
plt.figure(figsize=(12, 8))
disease_counts.plot(kind='bar', color='coral')
plt.title('Class Distribution: Number of Cases per Disease', fontsize=16)
plt.xlabel('Disease (Prognosis)', fontsize=14)
plt.ylabel('Number of Cases', fontsize=14)
plt.xticks(rotation=90)
plt.grid(axis='y')
plt.tight_layout()
plt.show()
