## Day 43: Logistic Regression + Gradient Descent 📉
Today was about the mathematical implementation of **Gradient Descent** using matrix operations for efficiency.
### 1. Vectorized Predictions
 * **Input:** We represent data as an m \times (n+1) matrix X and weights as a vector w.
 * **Calculation:** Predictions are calculated as \hat{Y} = \sigma(X \cdot w).
### 2. Gradient Derivation
 * **Loss Function:** We use the matrix form of Binary Cross-Entropy.
 * **Derivative:** The partial derivative of the loss with respect to weights simplifies to \frac{\partial L}{\partial w} = -\frac{1}{m}(Y - \hat{Y})X.
### 3. Weight Update Rule
 * **The Formula:** w = w + \eta \cdot \frac{1}{m}(Y - \hat{Y}) \cdot X.
 * **Note:** This update rule is mathematically elegant and shares the same form as Linear Regression.
