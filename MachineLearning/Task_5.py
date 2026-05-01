import pandas as pd
import numpy as np
#Reading the csv file into DataFrame
cars_data = pd.read_csv('D:\TuteDude\GenAI\MachineLearning\cars.csv')
print(cars_data)

#checking the shape of the DataFrame
print(cars_data.shape)
#Displaying the column types of the DataFrame
print(cars_data.dtypes)
#Identifying the Numerical and Categorical columns in the DataFrame
Numerical_cols= cars_data.dtypes[(cars_data.dtypes == 'int64') | (cars_data.dtypes == 'float64')].index
Categorical_cols= cars_data.dtypes[cars_data.dtypes == 'str'].index
print("Numerical Columns:", Numerical_cols)
print("Categorical Columns:", Categorical_cols)
#Checking the missing values count per column in the DataFrame
missing_values_count = cars_data.isnull().sum()
#Rest of the Things to be done in the next task
cars_data.describe()
cars_data.info()
cars_data.head()
cars_data.tail()
