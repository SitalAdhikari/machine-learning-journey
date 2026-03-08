## Day 17 – Arbitrary Value Imputation

Today I learned about **Arbitrary Value Imputation** for handling missing numerical data.

### What is Arbitrary Imputation?

In this method, missing values are replaced with a **specific constant value** that is outside the normal range of the data (for example **-1, 99, or 999**). This makes it easy for the model to recognize that the value was originally missing.

### Key Observations

* Arbitrary values clearly **separate missing data from real values**.
* However, using very large values can **increase variance and distort the data distribution**.
* It is often useful when we want the model to **treat missing values as a separate signal**.

### Key Takeaway

Arbitrary imputation is simple and sometimes effective, but it must be used carefully because it can **change the statistical properties of the dataset**.

