## Day 42: Logistic Regression Loss Function 🚀
Today's focus was on understanding why we move away from the **Perceptron's** "line-push/pull" mechanics toward **Maximum Likelihood Estimation** and **Cross-Entropy Loss** for Logistic Regression.
### 1. The Sigmoid Function
To convert linear outputs into probabilities, we use the Sigmoid function:

 * **Thresholding:** If z \ge 0, then \sigma(z) \ge 0.5 \rightarrow 1. If z < 0, then \sigma(z) < 0.5 \rightarrow 0.
 * **Derivative:** A key property for gradient descent is \sigma'(z) = \sigma(z)(1 - \sigma(z)).
### 2. From Likelihood to Log-Loss
 * **Maximum Likelihood:** We aim to find a line that maximizes the product of probabilities for all correctly classified points.
 * **The Log Trick:** Multiplying thousands of small probabilities results in tiny values that are hard to compute. We take the **negative log** to turn products into sums and convert the maximization problem into a minimization problem.
### 3. Binary Cross-Entropy (Log-Loss)
The generalized formula for calculating loss for a single point is:

 * **Case y=1:** Loss simplifies to -\log(\hat{y}_i).
 * **Case y=0:** Loss simplifies to -\log(1 - \hat{y}_i).
### Key Takeaway
Unlike the step function in Perceptrons, the **Sigmoid** provides a smooth gradient (y_i - \hat{y}_i can be any value between 0 and 1), allowing for more nuanced weight updates during **Gradient Descent**.
