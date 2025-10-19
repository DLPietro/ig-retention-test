# 🎰 iGaming Retention Test — A/B Experiment & Churn Modeling

> _**“If I can’t access real player data, I’ll simulate it, and still extract business insights.”**_

This repository reproduces a **realistic iGaming retention experiment**, from **data generation** to **A/B testing** and **churn prediction modeling**, built entirely in **Python 3**.

**Main goal**: to test if a new feature (the “treatment”) improves player retention over a control group — and to quantify it statistically and predictively.

---

## 🧠 Project Overview

This repository simulates the **complete analytics workflow** used in iGaming for evaluating feature performance and user retention:

1. Generate a synthetic dataset of **70,000 users**
2. Split them into **Control vs Treatment**
3. Simulate sessions, deposits, and feature usage
4. Run a **retention A/B test**
5. Train a **logistic regression churn model**

---

## 🧩 Data Generation - A/B Groups (⚠️⚠️ TEMPORARY ⚠️⚠️)

Using `numpy` and `pandas`, we simulate a dataset of **70,000 players**, randomly split between a **control** and a **treatment** group.

The treatment group simulates a feature rollout or bonus exposure.

| Variable | Description | Distribution |
|-----------|--------------|---------------|
| `sessions` | Number of daily game sessions | Poisson (λ = 5) |
| `deposits` | Total deposited amount (€) | Gamma (shape=2, scale=50) |
| `feature_used` | Whether the new feature was used | Binomial (p=0.4 / 0.7) |
| `churn` | Player left or not | Binomial (with dynamic probability by group) |

> 🎯 Treatment players show **+15 avg deposit boost** and **slightly higher session count**.

```python
✅ Dataset saved to simulated_users.csv  
70,000 rows × 6 columns
```

---

## 🧮 A/B Test Analysis (⚠️⚠️ TEMPORARY ⚠️⚠️)

After generating the dataset, we compare the retention rates (1 - churn) between control and treatment.

>  **Group  Retention Rate**
> 
>  **Control    56.8%**
>
>  **Treatment  6.6%**

A _Chi-square_ test confirms this difference is statistically significant:

```text
Chi-square: 712.02
P-value: 0.0000 ✅
```
> The treatment clearly increased player retention, around +10 percentage points.

---

## 📊 Visualization

![Barplot comparing retention across groups](https://github.com/DLPietro/ig-retention-test/blob/main/results/retention_rates.png)

_*Treatment users retained significantly more than control*_.

---

## 🤖 Churn Prediction Model (⚠️⚠️ TEMPORARY ⚠️⚠️)

A Logistic Regression model has trained using:

> Sessions count, Total Deposits and Feature Usage
>
> **Target:** _churn (1 = player left)_

| Metric | Value |
|-----------|----|
| `AUC Score` | 0.531 |
| `Accuracy` | 62% |
| `Recall (Churn=1)` | 0% |
| `Precision (Churn=1)` | 0% |

> ⚠️⚠️ DISCLAIMER!! ⚠️⚠️: The baseline model is weak, it predicts the majority class (no churn).
>
> That’s actually typical in early-stage churn modeling when class imbalance is strong.

# 🧭 Feature Importance

| Feature | Coefficient |
|-----------|----|
| `Sessions` | Slightly negative |
| `Deposits` | Negative |
| `Feature Used` | Strongly negative |

---

## 🛠 Methodology & Tools

- Data simulation using **Numpy & Pandas**
- **Scipy.stats** for Statistical Testing
- **Matplotlib, Seaborn** for Data Visualization (_churn probability & retention rates by group_)
- Logistic Regression model with **Sklearn** library
- Export in _CSV, PNG_ outputs

---

## 🧭 All is beautiful, but why this project?

A single repository in iGaming is not enough to understand the work behind it: so I created another project to **master the KPI factors** an iGaming company research on to maximise profits, marketing campaign and efficiency.

In addition, I wanted to start using **Machine learning tools** to improve and enhance my analytical skills.

---

## 🏡 Project Structure

```text
user-retention-experiment/
│
├── data/
│   └── simulated_users.csv              # Generated synthetic users dataset
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
├── LICENSE                              # GNU License v3.0
├── README.md                            # Project Description
└── requirements.txt                     # Ptrhon Libraries

```

---

## 🔗 Related Work

- [📊 My Data Journey Blog](https://dlpietro.github.io) — Weekly updates on my upskilling  
- [🧠 My Learning Roadmap](https://github.com/DLPietro/learning-roadmap) — Publicly tracked progress  
- [🎲 iGaming Analytics Dashboard](https://github.com/DLPietro/igaming-analytics-case-study) — KPI and players Retention (_Cohort, Church..._)
- [📈 Empirical Analysis: S&P 500 vs IVV vs Fidelity](https://github.com/DLPietro/thesis-backtesting-etf-spx) — Using R, GARCH, backtesting

---

## ⚡ Credits

[![GitHub Profile](https://img.shields.io/badge/GitHub-DLPietro-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/DLPietro)
[![Email](https://img.shields.io/badge/Email-dileopie-d14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:dileopie@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Pietro-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/pietrodileo)

> _© 2025 Pietro Di Leo — From Operations to Data. One Commit at a Time._
