## Day 66: AdaBoost (Adaptive Boosting)
Today, I explored **AdaBoost**, a stagewise additive method that combines multiple "weak learners" to create a highly accurate ensemble.
### Key Learnings
 * **Decision Stumps**: AdaBoost typically uses trees with a max_depth=1, known as decision stumps.
 * **Weight Update Mechanism**: It assigns equal weights to all rows initially. After each step, it increases the weights of misclassified points, forcing the next model to focus on those errors.
 * **Model Performance (\alpha)**: A model's influence depends on its error rate; lower error leads to a higher \alpha (importance).
 * **Learning Rate**: Introducing a learning rate can slow down the process to effectively reduce **overfitting**.
Day 66 complete—mastering the art of learning from mistakes! 🚀
