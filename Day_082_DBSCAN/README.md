## Day 82: DBSCAN Clustering
Today, I explored **DBSCAN** (Density-Based Spatial Clustering of Applications with Noise), an unsupervised algorithm that groups data based on regional density.
### Key Learnings
 * **Core Concepts**: Data points are categorized into three distinct groups based on a radius (\epsilon) and minimum points (\text{MinPts}) threshold:
   * **Core Points**: Points containing at least the minimum required neighbors within their radius.
   * **Border Points**: Points that have fewer neighbors than \text{MinPts} but fall inside a core point's neighborhood.
   * **Noise Points**: Outliers that are neither core nor border points.
 * **Algorithm Pipeline**: It labels points, builds clusters around unclustered core points, and expands them through density connectivity before assigning leftover border points to their nearest core cluster.
 * **Pros & Cons**: It requires only two hyperparameters and remains exceptionally robust to outliers. However, it struggles heavily when handling datasets with varying cluster densities.
Day 82 complete—mastering density-based spatial groupings! 🚀
