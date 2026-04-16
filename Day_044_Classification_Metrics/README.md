## Day 44: Classification Metrics 📊
Today I moved beyond simple accuracy to understand how we truly evaluate classification models using **Confusion Matrices**.
### 1. Accuracy Score
 * **Definition**: The ratio of total correct predictions to the total number of predictions.
 * **Calculation**: \frac{TP + TN}{TP + FN + FP + TN}.
 * **Limitation**: Accuracy alone can be misleading, especially in critical fields like healthcare where a 1% error rate can be dangerous.
### 2. Confusion Matrix
A tool to visualize the specific types of mistakes a model makes:
 * **True Positive (TP)**: Correctly predicted positive.
 * **True Negative (TN)**: Correctly predicted negative.
 * **False Positive (FP)**: Type 1 Error (Model said "Yes", but it's "No").
 * **False Negative (FN)**: Type 2 Error (Model said "No", but it's "Yes").
### Key Takeaway
A high accuracy score doesn't always mean a good model. Understanding the **kind** of mistake (Type 1 vs. Type 2) is essential for solving real-world problems effectively.
