# 🎬 Project 78 of 100 -- Movie Budget vs Revenue Regression 🇨🇴

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?logo=numpy)
![Seaborn](https://img.shields.io/badge/Seaborn-Visualization-4c72b0)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Linear%20Regression-F7931E?logo=scikitlearn)
![Status](https://img.shields.io/badge/Challenge-78%2F100-success)
![License](https://img.shields.io/badge/License-MIT-green)

------------------------------------------------------------------------

## 📌 Overview

This project explores the relationship between movie production budgets
and worldwide revenues using real-world box office data.

Through structured data cleaning, exploratory analysis, and regression
modeling, we investigate a fundamental question:

> Does spending more money on a movie increase its chances of generating
> higher revenue?

This notebook is part of my **100 Python Projects Challenge**, built
with discipline, consistency, and a long-term growth mindset.

------------------------------------------------------------------------

## 📂 Dataset

The dataset includes:

-   Production Budget (USD)
-   Worldwide Gross Revenue (USD)
-   Domestic Gross Revenue (USD)
-   Release Date
-   Movie Title

The data required cleaning before analysis due to currency formatting
and missing values.

------------------------------------------------------------------------

## 🧹 Data Preparation

Key preprocessing steps:

-   Removed currency symbols and commas
-   Converted financial columns to numeric types
-   Dropped missing values
-   Removed unreleased films at the time of data collection
-   Created a `Decade` column using floor division for historical
    analysis

Clean data → reliable insights.

------------------------------------------------------------------------

## 📊 Exploratory Data Analysis

The notebook investigates:

-   Average production budgets
-   Average worldwide revenue
-   Minimum and maximum revenues
-   Zero-revenue films
-   International-only releases
-   Percentage of money-losing films
-   Budget and revenue differences across decades

One major finding:

> Approximately 37% of films did not recover their production costs.

Cinema is art --- but financially, it's a serious risk.

------------------------------------------------------------------------

## 📈 Regression Modeling

Using **Scikit-Learn's LinearRegression**, we:

-   Modeled the relationship between budget and revenue
-   Compared classic cinema (pre-1970) vs modern cinema
-   Evaluated slope differences between eras
-   Interpreted R² scores for predictive strength

The results show a clear positive relationship between investment and
revenue --- but with increasing scale in modern cinema.

From millions to billions.

Same principle. Bigger stage.

------------------------------------------------------------------------

## 🛠 Technologies Used

-   Python\
-   Pandas\
-   NumPy\
-   Matplotlib\
-   Seaborn\
-   Scikit-Learn

------------------------------------------------------------------------

## 🚀 How to Run

1.  Clone this repository\
2.  Install dependencies:

``` bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

3.  Launch Jupyter Notebook:

``` bash
jupyter notebook
```

4.  Open:

Movie-Regression.ipynb

------------------------------------------------------------------------

## 🧠 Key Takeaways

-   Production budget is strongly correlated with worldwide revenue.
-   Modern films operate on significantly larger financial scales.
-   A substantial portion of films still lose money.
-   Historical segmentation provides deeper insight than aggregate
    analysis alone.

Data doesn't guess. It measures.

------------------------------------------------------------------------

## 🇨🇴 About This Project

This project keeps everything technically professional and fully in
English,\
while carrying a subtle Colombian tone --- warm, disciplined, and
analytical.

Built step by step.\
No shortcuts.\
Just consistent progress.
