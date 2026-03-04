# 📅 Day 13 – Handling Mixed Data Columns

Today I learned how to handle **mixed-type columns** (columns containing both letters and numbers) in a dataset.

Dataset used: Titanic

The focus was on the **Cabin** column, which contains alphanumeric values like:

* B45
* C23 C25 C27
* F G63
* A21

---

## 📌 Problem

Some columns contain a mixture of:

* Categorical information (letters)
* Numerical information (numbers)

These cannot be directly used in machine learning models.

---

## ⚙️ What I Did

* Removed missing values
* Analyzed the Cabin column
* Extracted:

  * **Numerical part** → Cabin number
  * **Categorical part** → Cabin deck (first letter)
* Created two new features:

  * `cabin_num`
  * `cabin_cat`

Used:

```python
df['cabin_num'] = df['Cabin'].str.extract('(\d+)')
df['cabin_cat'] = df['Cabin'].str[0]
```

---

## 🧠 Key Learning

* Mixed columns should be separated into meaningful features.
* Extracting structured information improves feature engineering.
* Real-world datasets are messy — preprocessing is critical.
* The same approach can also be applied to columns like **Ticket**.

