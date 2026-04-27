## Day 55: Hard Margin vs. Soft Margin SVM
Today, I explored how Support Vector Machines handle imperfect, real-world data by transitioning from Hard Margin to **Soft Margin SVM**.
### Key Learnings
 * **Hard Margin Constraints**: Requires "totally clean" data with zero errors, where every point must satisfy y_i(\vec{w}\vec{x} + b) \geq 1.
 * **Soft Margin SVM**: Introduced to handle overlapping classes or outliers by allowing some misclassifications.
 * **Slack Variables (\zeta - Zeta)**: Used to represent the distance between an incorrectly classified point and its correct margin boundary.
   * For correctly classified points, \zeta = 0.
   * For incorrect points, \zeta > 0 represents the error distance.
 * **Objective Function**: The optimization goal shifts to minimizing both the weights and the classification errors:
   
 * **Hyperparameter C**: Acts as a regulator to balance maximizing the margin width and minimizing classification errors.
