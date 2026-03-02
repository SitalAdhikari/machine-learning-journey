 Day 11 – Power Transformer (Box-Cox & Yeo-Johnson)

Today I explored **Power Transformation** techniques to improve model performance by making data more normally distributed.

I worked on the **Concrete Strength dataset** and applied:

* Box-Cox Transformation
* Yeo-Johnson Transformation
* Linear Regression
* Cross Validation (R² score comparison)

---

##  Dataset Overview

* 1030 rows
* 8 input features
* Target variable: **Strength**
* No missing values

---

##  Model Performance

### 🔹 Before Transformation

* Test R² Score → **0.62**
* Cross Validation R² → **0.46**

---

### 🔹 After Box-Cox Transformation

* Test R² Score → **0.76**
* Cross Validation R² → **0.66**

---

###🔹 After Yeo-Johnson Transformation

* Test R² Score → **0.77**
* Cross Validation R² → **0.68**

##  Key Learnings

* Power transformations significantly improved model performance.
* Box-Cox requires strictly positive values (handled using +0.00001 adjustment).
* Yeo-Johnson works with zero and negative values.
* Making features more normally distributed improves Linear Regression performance.
* Data transformation can impact results more than changing the model.


