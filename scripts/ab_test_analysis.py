# A/B Test Analysis
# Checking the behaviour and results for both groups: treated and controlled

# Step 1: loading data and libraries
import pandas as pd, seaborn as sns, matplotlib.pyplot as plt
from scipy.stats import chi2_contingency

df = pd.read_csv('data/simulated_users.csv')

# Step 1: defining Retention = 1 - churn
df['retained'] = 1 - df['churn']

# Step 2: group stats calculations
summary = df.groupby('group')['retained'].mean().reset_index()
summary['retention_rate_%'] = (summary['retained'] * 100).round(2)
print(summary)

# Step 3: significance test using Chi-square
contingency = pd.crosstab(df['group'], df['retained'])
chi2, p, dof, expected = chi2_contingency(contingency)
print(f"\nChi-square test: chi2={chi2:.2f}, p-value={p:.4f}")

with open('results/ab_summary.txt', 'w') as f:
    f.write(f"Chi-square test: chi2={chi2:.2f}, p={p:.4f}\n")
    f.write(str(summary))

# Step 4: Plot retention comparison
sns.barplot(x='group', y='retention_rate_%', data=summary, palette='viridis')
plt.title('Retention Rate by Group')
plt.ylabel('Retention (%)')
plt.savefig('results/retention_rates.png', bbox_inches='tight')
plt.show()
