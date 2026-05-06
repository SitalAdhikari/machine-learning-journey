## Day 64: Random Forest
Today, I explored **Random Forest**, a powerful bagging technique that builds a "forest" of decision trees to achieve low bias and low variance.
### Key Learnings
 * **Bagging vs. Random Forest**: Unlike standard bagging, Random Forest introduces **Feature Sampling** at the node level. Instead of selecting features once per tree, it selects a random subset at every single node split, increasing diversity and randomness.
 * **Stability**: By splitting the dataset and distributing noisy data across multiple trees, it effectively reduces variance.
 * **OOB Score**: Since ~37% of rows remain "Out-of-Bag" (untrained), they serve as an internal test set to validate model performance.
