## Day 50: Naive Bayes & Mathematical Intuition
Today, I transitioned from basic probability to the **Naive Bayes Classifier**, focusing on its mathematical architecture.
### Key Learnings
 * **Probabilistic Classification**: Used a cricket match dataset (toss, venue, weather) to predict outcomes by comparing the posterior probabilities of "Won" vs. "Lost".
 * **Simplified Computation**: Learned that the denominator (evidence) can be ignored when comparing classes since it remains constant for all outcomes.
 * **Chain Rule & Independence**: Explored the **Chain Rule for Conditional Probability** and how Naive Bayes simplifies complex joint distributions by assuming feature independence.
Successfully implemented the "win" prediction logic where P(C_k|X) determines the final classification.
