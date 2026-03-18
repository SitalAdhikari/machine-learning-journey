## Day 21 – KNN Imputer & MICE

Today I explored more advanced techniques for handling missing data: **KNN Imputation** and **MICE (Multiple Imputation by Chained Equations)**.

### 1. KNN Imputer

**KNN Imputation** fills missing values based on the values of **nearest neighbors**.

* It finds the *k* closest data points (using distance metrics like Euclidean distance).
* The missing value is replaced using the **mean (or majority for categorical)** of those neighbors.

🔹 **Advantages**

* Considers relationships between features
* More accurate than simple imputation in many cases

🔹 **Disadvantages**

* Computationally expensive
* Sensitive to feature scaling

---

### 2. MICE (Multiple Imputation)

**MICE** is an iterative method where each feature with missing values is modeled as a function of other features.

* Missing values are filled multiple times using predictive models
* Each column is treated as a **dependent variable** in turn
* Process repeats until convergence

🔹 **Advantages**

* Captures complex relationships
* Produces more realistic imputations

🔹 **Disadvantages**

* Slower and more complex
* Requires careful implementation

---

### Key Difference

* **KNN Imputer** → Uses similarity between data points
* **MICE** → Uses predictive modeling for each feature


