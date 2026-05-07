## Day 65: Feature Importance in Random Forest
Today, I explored how to identify the most significant features in a dataset using **Feature Importance** in Decision Trees and Random Forests.
### Key Learnings
 * **Core Concept**: Not all features contribute equally to a model; identifying and removing unnecessary features is crucial for efficiency.
 * **Decision Tree Calculation**: Feature importance (fi_k) is calculated by summing the **node importance** for all nodes where a split occurs on feature *k*, then normalizing it against the total importance of all nodes.
 * **Random Forest Integration**: To find the overall feature importance in a Random Forest, you calculate the importance for every individual tree and then **average** those results.
 * **Visualization**: Utilized tools like rf.feature_importances_ and sns.heatmap to visualize feature impact
