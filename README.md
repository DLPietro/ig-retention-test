# user-retention-experiment
Goal of the repo: simutating an A/B experiment to evaluate an impact of a feature or retention / churn campaign, and building a small churn predictive model.

```text
user-retention-experiment/
│
├── data/
│   └── synthetic_users.csv              # Generated synthetic users dataset
│
├── notebooks/
│   └── ab_test_analysis.ipynb           # Complete notebook
│
├── scripts/
│   ├── generate_data.py                 # Dataset generator
│   ├── ab_test_analysis.py              # Statistic tests
│   └── churn_model.py                   # Predictive LLM model
│
├── results/
│   ├── retention_rates.png              # Retention plot
│   ├── churn_probability.png            # ML model plot
│   └── ab_summary.txt                   # Test Results
│
├── README.md                            # Project Description
└── requirements.txt                     # Ptrhon Libraries

```
