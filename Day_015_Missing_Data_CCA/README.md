## Day 15 – Handling Missing Data (Complete Case Analysis)

Today I learned about **Complete Case Analysis (CCA)** for handling missing data in Machine Learning datasets.

CCA is a simple technique where we **remove rows that contain missing values** in selected columns.

### What I Learned

* Checking **percentage of missing values** in each column
* Selecting columns where **missing values are less than 5%**
* Applying **Complete Case Analysis (dropna)** on those columns
* Comparing **dataset size before and after CCA**
* Verifying that the **data distribution remains similar** after removing missing values

### Key Insight

After applying CCA, I compared the **distribution of features using KDE plots**.
The distributions remained **almost the same**, which means removing those rows did **not significantly affect the data pattern**.

### Dataset Observation

* Original dataset: **19,158 rows**
* After CCA: **17,182 rows**

### Files in This Notebook

* Missing value analysis
* Selecting eligible columns
* Applying Complete Case Analysis
* Distribution comparison before and after CCA
