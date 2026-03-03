# 📅 Day 12 – Feature Discretization (Binning)

Today I explored **Discretization (Binning)** using `KBinsDiscretizer` and analyzed how converting continuous features into bins affects model performance.

Dataset: Titanic
Features Used: **Age, Fare**
Model: Decision Tree Classifier

---

## 📌 What I Did

* Removed rows with missing values
* Trained Decision Tree **without binning**
* Applied `KBinsDiscretizer` using:

  * 15 bins
  * Quantile strategy
  * Ordinal encoding
* Used `ColumnTransformer` for column-wise binning
* Compared accuracy before and after transformation
* Tested performance using cross-validation

---

## 🎯 Model Performance

### 🔹 Without Binning

* Test Accuracy → **0.58**
* Cross-validation Accuracy → **0.56**

### 🔹 With Quantile Binning (15 bins)

* Test Accuracy → **0.59**
* Cross-validation Accuracy → **0.55**

---

## 🧠 Key Learnings

* Binning slightly improved test accuracy but did not significantly improve cross-validation performance.
* Decision Trees already handle non-linear patterns well, so discretization may not drastically improve performance.
* Quantile strategy ensures equal distribution of samples in each bin.
* Feature engineering must be validated using cross-validation, not just test accuracy.
* Custom/domain-based binning can also be applied using Pandas.


