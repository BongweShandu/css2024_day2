# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 20:49:01 2024

@author: bongw
"""

import pandas as pd

#Importing file from url
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")

#The data has no column names, therefore, adding column names (use single quotation '' for your list)

column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", header = None, names = column_names)

#DIFFERENT FILE TYPES

#Text files; use semi-colon
df = pd.read_csv("Geospatial Data.txt", sep = ";")
#print(df)

#Excel files; remember xlsx
df = pd.read_excel("residentdoctors.xlsx")
#print(df)

#JSon files
df = pd.read_json("student_data.json")
# print(df)


# TRANSFORM

#indexing a column
  
df = pd.read_csv("country_data_index.csv")
# print(df)
df = pd.read_csv("country_data_index.csv", index_col = 0)

#Skipping columns; use skiprows
df = pd.read_csv("insurance_data.csv", skiprows = 5)
# print(df)

#Adding column headings (use double quotation "" for your list)
df = pd.read_csv("patient_data.csv")
# print(df)

column_names = ["duration", "pulse", "max_pulse", "calories"]
df = pd.read_csv("patient_data.csv", header = None, names = column_names)
# print(df)

#Unique delimiter; the data is seperated by semi-colons and pandas is expecting a come
df = pd.read_csv("Geospatial Data.txt", sep = ";")

#Inconsistent data types and names
df = pd.read_excel("residentdoctors.xlsx")

  # Step 1: Extract the lower end of th
df['LOWER_AGE'] = df['AGEDIST'].str.extract('(\d+)-')

  # Step 2: Convert the new column to float
df['LOWER_AGE'] = df['LOWER_AGE'].astype(int)

#Working with dates
"""Sometimes dates are written in different formats. For example, 24-02-2024 and 02-24-2024."""
df = pd.read_csv("time_series_data.csv")
# Convert the 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')

# Split the 'Date' column into separate columns for year, month, and day
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day


#NANs and Wrong Formats
df = pd.read_csv('patient_data_dates.csv')

# Allows you to see all rows
pd.set_option('display.max_rows',None)
print(pd)

#Deleting a redundant index column, use the drop function
df.drop(['Index'],inplace=True,axis=1) 
"""works for any column you want to remove"""

#To replace empty values, use the fillna function
x = df["Calories"].mean()
df["Calories"].fillna(x, inplace = True)

x = df["Date"].mode()
df["Date"].fillna(x, inplace = True)  

#Wrong Date Format – Convert with to_datetime()
# df['Date'] = pd.to_datetime(df['Date'])
# df.dropna(subset=['Date'], inplace = True)

 
 
 
 