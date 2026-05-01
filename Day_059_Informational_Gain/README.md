## Day 59: Information Gain in Decision Trees
Today, I explored **Information Gain**, the primary metric used by Decision Trees to determine the most effective feature for splitting data.
### Key Learnings
 * **Definition**: Information Gain measures the expected reduction in entropy after a dataset is split by an attribute.
 * **Calculation**: It is the difference between the **Parent Entropy** and the **Weighted Average Entropy** of the children.
 * **Selection Logic**: The algorithm calculates the gain for every column and selects the one with the highest value to split the data recursively.
 * **Leaf Nodes**: When a split results in an entropy of 0, that subset becomes a final **Leaf Node**
