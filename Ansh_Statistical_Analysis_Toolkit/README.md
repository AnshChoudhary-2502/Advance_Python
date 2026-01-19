# 📊 Sales Data Statistical Analysis & Normalization

## 📁 Dataset

**File:** `sales.csv`

**Columns:**

* `order_id`
* `Amount`
* `Discount`
* `Quantity_Sold`

Only numerical columns (`Amount`, `Discount`, `Quantity_Sold`) are used for analysis.

---

## Step 1 — Statistical Module

Build a Python module using **NumPy only** to compute the following statistical measures:

* Mean
* Median
* Variance
* Standard Deviation
* Skewness
* Kurtosis

> No use of `scipy` or other high-level statistics libraries.

---

## Step 2 — Distribution Analyzer

Analyze data distribution and detect anomalies.

### Visualizations

* Histogram
* Boxplot

### Anomaly Detection

* **Outliers (IQR Method)**

  * IQR = Q3 − Q1
  * Outliers: values outside [Q1 − 1.5×IQR, Q3 + 1.5×IQR]

* **Z-score Anomalies**

  * Z = (x − mean) / std
  * Anomaly if |Z| > 3

---

## Step 3 — Normalization Engine

Implement data scaling techniques:

* **Min-Max Scaling**

  * Scales data to range [0, 1]

* **Z-score Scaling (Standardization)**

  * Centers data at mean 0 with unit variance

* **Robust Scaling**

  * Uses Median and IQR
  * Resistant to outliers

---

## Step 4 — Performance Benchmark

Measure execution time of:

* Statistical Module
* Distribution Analyzer
* Normalization Engine

**Tool used:** `time.perf_counter()`

---

## ▶️ How to Run

```bash
pip install numpy pandas matplotlib
python benchmark.py
```

---

## 🎯 Learning Outcomes

* Strong understanding of descriptive statistics
* Manual implementation of preprocessing techniques
* Distribution analysis and anomaly detection
* Performance measurement of numerical computations

---

## 📌 Notes

* Dataset is loaded once to ensure fair benchmarking
* All computations are implemented from scratch using NumPy
