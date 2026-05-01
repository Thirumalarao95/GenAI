import pandas as pd
import numpy as np
#Reading the csv file into DataFrame
cars_data = pd.read_csv('D:\TuteDude\GenAI\MachineLearning\cars.csv')
print(cars_data)
#checking for missing values in the DataFrame
print("Missing_Values are",cars_data.isnull().sum())
#checking the data types of the columns in the DataFrame
print(cars_data.dtypes)

#Now I am filling the numerical missing values with mean/mode and categorical missing values with Unknown
cars_data['Engine Fuel Type'] = cars_data['Engine Fuel Type'].fillna('Unknown')
cars_data['Make'] = cars_data['Make'].fillna('Unknown')
cars_data['Model'] = cars_data['Model'].fillna('Unknown')
cars_data['Year'] = cars_data['Year'].fillna(cars_data['Year'].mean())
cars_data['Engine HP'] = cars_data['Engine HP'].fillna(cars_data['Engine HP'].mean())
cars_data['Engine Cylinders'] = cars_data['Engine Cylinders'].fillna(cars_data['Engine Cylinders'].mean())
cars_data['Transmission Type'] = cars_data['Transmission Type'].fillna('Unknown')
cars_data['Driven_Wheels'] = cars_data['Driven_Wheels'].fillna('Unknown')
cars_data['Number of Doors'] = cars_data['Number of Doors'].fillna(cars_data['Number of Doors'].mean())
cars_data['Market Category'] = cars_data['Market Category'].fillna('Unknown')
cars_data['Vehicle Size'] = cars_data['Vehicle Size'].fillna('Unknown')
cars_data['Vehicle Style'] = cars_data['Vehicle Style'].fillna('Unknown')
cars_data['highway MPG'] = cars_data['highway MPG'].fillna(cars_data['highway MPG'].mean())
cars_data['city mpg'] = cars_data['city mpg'].fillna(cars_data['city mpg'].mean())
cars_data['Popularity'] = cars_data['Popularity'].fillna(cars_data['Popularity'].mean())
print("Missing_Values are",cars_data.isnull().sum())
#Checking for Duplicate values in the DataFrame
print("Duplicate Values in the DataFrame:", cars_data.duplicated().sum())
#now I am dropping the duplicate values from the DataFrame
cars_data.drop_duplicates(inplace=True)
print("Duplicate Values:", cars_data.duplicated().sum())
#Renaming the columns to lower_case and snake_case format
cars_data.rename(columns=lambda x: x.strip().lower().replace(' ', '_'), inplace=True)
print(cars_data.columns)
print(cars_data.dtypes)
cars_data['number_of_doors'] = cars_data['number_of_doors'].astype(int)
print(cars_data.dtypes)
