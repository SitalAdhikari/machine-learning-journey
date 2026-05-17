## Day 75: XGBoost Objective & Loss Function
Today, I explored the formal **Objective Function** of **XGBoost** and how it incorporates regularization to control model complexity.
### Key Learnings
 * **Objective Function**: The total objective to minimize at step t is L^{(t)} = \sum_{i=1}^{n} L(y_i, \hat{y}_i^{(t-1)} + f_t(x_i)) + \Omega(f_t), balances training loss and regularization.
 * **Regularization Term (\Omega)**: Defined as \Omega(f) = \gamma T + \frac{1}{2}\lambda ||w||^2, where T is the number of terminal leaves and w represents leaf weights.
 * **Complexity Control**: The \gamma parameter penalizes the total number of leaves, while \lambda imposes an L_2 penalty on the weights to prevent overfitting.
Day 75 complete—mastering mathematical regularization in boosting ensembles! 🚀
