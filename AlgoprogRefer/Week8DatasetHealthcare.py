import pandas as pd

df= pd.read_csv("healthcaredataset.csv")

print(df.info) #Show the general content of the dataset
print(df.head()) #Show the first 5 rows
print(df.tail()) #Show the last 5 rows
print(df['Name'][0:8]) #Choosing what column to show and which numbers to show
print(df.isnull().sum()) #To check the number of column that has the most missing values
print(df[df['Gender']== 'Female']) #To take out only the female gender from the dataset
print(df["Medication"].value_counts()) #To count the total values in the column
print(df["Age"].mean()) #To find the average value
