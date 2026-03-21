Day 23 – Handling Outliers using IQR & Percentile Method

Today I learned two important techniques to handle outliers: IQR (Interquartile Range) and Percentile Method.

1. IQR Method

The IQR method is based on the spread of the middle 50% of the data.

IQR = Q3 – Q1
Lower Bound = Q1 − 1.5 × IQR
Upper Bound = Q3 + 1.5 × IQR

Any value outside this range is considered an outlier.

🔹 Works well for skewed data
🔹 More robust than Z-score

2. Percentile Method

In this method, we remove extreme values based on percentile thresholds.

Example:

Remove values below 1st percentile
Remove values above 99th percentile

🔹 Simple and effective
🔹 Useful when we want to cap extreme values

What I Did
Calculated Q1 and Q3
Found IQR and outlier bounds
Removed or capped outliers using IQR
Applied percentile capping
Compared results before and after treatment
Key Insight
IQR method is better for skewed distributions
Z-score works better for normal distributions
Percentile method gives flexibility in handling extreme values
Final Takeaway

Different datasets require different outlier handling techniques.
Choosing the right method depends on the data distribution and problem context.
