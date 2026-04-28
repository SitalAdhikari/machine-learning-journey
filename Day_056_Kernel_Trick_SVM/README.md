## Day 56: The Kernel Trick in SVM
Today, I explored how **Support Vector Machines** handle non-linear datasets by projecting them into higher dimensions using the **Kernel Trick**.
### Key Concepts
 * **Dimension Transformation**: When data is not linearly separable in a low dimension (e.g., 1D), we convert it to a higher dimension (e.g., 2D or 3D) where a linear hyperplane can separate the classes.
 * **Kernel Functions**: These functions allow us to operate in high-dimensional space without explicitly calculating the coordinates of the data in that space.
 * **Common Kernel Types**:
   * **Linear**: Used for linearly separable data.
   * **Polynomial**: Handles non-linear relationships using a specified degree (default is 3).
   * **RBF (Radial Basis Function)**: A popular choice for complex datasets, often using transformations like y = e^{-x^2}.
   * **Sigmoid**: Useful for neural network-like behaviors.
### Implementation in Scikit-Learn
I practiced implementing different kernels using the SVC class:
```python
from sklearn.svm import SVC

# Linear Kernel
clf = SVC(kernel="linear")

# RBF Kernel
clf_rbf = SVC(kernel="rbf")

# Polynomial Kernel with degree 3
clf_poly = SVC(kernel="poly", degree=3)

```
Day 56 complete—understanding how to unlock high-dimensional power for non-linear classification!
