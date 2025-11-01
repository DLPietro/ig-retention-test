# Logistic Regression ML churn model

# Step 1: Importing libraries using SKlearn 
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, classification_report

# Step 2: Connecting sqlite3 again for regression testing 
conn = sqlite3.connect('player_data.db')
df = pd.read_sql("SELECT sessions, deposits, feature_used, churn FROM player_data", conn)
conn.close()

# Step 3: Defining Y and X values for the regression model
X = df[['sessions', 'deposits', 'feature_used']]
y = df['churn']
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42, test_size=0.3)

model = LogisticRegression(max_iter=1000, class_weight='balanced')
model.fit(X_train, y_train)

# Step 4: Testing model
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]


# Step 5: Printing results
print("✅ Logistic Regression Churn Model Results")
print(f"AUC: {roc_auc_score(y_test, y_prob):.3f}")
print(classification_report(y_test, y_pred))

# Step 6: Feature importance
coef_df = pd.DataFrame({'Feature': X.columns, 'Coefficient': model.coef_[0]})
display(coef_df)

# Step 7: Export churn probabilities for visualization in Tableau
export_df = X_test.copy()
export_df['churn_probability'] = y_prob
export_df['actual_churn'] = y_test.values

export_df.to_csv('churn_probabilities.csv', index=False)
print("✅ Churn probabilities exported to churn_probabilities_export.csv")