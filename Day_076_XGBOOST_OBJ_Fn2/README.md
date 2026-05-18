## Day 76: XGBoost Objective Function Optimization
Today, I explored the mathematical optimization of the **XGBoost Objective Function** using Taylor expansion.
### Key Learnings
 * **Taylor Expansion**: The objective function at step t is approximated using first-order (gradient g_i) and second-order (Hessian h_i) derivatives: L^{(t)} \approx \sum_{i=1}^{n} [L(y_i, \hat{y}_i^{(t-1)}) + g_i f_t(x_i) + \frac{1}{2}h_i f_t^2(x_i)] + \Omega(f_t).
 * **Leaf Node Formulation**: By grouping the instances by leaf j (where w_j = f_t(x_i)), the objective can be rewritten in terms of leaf weights: \sum_{j=1}^{T} [(\sum_{i \in I_j} g_i)w_j + \frac{1}{2}(\sum_{i \in I_j} h_i + \lambda)w_j^2] + \gamma T.
 * **Optimal Weights (w_j^*)**: Taking the derivative with respect to w_j yields the optimal weight formula: w_j = -\frac{\sum g_i}{\sum h_i + \lambda}.
 * **Task Simplification**:
   * **Regression**: g_i = -(y_i - \hat{y}_i) and h_i = 1, yielding w_j = \frac{\sum \text{Residuals}}{\text{Count} + \lambda}.
   * **Classification**: g_i = -(y_i - p_i) and h_i = p_i(1 - p_i), giving w_j = \frac{\sum \text{Residuals}}{\sum p_i(1 - p_i) + \lambda}.
Day 76 complete—finding optimal weights through calculus! 🚀
