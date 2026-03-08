# 🇨🇴 Project 73 of 100 Python Challenges  
## Programming Language Popularity Analysis (Stack Overflow Data)

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange?logo=plotly)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)
![Challenge](https://img.shields.io/badge/100%20Python%20Challenges-73%2F100-blueviolet)


> “Good data tells a story. Great visualization makes it unforgettable.”

---

## 📊 Project Overview

This project analyzes the popularity of programming languages over time using real Stack Overflow post data.

Each post on Stack Overflow is tagged with a programming language.  
By aggregating and visualizing these tags, we can explore:

- Which language has the most posts overall
- How popularity evolved over time
- When certain languages began to dominate
- Long-term trends using smoothed time-series analysis

The dataset spans from July 2008 onward.

---

## 📂 Files Included

- `Data-Visualization.ipynb` → Original Jupyter Notebook  
- `Data-Visualization.html` → Exported HTML version (viewable directly on GitHub)  
- `QueryResults.csv` → Stack Overflow dataset  
- `README.md`

The HTML file allows anyone to explore the full notebook — including all charts — without running the code locally.

---

## 🧠 Skills & Concepts Practiced

This project focuses on:

- Pandas DataFrame manipulation
- `.groupby()` aggregation
- Time-series conversion using `pd.to_datetime()`
- Data reshaping with `.pivot()`
- Handling missing values with `.fillna()`
- Multi-line data visualization with Matplotlib
- Grid-based subplot layouts
- Rolling mean smoothing for trend clarity

---

## 🔍 Data Exploration

We begin by:

- Loading and renaming dataset columns
- Inspecting structure with `.head()`, `.tail()`, `.info()`
- Measuring dataset size with `.shape()`
- Counting total posts per programming language

To identify overall popularity:

```python
total_posts = df.groupby('TAG').sum()
total_posts.sort_values('POSTS', ascending=False)
```

---

## 🔄 Data Transformation

To prepare the data for time-series visualization:

### Convert DATE column to datetime:
```python
df['DATE'] = pd.to_datetime(df['DATE'])
```
### Pivot the DataFrame:
```python
reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')
```
### Replace missing values:
```python
reshaped_df.fillna(0, inplace=True)
```

---

## 📈 Visualization Approach
### 1️⃣ Single Language Trend

Plotting individual languages (e.g., Java).

### 2️⃣ Multi-Line Comparison

Comparing Java vs Python to observe competitive growth.

### 3️⃣ Full Language Comparison

Plotting all languages together using a loop:

for column in reshaped_df.columns:
```python
plt.plot(reshaped_df.index, reshaped_df[column])
```

---

## 📊 Smoothed Trend Analysis

Time-series data can be noisy.
To clarify long-term trends, we apply a 6-month rolling average:
```python
roll_df = reshaped_df.rolling(window=6).mean()
```
This helps reveal structural growth patterns rather than short-term spikes.

---

## 🗂 Grid-Based Visualization (Enhanced Layout)

Instead of visual clutter from plotting all languages together, this project includes a structured subplot grid.

Each programming language is displayed in its own mini-chart:
```python
column_list = reshaped_df.columns.to_list()

n_cols = 5
n_rows = 3

fig, axs = plt.subplots(n_rows, n_cols, figsize=(20, 12), layout="constrained")

for i, col_name in enumerate(column_list):
    ax = axs.flat[i]
    ax.plot(reshaped_df.index, reshaped_df[col_name], linewidth=1.5)
    ax.set_title(col_name, fontsize=10)
    ax.tick_params(axis='both', labelsize=7)
    ax.grid(True, alpha=0.3)

for j in range(len(column_list), n_rows * n_cols):
    axs.flat[j].axis('off')

fig.suptitle("Stack Overflow Language Popularity – Individual View", fontsize=16)

plt.show()
```

This layout provides:

* Cleaner comparison
* Individual trend focus
* Improved readability
* Portfolio-level presentation

---

## 🏆 Key Insight

From both raw and smoothed visualizations:

**Python** emerges as the dominant language over time, showing sustained growth and overtaking historically strong languages such as Java and C++.

---

## 🛠 Technologies Used

* Python 3
* Pandas
* Matplotlib
* Jupyter Notebook

---

## 🌎 Why This Project Matters

This project demonstrates a complete data analysis workflow:

* Data cleaning
* Time-series transformation
* Reshaping structured datasets
* Visualization design
* Analytical interpretation

It reflects both technical execution and presentation clarity — essential skills in data analysis and data science roles.

---

## ☕ Final Thoughts

Data analysis is like Colombian coffee:

Strong foundation.
Careful preparation.
Clear finish.
