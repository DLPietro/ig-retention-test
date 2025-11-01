# Data Generator A/B groups using Python
# Two group of people splitted, between treatment and control group

# Step 1: importing libraries
import numpy as np
import pandas as pd

# Setting seed and number of players
np.random.seed(69)
n = 70000

# Step 2: Group assignment
groups = np.random.choice(['control', 'treatment'], size = n)

# Step 3: Base engagement metrics (for both groups)
sessions = np.random.poisson(lam = 5, size = n) + (groups == 'treatment') * np.random.poisson(lam = 2, size = n)

# Step 4: Deposits
base_deposits = np.random.gamma(shape = 2, scale = 50, size = n)
treatment_boost = (groups == 'treatment') * np.random.normal(20, 10, size = n)
deposits = np.clip(base_deposits + treatment_boost, 0, None)

# Step 5: Feature usage (higher in treatment)
feature_used = np.where(groups == 'treatment', np.random.binomial(1, 0.7, size = n), np.random.binomial(1, 0.4, size = n))

# Step 6: Churn generation: different in treatment group
churn_prob = 0.45 - 0.08 * (groups == 'treatment') - 0.03 * feature_used - 0.01 * (sessions > 6)
churn_prob = np.clip(churn_prob, 0.1, 0.9)
churn = np.random.binomial(1, churn_prob)

# Step 7: assemble dataset and print it
df = pd.DataFrame({
    'user_id': np.arange(1, n + 1),
    'group': groups,
    'sessions': sessions,
    'deposits': np.round(deposits, 2),
    'feature_used': feature_used,
    'churn': churn,
})
df.to_csv('simulated_users.csv', index = False)
print('✅ Simulated data saved to simulated_users.csv')