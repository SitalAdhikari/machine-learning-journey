## Day 77: XGBoost Similarity Scores & Splitting
Today, I explored the mathematical derivations of **Similarity Scores (SS)** in **XGBoost** and how they drive tree node splits.
### Key Learnings
 * **Mathematical Foundation**: Similarity scores are derived from the objective function using first and second-order gradients (g_i and h_i) grouped by leaf nodes.
 * **Regression Formula**: Computed as SS = \frac{(\sum \text{Residuals})^2}{N + \lambda}, where N is the number of residuals and \lambda is the regularization parameter.
 * **Classification Formula**: Formulated as SS = \frac{(\sum \text{Residuals})^2}{\sum [p_i(1 - p_i)] + \lambda}, weighting residuals by previous probabilities.
 * **Loss Reduction**: Node splits are determined by maximizing the Gain formula: \text{Gain} = SS_{\text{Left}} + SS_{\text{Right}} - SS_{\text{Parent}}, representing structural loss reduction.
Day 77 complete—uncovering structural split math! 🚀
