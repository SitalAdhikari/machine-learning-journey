## Day 62: Voting Ensembles
Today, I explored **Voting Ensembles**, a fundamental type of ensemble learning that leverages multiple independent models to improve overall prediction accuracy.
### Key Learnings
 * **Core Concept**: Combines different algorithms (Base Models) trained on the same data to make a final prediction.
 * **Types of Voting**:
   * **Hard Voting**: The final output is based on the **majority count** of the predicted classes.
   * **Soft Voting**: The final output is based on the **average probability** assigned to each class by the models, which is often more effective.
 * **Mathematical Intuition**: If you combine three independent models with 70% accuracy each, the ensemble's collective accuracy can rise to 78% due to the "Wisdom of the Crowd".
 * **Critical Assumption**: For the ensemble to be effective, base models must be **independent** and have an accuracy score better than random guessing (>50%).
### Implementation in Scikit-Learn
I practiced using VotingClassifier and VotingRegressor, experimenting with the weights parameter to adjust the importance of specific base models.
Day 62 complete—learning how collective intelligence outpaces individual experts! 🚀
