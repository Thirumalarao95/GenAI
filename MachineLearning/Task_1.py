#importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import sklearn

#reading the csv data file into dataframe
cars_data = pd.read_csv('D:\TuteDude\GenAI\MachineLearning\cars.csv')
#Printing the shape of the dataframe
print(cars_data.shape)
#printing the column names which are present in our DataFrame
print(cars_data.columns)
#Printing the top 5 rows/records from the DataFrame
print(cars_data.head(5))
#printing the bottom 5 rows/records from the DataFrame
print(cars_data.tail(5))
#checking for null values in the DataFrame
print(cars_data.isnull().sum())
#checking for duplicate values in the DataFrame
print(cars_data.duplicated().sum())
#describing the DataFrame to get statistical information about the data
print(cars_data.describe())
#checking the data types of the columns in the DataFrame
print(cars_data.dtypes)
#Value counts of the 'Make' column in the DataFrame
print(cars_data['Make'].value_counts())
#Value counts of the 'Model' column in the DataFrame
print(cars_data['Model'].value_counts())  
#Value counts of the 'Year' column in the DataFrame
print(cars_data['Year'].value_counts())
#Checking for the unique values in the 'Make' column of the DataFrame
print(cars_data['Make'].unique())
#Checking for the unique values in the 'Model' column of the DataFrame
print(cars_data['Model'].unique())
#checking the min and max values of city_mpg column in the DataFrame
print(cars_data['city mpg'].min())
print(cars_data['city mpg'].max())
#checking for statistical information like mean,mode and median ,std of the DataFrame
print(cars_data['city mpg'].mean())
print(cars_data['city mpg'].median())
print(cars_data['city mpg'].std())
#checking for missing values in our DataFrame
print(cars_data.isnull().sum())
#checking for duplicate values in our DataFrame
print(cars_data.duplicated().sum())
#if we have duplicate values in our DataFrame then we can drop them using the below code
cars_data.drop_duplicates(inplace=True)
#checking for datatypes of the columns in our DataFrame
print(cars_data.dtypes)
#converting the datatype of 'city mpg' column from int to float 
cars_data['city mpg'] = cars_data['city mpg'].astype('float64')
print(cars_data.dtypes)
