import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
#Reading the csv file into DataFrame
cars_data = pd.read_csv('D:\TuteDude\GenAI\MachineLearning\cars.csv')
print(cars_data.head())

#Here we had the number of door column as Float type but it should be Integer type so I am converting it into Integer type   
print(cars_data.dtypes)
cars_data['Number of Doors'] = cars_data['Number of Doors'].astype('Int64')
print(cars_data.dtypes)

print(cars_data['Make'].value_counts)
le = LabelEncoder()
cars_data['Make_Encode'] =le.fit_transform(cars_data['Make']) 

print(cars_data['Make_Encode'].value_counts)
# Here I am Considering the MSRP column as Target Column
#input_features and Target Column
print(cars_data.columns)

Final_data = cars_data[['Make','Model','Year','Engine HP','Engine Cylinders','Driven_Wheels','Vehicle Size','Vehicle Style',
                        'highway MPG','city mpg','Popularity','MSRP']]

print(Final_data.head())
# I am considerig the input features except MSRP column and target column is MSRP

categorical_features = ['Make', 'Model', 'Driven_Wheels', 'Vehicle Size','Vehicle Style']
numeric_features = ['Year', 'Engine HP', 'Engine Cylinders', 'highway MPG', 'city mpg']


transform_data = ColumnTransformer(
    transformers=[('tr1', OneHotEncoder(), categorical_features)],
    remainder='passthrough')
print(transform_data)
x = Final_data.iloc[:,:-1]
y = Final_data['MSRP']
x = transform_data.fit_transform(x)
print(x)
le_en = LabelEncoder()
y = le_en.fit_transform(y)
print(y)


