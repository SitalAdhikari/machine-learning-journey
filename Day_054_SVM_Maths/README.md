## Day 54: SVM Mathematical Intuition
Dived into the geometric and mathematical foundations of **Support Vector Machines (SVM)**, focusing on hard margin maximization.
### Key Learnings
 * **Core Principles**: SVM seeks a hyperplane with the maximum distance from support vectors to ensure robust classification.
 * **Vector Projection**: Used vector projections to determine point classification based on the decision boundary \vec{w} \cdot \vec{x} + b = 0.
 * **Margin Optimization**: Derived the margin width formula, d = \frac{2}{\|\vec{w}\|}, identifying that maximizing the margin is equivalent to minimizing \|\vec{w}\|.
 * **Constraints**: Applied the constraint y_i(\vec{w} \cdot \vec{x}_i + b) \geq 1 to ensure all data points are correctly classified outside the margin.
Halfway through the math behind optimal separators!
