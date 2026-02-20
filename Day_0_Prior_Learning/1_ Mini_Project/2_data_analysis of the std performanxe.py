import pandas as pd
import numpy as np

df = pd.read_csv("2_Student_Marks.csv", encoding="latin1")

# print(df.isnull().sum) # to check the value is null or not
#  print(df[(df["number_courses"]<0) | (df["time_study"] <0) | (df["Marks"]<0)]  )  #to check the value is impossible or not
# print(df.describe())

q1= df["Marks"].quantile(0.25)
q3=df["Marks"].quantile(0.75)
iqr=q3-q1

print(df[(df["Marks"] < (q1- 1.5*iqr)) | (df["Marks"]<(q3+1.5*iqr))].sum())
df.drop( )