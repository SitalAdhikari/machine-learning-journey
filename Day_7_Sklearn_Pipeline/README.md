# 📅 Day 7 – Titanic Survival Prediction (With Sklearn Pipeline)

Today I rebuilt the Titanic Survival Prediction model — this time using **Sklearn Pipelines** to create a cleaner and safer workflow.

After discovering suspicious 100% accuracy on Day 6, I wanted to fix potential data leakage and structure the preprocessing properly.

## 📌 What I Implemented

* Train-test split before preprocessing
* Column-wise preprocessing using ColumnTransformer
* One Hot Encoding for categorical features
* Standardization for numerical features
* Full workflow wrapped inside `sklearn.pipeline.Pipeline`
* Model training and evaluation

## 🎯 Key Learning

Using Pipelines:

* Prevents data leakage
* Makes code cleaner and modular
* Ensures preprocessing happens correctly during cross-validation
* Makes models production-ready

This approach is much more reliable compared to manual preprocessing.

Debug → Improve → Optimize.
Consistency continues.
