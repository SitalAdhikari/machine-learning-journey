## Day 60: Gini Impurity and Numerical Data in Decision Trees
Today, I explored **Gini Impurity** as an alternative to Entropy and learned how Decision Trees handle **numerical features**.
### Key Learnings
 * **Gini Impurity**: Calculated as G.I = 1 - \sum (P_i^2). It is computationally faster than Entropy because it avoids logarithmic calculations.
 * **Performance Trade-offs**: While Gini is faster, Entropy often produces more balanced trees, whereas Gini can sometimes lead to **overfitting**.
 * **Numerical Features**: To split continuous data, the algorithm sorts values in ascending order and tests every value as a potential split point (e.g., rating > 3.5) to maximize Information Gain.
 * **Complexity**: Training is computationally expensive due to testing all split points, but **test time complexity** is only O(\log n), making it very fast for predictions.
Day 60 complete—optimizing tree construction for speed and precision! 📈
