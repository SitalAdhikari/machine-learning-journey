# Day 1 – Standardization in Machine Learning

Today I learned about **feature standardization (Z-score normalization)**.

Standardization transforms data so that:
- Mean = 0  
- Standard Deviation = 1  

Formula:
Z = (X - mean) / standard deviation

Why it is important:
- Helps gradient descent converge faster  
- Improves performance of distance-based models  
- Prevents features with large values from dominating  

In this notebook, I:
- Applied manual standardization
- Used StandardScaler from sklearn
- Compared data before and after scaling

Notebook: Standardization.ipynb
