## Day 69: Gradient Boosting Mathematics (Part 2)
Today, I continued the mathematical derivation of **Gradient Boosting Regression**, focusing on tree fitting and leaf value optimization.
### Key Mathematical Steps
 * **Pseudo Residuals as Targets**: After computing pseudo residuals (r_{im}) from the previous model, a new **Decision Tree Regressor** is trained using these residuals as the target values.
 * **Terminal Regions**: The tree splits the data into J_m terminal regions (leaves), denoted as R_{jm}.
 * **Leaf Value Optimization**: For each leaf, we calculate an output value (\gamma_{jm}) that minimizes the loss function relative to the previous model’s predictions.
 * **Model Update**: The ensemble is updated by adding the new tree’s predictions, scaled by the learning rate, to the existing model: F_m(x) = F_{m-1}(x) + \nu \sum \gamma_{jm}.
Day 69 complete—mastering how sequential trees iteratively reduce loss! 🚀
