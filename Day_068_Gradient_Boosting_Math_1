## Day 68: Gradient Boosting Mathematics (Part 1)
Today, I dived into the mathematical foundations of **Gradient Boosting Regression**, focusing on additive modeling and the initialization process.
### Key Mathematical Steps
 * **Additive Modeling**: The model is built as a sum of functions, where F(x) = f_0(x) + f_1(x) + \dots + f_m(x), and each subsequent function is a Decision Tree designed to improve the previous prediction.
 * **Initialization**: The process begins by finding a constant value f_0(x) that minimizes the differentiable loss function, L(y, F(x)).
 * **Loss Function**: Using a Squared Error loss function, \frac{1}{2}\sum (y_i - \hat{y}_i)^2, the initial prediction f_0(x) is mathematically proven to be the **mean** of the target values.
 * **Pseudo Residuals**: For each iteration m, we calculate pseudo residuals (r_{im}). These represent the negative gradient of the loss function with respect to the previous model's predictions.
 * **Residual Calculation**: In the case of squared error, the pseudo residual simplifies to the difference between the actual value and the previous prediction: r_{im} = y_i - f_{m-1}(x_i).
Day 68 complete—bridging the gap between algorithmic intuition and formal calculus! 🚀
