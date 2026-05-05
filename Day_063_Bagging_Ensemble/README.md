## Day 63: Bagging Ensembles
Today, I explored **Bagging** (Bootstrap Aggregating), a powerful ensemble technique designed to reduce variance.
### Key Learnings
 * **Core Process**: It involves **Bootstrapping** (creating multiple data subsets with replacement) and **Aggregation** (combining model results via majority vote or average).
 * **Variance Reduction**: By training homogeneous models on different data subsets, error is distributed, significantly lowering variance.
 * **Pasting**: A variation where sampling is done **without replacement**.
 * **OOB Score**: Roughly **37%** of data remains "Out-of-Bag" (untrained), acting as a built-in validation set to test accuracy.
Day 63 complete—learning to stabilize models through diversity! 🚀
