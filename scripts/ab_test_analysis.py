# A/B Test Analysis
# Checking the behaviour and results for both groups: treated and controlled

# Step 1: importing libraries
import pandas as pd
import sqlite3

# Step 2: Defining file and table
csv_file = "simulated_users.csv"
table_name = "player_data"
db_file = "player_data.db"

# Step 3: Loading CSV into DataFrame
df = pd.read_csv(csv_file)

# Step 4: Renaming group column to user_group for safety
if 'group' in df.columns:
    df = df.rename(columns={'group': 'user_group'})
elif 'user_group' not in df.columns:
    raise ValueError("CSV missing 'group' or 'user_group' column")

# Step 5: Connecing to SQLite and creating / replacing table
conn = sqlite3.connect(db_file)
df.to_sql(table_name, conn, if_exists='replace', index=False)

# Step 6: Writing SQL query retention and churn aggregation per user group
query = """
SELECT
  user_group,
  COUNT(*) AS total_players,
  SUM(churn) AS churned,
  SUM(1 - churn) AS retained,
  ROUND(100.0 * SUM(1 - churn) / COUNT(*), 2) AS retention_rate_pct
FROM player_data
GROUP BY user_group;
"""

# Step 7: Executing query and loading to DataFrame
result = pd.read_sql(query, conn)
conn.close()

# Step 8: Showing results
print("📊 Retention Analysis Results:")
print(result)

# Statistical Testing of Retention difference
# Step 1: importing scipy for the stats
from scipy.stats import chi2_contingency

# Step 2: Connecting again for the retention difference
conn = sqlite3.connect('player_data.db')
df = pd.read_sql("SELECT user_group, churn FROM player_data", conn)
conn.close()

# Step 3: Testing Contingency table for Chi-square test
contingency = pd.crosstab(df['user_group'], 1 - df['churn'])
chi2, p_value, _, _ = chi2_contingency(contingency)

# Step 4: Printing results
print(f"✅ Chi-square test for retention difference")
print(f"Chi-square statistic: {chi2:.2f}")
print(f"P-value: {p_value:.4f}")