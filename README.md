# 🎰 iGaming Retention Test — A/B Experiment & Churn Modeling

> _**“If I can’t access real player data, I’ll simulate it, and still extract business insights.”**_

This repository reproduces a **realistic iGaming retention experiment**, from **simulated data generation** to **A/B testing** and **churn modeling**, built entirely in **Python 3** and **SQL/Pandas/Ploty**.

**Main goal**: Test if a new feature (the “treatment”) improves player retention over a control group, and quantify the impact both statistically and predictively.

---

## 🧠 Project Overview

This repository simulates the **end-to-end analytics workflow** used in iGaming for evaluating feature effects on user retention:

1. Generate a synthetic dataset of **70,000 users**
2. Split into **Control vs Treatment**
3. Simulate sessions, deposits, and feature usage
4. Run a **retention A/B test** and statistical significance check
5. Train a **logistic regression churn model**
6. Visualize everything with **Plotly**

---

## 🧩 Data Generation - A/B Groups

Using `numpy` and `pandas`, let's simulate a dataset of **70,000 players**, split equally between **control** and **treatment**.

| Variable | Description | Distribution |
|-----------|--------------|---------------|
| `sessions` | Number of sessions | Poisson (λ = 5, Treatment: +2) |
| `deposits` | Total deposited amount (€) | Gamma (shape=2, scale=50), treatment: +€20 boost |
| `feature_used` | Whether the new feature was used | Binomial (p=0.4 for control, p=0.7 for treatment) |
| `churn` | Player left or not | Binomial, dynamic probability by group/features |

> 🎯 Treatment players show **higher deposits and slightly more sessions than control.**.

```python
✅ Dataset saved to simulated_users.csv  
70,000 rows × 6 columns
```

---

## 🧮 A/B Test Analysis: Retention Results

After generating the dataset, we compare retention (1 - churn) between groups:

| user_group | total_players | retention_rate_pct |
|-----------|--------------|---------------|
| _control_ | 34,891 | 56.3% |
| _treatment_ | 35,109 | 65.8% |

> **Treatment group** retention is **~9.5 percentage points higher**.
>
> A _Chi-square_ test confirms statistical significance:

```text
Chi-square: 655.00
P-value: 0.0000 ✅
```
> **Conclusion:** The new feature/treatment produces a clear, significant uplift in player retention.

---

## 📊 Visualization

_*Both retention and deposits are higher for the treatment group:*_.

![Barplot comparing retention across groups](https://github.com/DLPietro/ig-retention-test/blob/main/results/retention_rates.png)

![Deposit amount histogram across groups](https://github.com/DLPietro/ig-retention-test/blob/main/results/deposit_boxplot.png)


---

## 🤖 Churn Prediction Model

A Logistic Regression model is trained to predict churn:

> **Features**: Sessions, Deposits, Feature Used
>
> **Target:** _churn (1 = player left)_

![Churn Probability for the model](https://github.com/DLPietro/ig-retention-test/blob/main/results/churn_probability.png)

| Metric | Value |
|-----------|----|
| `AUC Score` | 0.547 |
| `Accuracy` | 54% |
| `Recall (Churn=1)` | 52% |
| `Precision (Churn=1)` | 43% |

> The model performs only slightly better than random. This is common with synthetic or highly balanced data and few features.


# 🧭 Feature Importance (Coefficients)

| **Feature** | **Coefficient** | **Interpretation** |
|-------------|-----------------|--------------------|
| `Sessions` | -0.027 | More sessions = lower churn |
| `Deposits` | -0.0004 | More deposits = lower churn |
| `Feature Used` | -0.197 | Used feature = much lower churn |

---

## 🛠 Methodology & Tools

- Data simulation: **Numpy & Pandas**
- Statistical Testing: **Scipy.stats**
- SQL-based aggregation: **SQLite**
- Visualization: **Plotly** (fully interactive)
- Machine Learning: **Scikit-learn** logistic regression

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
│   └── simulated_users.csv              # Synthetic dataset
│
├── notebooks/
│   ├── ab_test_analysis.py              # Statistic tests
│   └── player_data.db                   # MySQL database
│
├── scripts/
│   ├── generate_data.py                 # Data generator
│   ├── ab_test_analysis.py              # Statistic tests
│   └── churn_model.py                   # Predictive LLM model
│
├── results/
│   ├── retention_rates.png              # Retention barplot
│   ├── deposit_boxplot.png              # Deposit boxplot
│   ├── churn_probability.png            # Churn model plot
│   └── ab_summary.txt                   # Statistical test results
│
├── LICENSE                              # GNU License v3.0
├── README.md                            # Project Description
└── requirements.txt                     # Python Libraries

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
