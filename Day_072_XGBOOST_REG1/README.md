## Day 72: XGBoost Regression (Part 1)
Today, I explored the construction of decision trees in **XGBoost Regression**. While it follows the same principle as Gradient Boosting, the tree-building process is unique.
### Key Learnings
 * **Similarity Score (SS)**: Trees are built by calculating SS for nodes using \frac{(\sum Residuals)^2}{\text{Number of Residuals} + \lambda}, where \lambda is regularization.
 * **Splitting Criteria**: Potential splits are determined by the mean of adjacent feature values.
 * **Gain Calculation**: The best split is chosen by maximizing Gain = (SS_L + SS_R) - SS_{Root}.
 * **Optimization**: The split with the highest gain becomes the root or decision node for the tree.
Day 72 complete—optimizing splits with Similarity Scores! 🚀
