Day 10 – Log & Reciprocal Transformations in Machine Learning

Today I explored **mathematical feature transformations** and analyzed how they affect model performance.

The focus was on applying:

* Log Transformation (`log1p`)
* Reciprocal Transformation
* Square and Square Root Transformations

using `FunctionTransformer` in scikit-learn.

---

## 📌 What I Did

* Selected **Age** and **Fare** features from the Titanic dataset
* Handled missing values
* Visualized distributions using:

  * Histogram
  * Probability (Q-Q) Plot
* Trained:

  * Logistic Regression
  * Decision Tree Classifier
* Compared accuracy **before and after transformation**

---

## 🎯 Model Performance

### Before Transformation:

* Logistic Regression → **0.66**
* Decision Tree → **0.58**

### After Log Transformation:

* Logistic Regression → **0.64**
* Decision Tree → **0.59**

---

## 🧠 Key Insight

* Log transformation slightly **decreased accuracy** for Logistic Regression.
* Reason: The data was already close to normally distributed, so log transformation distorted it.
* Decision Tree showed almost no significant change.
* Square, sqrt, and reciprocal transformations also did not improve performance.

This shows an important lesson:
Transformations should be applied based on data distribution, not blindly.
