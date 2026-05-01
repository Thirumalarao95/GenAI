import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

# Reading the csv file into DataFrame
cars_data = pd.read_csv('D:\\TuteDude\\GenAI\\MachineLearning\\cars.csv')
print(cars_data.head())

# Convert 'Number of Doors' to integer
print(cars_data.dtypes)
cars_data['Number of Doors'] = cars_data['Number of Doors'].astype('Int64')
print(cars_data.dtypes)

# Label Encoding for 'Make' (optional, since we'll one-hot encode later)
le = LabelEncoder()
cars_data['Make_Encode'] = le.fit_transform(cars_data['Make'])

# Selecting relevant columns
Final_data = cars_data[['Make','Model','Year','Engine HP','Engine Cylinders',
                        'Driven_Wheels','Vehicle Size','Vehicle Style',
                        'highway MPG','city mpg','Popularity','MSRP']]

print(Final_data.head())

# Separate features and target
x = Final_data.iloc[:, :-1]
y = Final_data['MSRP']

# Define categorical columns
categorical_features = ['Make', 'Model', 'Driven_Wheels', 'Vehicle Size', 'Vehicle Style']

# Apply One-Hot Encoding using pandas
x = pd.get_dummies(x, columns=categorical_features, drop_first=False)

print(x.head())

#Encoding with Label Encoder
le_en = LabelEncoder()
y = le_en.fit_transform(y)

print(y)