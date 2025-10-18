# A/B Test Analysis
# Checking the behaviour and results for both groups: treated and controlled

# Step 1: importing missing libraries
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency

df = pd.read_csv('data/simulated_users.csv')


# Step 2: reading csv file generated previously
df = pd.read_csv('simulated_users.csv')
display(df)
# Group stats calculations
summary = df.groupby('group')['retained'].mean().reset_index()
summary['retention_rate_%'] = (summary['retained'] * 100).round(2)
display(summary)


# Step 3: significance test using Chi-square
contingency = pd.crosstab(df['group'], df['retained'])
chi2, p, dof, expected = chi2_contingency(contingency)
print(f"Chi-square: {chi2:.2f}\nP-value: {p:.4f}")


# Step 4: Plot retention comparison
sns.barplot(x='group', y='retention_rate_%', data=summary, palette='viridis')
plt.title('Retention Rate by Group')
plt.ylabel('Retention (%)')
plt.savefig('retention_rates.png', bbox_inches='tight')
plt.show()