## Day 81: Agglomerative Hierarchical Clustering
Today, I explored **Hierarchical Clustering**, an unsupervised algorithm that handles complex data patterns where K-Means fails.
### Key Learnings
 * **Core Types**:
   * **Agglomerative**: a bottom-up approach that treats each point as a cluster and merges them iteratively.
   * **Divisive**: a top-down approach that starts with one cluster and recursively splits it.
 * **Linkage Criteria**: Single (minimum distance), Complete (maximum distance), Group Average, and Ward (minimizes variance).
 * **Dendrograms**: Tree diagrams used to identify the hierarchy and determine the ideal number of clusters.
 * **Limitation**: High memory complexity (O(N^2)) since it computes a proximity matrix for all points, making it unsuitable for large datasets.
Day 81 complete—mastering tree-based groupings! 🚀
