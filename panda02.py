# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 09:46:11 2024

@author: bongw
"""

import pandas

#Importing: pd can be named anything
import pandas as pd

file = pd.read_csv("iris.csv")
print(file)



#Absolute path: C:\Users\bongw\css2024_day2   
#Relative path: iris.csv

#Importing data from websites
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")


#To give the data from the website headers since the original data does not have the headers
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data",header=None, names= column_names)

#DIFFERENT TYPES OF FILES

#Text
file = pd.read_csv("Geospatial Data.txt", sep=";")

#Excel
file = pd.read_excel("residentdoctors.xlsx")

#Json
file = pd.read_json("student_data.json")


#df = DataFrame; saves data in a table form

# url = "https://github.com/Asabele240701/css4_day02/blob/main/effects-of-covid-19-on-trade-at-15-december-2021-provisional.csv"

# df = pd.read_csv(chat_files/Accelerometer_data

#ETL stands form extraction, transformation and loading


#TRANSFORMATION

df = pd.read_csv("country_data_index.csv",index_col=0)

#Inconsistent data types & names
df = pd.read_excel("residentdoctors.xlsx")

print(df.info())
# print(df.describe())

#adding a column

"""
\d digits from 0 to 9, the + sign means u add one 
"""

df["LOWER_AGE"] = df["AGEDIST"].str.extract('(\d+)-')

print(df.info())

#astype: to convert to and object into an integer
df["LOWER_AGE"] = df["LOWER_AGE"].astype(int)
print(df.info())


#WORKING WITH DATES
"""
#Read dates from Excel as string; there are workds and dashes

Date formats: 10-01-2024 UK
                01-10-2024 US
"""

df = pd.read_csv("time_series_data.csv", index_col=0) #removing index column
print(df.info())

df['Date'] = pd.to_datetime(df['Date'])
print(df.info())

#df['Date'] = pd.to_datetime(df['Date'], format = "%d-%m-%y")
# print(df.info())

df['Date'] = pd.to_datetime(df['Date'], format = "%d-%m-%y")
print(df.info())

#Extracting dates
df['Year'] = df['Date'].dt.year

"""
.str
.extract
.astype
.dt
Ways to manipulate your data from your column
"""

#Remove an error column from Excel
#df.drop(index=26, inplace=True   (26 is the error position/column)


df = pd.read_csv("patient_data.csv")
print(df)

df = pd.read_csv('patient_data_dates.csv')
pd.set_option('display.max_rows',None)

print(df)

#Removing a column: use drop
df.drop(['Index'],inplace=True,axis=1)

#Replace empty space: use fillna
x = df["Calories"].mean()
df["Calories"].fillna(x, inplace = True)

#APPLYING DATA TRANSFORNATION
#Aggregation

df = pd.read_csv("iris.csv")
col_names = df.columns.tolist()
print(df.columns)

df["sepal_length_sq"] = df["sepal_length"]**2
df["sepal_length_sq2"] = df["sepal_length"].apply(lambda x: x**2)
grouped = df.groupby("class")
mean_square_values = grouped['sepal_length_sq'].mean()
print(mean_square_values)

# Append & Merge
df1 = pd.read_csv("person_split1.csv")
df2 = pd.read_csv("person_split2.csv")
df = pd.concat([df1, df2], ignore_index=True)

#--Inner join
df_merge = pd.merge(df1,df2, on="id")

#Filtering data
# df["class"] = df["class"].str.replace("iris-","")
# df = df[df['sepal_length'] > 5]
# df = df[df["class"] == "virginica"]
# df.to_csv("output/pulsar.csv") 
        



