# Student Performance Analysis Using Numpy and Pandas

import pandas as pd
import numpy as np


df= pd.read_csv("1_students.csv", encoding="latin1")
df["Total"] = df[["Maths", "Physics","Chemistry"]].sum(axis=1)
df["Percentage"] = round(df["Total"]/3,2)

conditions = [ 
    df["Percentage"]> 85,
    (df["Percentage"]> 70) & (df["Percentage"]<= 85),
    (df["Percentage"]> 55) & (df["Percentage"]<= 70),
    (df["Percentage"]> 40) & (df["Percentage"]<= 55)

]
grades = ["A", "B","C","D"]
df["Grades"]= np.select(conditions,grades,default="Fail")
topper_marks = df["Total"].max()
lower_marks=df["Total"].min()
topper_name = df.loc[df["Total"] == topper_marks , "Name"].values[0]
lower_name= df.loc[df["Total"] == lower_marks,"Name" ].values[0]
print(f"Topper = {topper_name} \t Marks={topper_marks} \n Lower = {lower_name} \t Marks = {lower_marks}")
print(df[["Maths", "Physics", "Chemistry"]].mean())

df.to_csv("1_students.csv", index=False) 