## Day 70: Gradient Boosting for Classification
Today, I explored **Gradient Boosting for Classification**, focusing on how it differs from the regression approach.
### Key Learnings
 * **Core Difference**: While regression uses Mean Squared Error, classification utilizes **Log Loss** as the loss function.
 * **Initial Model**: The first model calculates the **log(odds)** of the target classes rather than the mean.
 * **Probability Transformation**: This initial log(odds) value is converted into a probability using the logistic function: P = \frac{1}{1 + e^{-log(odds)}}.
 * **Pseudo Residuals**: Residuals are calculated as y - \text{probability} and passed to the next weak learner (Decision Tree Regressor).
 * **Leaf Node Calculation**: Output values for leaf nodes are computed using the formula: \frac{\sum \text{Residuals}}{\sum [\text{Previous Prob} \times (1 - \text{Previous Prob})]}.
Day 70 complete—mastering sequential probability refinement! 🚀
