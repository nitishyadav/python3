#Here we will try to merge the two files that we crated student1.csv and student2.csv
import pandas as pd 
df1 = pd.read_csv("student1.csv")
df2 = pd.read_csv("student2.csv")
result = pd.concat([df1,df2])
print(result)
