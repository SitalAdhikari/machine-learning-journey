## Day 18 – Handling Missing Categorical Data

Today I learned how to handle **missing values in categorical features**.

### Common Techniques

**1. Most Frequent Value (Mode)**

* Replace missing values with the **most common category** in that column.
* Works well when one category **dominates the distribution**.

**2. Missing Category**

* Replace null values with a new label such as **"Missing"**.
* Helps the model treat missing values as a **separate category**.

### Key Insight

Mode imputation is useful when the distribution is stable, but creating a **"Missing" category** can sometimes preserve more information about the data.

