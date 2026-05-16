## Day 74: XGBoost for Classification
Today, I explored **XGBoost for Classification**, focusing on similarity scores, gain, and leaf output calculations.
### Key Learnings
 * **Initial Prediction**: Starts by calculating the baseline log(odds) and converting them to probabilities.
 * **Similarity Score (SS)**: Evaluated using the formula: \frac{(\sum \text{Residual})^2}{\sum [\text{Previous Prob} \times (1 - \text{Previous Prob})] + \lambda}.
 * **Tree Splitting**: Splits are chosen by maximizing Gain = (SS_{Left} + SS_{Right}) - SS_{Root}.
 * **Leaf Output**: Calculated as \frac{\sum \text{Residual}}{\sum [\text{Previous Prob} \times (1 - \text{Previous Prob})] + \lambda} to update log(odds) predictions additively.
Day 74 complete—mastering XGBoost classification mechanics! 🚀
