## Day 19 – Random Sample Imputation

Today I learned **Random Sample Imputation**, a technique used to handle **missing values while preserving the original data distribution**.

### What is Random Sample Imputation?

Instead of filling missing values with the **mean, median, or mode**, we randomly select values from the **existing non-missing data in the same column** and use them to replace the missing entries.

This method helps maintain the **variance and distribution of the dataset**, which can improve model performance compared to simple imputation techniques.

### Key Steps

1. Count the number of missing values in a column.
2. Randomly sample the same number of values from the **non-null data**.
3. Replace the missing values with these randomly selected samples.

### Example (Concept)

* Find how many null values exist in a feature (e.g., `Age`, `GarageQual`, `FireplaceQu`).
* Sample the same number of values from the non-null entries.
* Fill the missing positions using those sampled values.

### Why Use Random Sample Imputation?

* Preserves **data distribution**
* Reduces bias introduced by mean/median imputation
* Works well for **both numerical and categorical variables**

### Key Insight

Random Sample Imputation is useful when you want to **retain the natural variability of the dataset**, making the imputed data closer to the real-world distribution.

