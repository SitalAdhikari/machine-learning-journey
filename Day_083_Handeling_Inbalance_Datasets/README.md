## Day 83: Handling Imbalanced Datasets
Today, I explored strategies for managing **Imbalanced Datasets** in classification tasks, where a stark class asymmetry biases predictive models toward the majority class.
### Key Learnings
 * **The Problem**: Standard models optimize for overall accuracy, which leads to biased algorithms that blindly predict the majority class while completely failing on minority instances.
 * **Undersampling**: Reduces majority class instances to match the minority class count using techniques like RandomUnderSampler. *Disadvantage: Severe loss of valuable training data.*
 * **Oversampling**: Replicates minority class instances to match the majority class volume using RandomOverSampler. *Disadvantage: High risk of overfitting, especially with Decision Trees.*
 * **SMOTE (Synthetic Minority Over-sampling Technique)**: Generates entirely new, synthetic minority data points instead of direct duplication. It fits a KNN model (K=5) on minority instances, selects a neighbor, and calculates new points along the line segment joining them.
Day 83 complete—mastering data balancing strategies! 🚀

late coz of electricity problem 
