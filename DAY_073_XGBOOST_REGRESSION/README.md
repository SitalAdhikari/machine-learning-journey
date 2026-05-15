## Day 73: XGBoost Regression (Part 2)
Today, I finalized the mathematical workflow for **XGBoost Regression** trees, focusing on split selection and leaf output.
### Key Learnings
 * **Gain-Based Selection**: I identified the best split by comparing gains; the criteria with the highest gain (e.g., CGPA < 8.25) becomes the decision node.
 * **Tree Depth**: The process repeats to build the tree, using similarity scores (SS) to evaluate every potential branch.
 * **Leaf Output**: Final leaf values are calculated using \frac{\sum Residuals}{\text{Count} + \lambda}.
 * **Final Prediction**: Predictions are updated additively: Model_1 + (\eta \times \text{Tree Output}), where \eta is the learning rate.
Day 73 complete—from similarity scores to final predictions! 🚀
