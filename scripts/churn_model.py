# Churn Model for retention

# Step 1: Importing missing libraries
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, confusion_matrix, classification_report


# Step 2: Loading data and defining churn model with y and x
df = pd.read_csv('simulated_users.csv')

X = df[['sessions', 'deposits', 'feature_used']]
y = df['churn']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


# Step 3: Model implementation
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

auc = roc_auc_score(y_test, y_prob)
print(f"AUC: {auc:.3f}")
print(classification_report(y_test, y_pred))


# Step 4: Feature importance, and plot
coef = pd.DataFrame({'Feature': X.columns, 'Importance': model.coef_[0]})
sns.barplot(x='Importance', y='Feature', data=coef, palette='coolwarm')
plt.title('Churn Model Feature Importance')
plt.savefig('churn_probability.png', bbox_inches='tight')
plt.show()