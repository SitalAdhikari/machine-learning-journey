## Day 49: Conditional Probability & Bayes' Theorem
Explored the foundations of probability as they relate to Naive Bayes and Logistic Regression.
### Core Concepts
 * **Conditional Probability**: Defined by the formula P(A|B) = \frac{P(A \cap B)}{P(B)}, provided P(B) \neq 0.
 * **Independent Events**: Occur when P(A \cap B) = P(A) \cdot P(B), meaning P(A|B) = P(A).
 * **Mutually Exclusive Events**: Events that cannot happen simultaneously, where P(A \cap B) = 0.
### Bayes' Theorem
Implemented **Bayes' Theorem** to calculate posterior probabilities using prior knowledge and likelihood:

### Practical Application
 * **Dice Simulation**: Calculated probabilities for specific sums when rolling two dice (e.g., finding P(A|B) where A is a specific face value and B is a sum \leq 10).
 * **Manufacturing Problem**: Solved a real-world scenario involving three machines (M_1, M_2, M_3) to determine the probability that a defective marker originated from a specific machine (M_3).
