## Day 57: Introduction to Decision Trees
Today, I began exploring **Decision Trees**, a versatile algorithm used for both classification and regression (CART).
### Core Concepts
 * **Structure**: A Decision Tree acts as a series of **nested if-else statements**. It consists of a **Root Node** (the best feature for initial splitting), **Decision Nodes** (internal sub-trees), and **Leaf Nodes** (final class predictions).
 * **Geometric Intuition**: Mathematically, decision trees use hyperplanes that run **parallel to the axes** of the coordinate system, dividing the space into **hyper-cuboids**.
 * **Entropy**: Introduced the concept of Entropy as a **measure of disorder or impurity** within a dataset, which helps determine how to split the data.
### Example: Iris Classification
I visualized how a tree separates species like Setosa, Versicolor, and Virginica based on features such as **Petal Length (PL)** and **Sepal Length (SL)**.
### Pros & Cons
 * **Advantage**: Intuitive and easy to interpret as pseudo-code.
 * **Disadvantages**: High risk of **overfitting** and potential errors when working with **imbalanced datasets**.
Day 57 complete—moving from linear separators to hierarchical decision-making!
