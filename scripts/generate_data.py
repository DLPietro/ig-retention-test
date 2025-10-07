# Data Generator A/B groups using Python
# Two group of people splitted, between treatment and control group

# Step 1: importing libraries, setting seed and number of players
import pandas as pd, numpy as np

np.random.seed(69)
n = 70000

# Step 2: Group assignment
groups = np.random.choice(['control', 'treatment'], size=n, p=[0.5, 0.5])

# Step 3: Base engagement metrics (for both groups)
sessions = np.random.poisson(lam=5, size=n)
deposits = np.random.gamma(shape=2, scale=50, size=n)

# Step 4: Treatment group effect with more sessions and deposits
sessions += np.where(groups == 'treatment', np.random.randint(0, 3, size=n), 0)
deposits += np.where(groups == 'treatment', np.random.normal(15, 10, size=n), 0)

# Step 5: Feature usage (higher in treatment)
feature_used = np.where(groups == 'treatment',
                        np.random.binomial(1, 0.7, size=n),
                        np.random.binomial(1, 0.4, size=n))

# Step 6: Churn generation: different in treatment group
base_churn = np.random.binomial(1, 0.45, size=n)
treatment_adjustment = np.where(groups == 'treatment', -0.1, 0)
churn_prob = np.clip(0.45 + treatment_adjustment - 0.02 * feature_used - 0.01 * (sessions > 6), 0, 1)
churn = np.random.binomial(1, churn_prob)

# Step 7: assemble dataset and print it
df = pd.DataFrame({
    'user_id': np.arange(1, n+1),
    'group': groups,
    'sessions': sessions,
    'deposits': np.round(deposits, 2),
    'feature_used': feature_used,
    'churn': churn
})

df.to_csv('data/simulated_users.csv', index=False)
print("✅ Dataset saved to data/simulated_users.csv")
