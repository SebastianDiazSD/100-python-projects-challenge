# 🇨🇴 Challenge 81 of 100

## Multivariable Regression Valuation Model -- Boston Housing Dataset

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458)
![NumPy](https://img.shields.io/badge/NumPy-Scientific%20Computing-013243)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Regression-F7931E)
![Status](https://img.shields.io/badge/Project-Completed-success)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

------------------------------------------------------------------------

# Overview

This repository contains my **Project 81 of a 100 Python
Challenges**.

The objective of this project is to build a **multivariable regression
model** capable of estimating residential property prices using
historical housing data from **Boston in the 1970s**.

The analysis simulates the type of evaluation performed by a **real
estate development firm** when assessing potential residential
investments.

Rather than relying solely on intuition, statistical modeling allows
analysts to understand **how multiple factors interact to influence
property prices**.

------------------------------------------------------------------------

# Business Scenario

Imagine a real estate development company evaluating potential housing
projects.

Before construction begins, the company wants to estimate the **expected
market value of a property** based on characteristics such as:

-   Number of rooms in the dwelling
-   Distance to employment centers
-   Environmental conditions
-   Socioeconomic characteristics of the area
-   Educational infrastructure (students per teacher)
-   Accessibility to highways and services

A predictive model helps provide **data‑driven estimates that support
investment decisions**.

------------------------------------------------------------------------

# Dataset

The project uses the **Boston Housing dataset**, a well‑known dataset
used in statistics and machine learning education.

Dataset characteristics:

-   **506 observations**
-   **13 predictive features**
-   **1 target variable (PRICE)**

### Target Variable
```
  Variable   Description
  ---------- ---------------------------------------------------
  PRICE      Median value of owner‑occupied homes (in \$1000s)
```
### Example Features
```
  Feature   Description
  --------- ---------------------------------------
  RM        Average number of rooms
  DIS       Distance to employment centers
  NOX       Pollution levels
  PTRATIO   Student--teacher ratio
  LSTAT     Percentage of lower income population
  RAD       Highway accessibility
  TAX       Property tax rate
```
------------------------------------------------------------------------

# Project Workflow

The project follows a structured **data science workflow**:

### 1️⃣ Data Exploration

Initial inspection of the dataset structure and feature types.

### 2️⃣ Data Cleaning

Verification of:

-   Missing values
-   Duplicate records

### 3️⃣ Descriptive Statistics

Statistical summaries provide insight into housing prices, school
quality, and neighborhood conditions.

### 4️⃣ Data Visualization

Visualizations help reveal patterns in:

-   Housing prices
-   Number of rooms
-   Distance to employment centers
-   Infrastructure accessibility

### 5️⃣ Relationship Analysis

Pair plots and joint plots are used to understand correlations between
variables such as:

-   Pollution vs distance
-   Poverty vs housing size
-   Rooms vs property value

### 6️⃣ Train/Test Split

The dataset is divided into:

-   **80% training data**
-   **20% testing data**

This ensures the model can be evaluated using **unseen observations**.

### 7️⃣ Multivariable Regression Model

A **Linear Regression model** is trained using all available features.

### 8️⃣ Residual Analysis

Model performance is evaluated by analyzing:

-   Predicted vs actual values
-   Residual distribution
-   Skewness of prediction errors

### 9️⃣ Log Transformation

Because housing prices are positively skewed, a **log transformation**
is applied to improve model performance.

### 🔟 Model Comparison

Two models are compared:

-   Original regression model
-   Log‑transformed regression model

The transformed model demonstrates **improved statistical properties**.

------------------------------------------------------------------------

# Key Insights

Several meaningful patterns emerge from the analysis:

• Larger homes tend to command higher prices\
• Areas with higher poverty rates typically show lower property values\
• Pollution levels negatively correlate with housing prices\
• Neighborhood infrastructure and accessibility influence property
demand

Applying a **log transformation to housing prices significantly improves
model stability**, reducing skewness in residuals and increasing
explanatory power.

------------------------------------------------------------------------

# Example Property Price Prediction

Using average feature values from the dataset, the regression model
estimates a property value close to:
```bash
    ~ $20,700
```
*(values expressed in 1970s USD)*

This demonstrates how regression models can provide **quick valuation
estimates based on neighborhood characteristics**.

------------------------------------------------------------------------

# Technologies Used

The analysis was developed using the Python data science ecosystem.

-   Python
-   Pandas
-   NumPy
-   Seaborn
-   Matplotlib
-   Plotly
-   Scikit‑Learn

------------------------------------------------------------------------

# Repository Structure
```bash
    81-Boston-Regression
    │
    ├── Multivariable-Regression-Valuation-Model.ipynb
    ├── boston.csv
    └── README.md
```
------------------------------------------------------------------------

# Conclusion

This project demonstrates how **multivariable regression can be applied
to real estate valuation problems**.

While the Boston dataset is historical and simplified, the methodology
reflects techniques used in:

-   real estate analytics
-   urban economics
-   predictive modeling
-   investment analysis

The workflow illustrates an important principle in applied data science:

> Good models are not only about prediction --- they are also about
> understanding the data and the story behind it.
