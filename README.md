# 🎰 iGaming Retention Test — A/B Experiment & Churn Modeling

> _**“If I can’t access real player data, I’ll simulate it, and still extract business insights.”**_

This mini project reproduces a **realistic iGaming retention experiment**, from **data generation** to **A/B testing** and **churn prediction modeling**, built entirely in **Python 3**.

The goal: to test if a new feature (the “treatment”) improves player retention over a control group — and to quantify it statistically and predictively.

---

## 🧠 Project Overview

This repository simulates the **complete analytics workflow** used in iGaming for evaluating feature performance and user retention:

1. Generate a synthetic dataset of **70,000 users**
2. Split them into **Control vs Treatment**
3. Simulate sessions, deposits, and feature usage
4. Run a **retention A/B test**
5. Train a **logistic regression churn model**

---

## 🧩 1. Data Generation — A/B Groups

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

---

## 🧮 2. A/B Test Analysis

After generating the dataset, we compare the retention rates (1 - churn) between control and treatment.

Group	Retention Rate
Control	56.8%
Treatment	66.6%

A Chi-square test confirms this difference is statistically significant:

```text
Chi-square: 712.02
P-value: 0.0000 ✅
```
> The treatment clearly increased player retention — around +10 percentage points.

---

## 📊 Visualization

Barplot comparing retention across groups:


Treatment users retained significantly more than control.

---

## 🤖 3. Churn Prediction Model




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
# ⚡ Credits

[![GitHub Profile](https://img.shields.io/badge/GitHub-DLPietro-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/DLPietro)
[![Email](https://img.shields.io/badge/Email-dileopie-d14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:dileopie@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Pietro-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/pietrodileo)

> _© 2025 Pietro Di Leo — From Operations to Data. One Commit at a Time._
