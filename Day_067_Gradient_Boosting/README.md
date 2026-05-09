## Day 67: Gradient Boosting
Today, I explored **Gradient Boosting**, a powerful additive ensemble technique that improves predictions by learning from the errors of previous models.
### Key Learnings
 * **Intuition**: The process starts with a simple base model—often the mean of the target values.
 * **Pseudo Residuals**: Subsequent models (typically Decision Trees) are trained to predict the **errors** (residuals) of the preceding model rather than the actual target.
 * **Additive Process**: Final predictions are updated by adding the weighted predictions of all trees: Output = M_1 + \eta M_2 + \eta M_3 \dots, where \eta is the **learning rate**.
 * **Comparison**: Unlike AdaBoost’s decision stumps, Gradient Boosting uses deeper trees and applies a constant learning rate to all models.
Day 67 complete—learning to minimize loss one step at a time! 🚀
