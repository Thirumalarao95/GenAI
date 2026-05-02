import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder,OrdinalEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

# I am Reading the File from my local and printing the top 5 and shape of the df
social_data = pd.read_csv(r"D:\TuteDude\GenAI\MachineLearning\Assignment_14\sales_dataset.csv")
print(social_data.head())
print("shape",social_data.shape)

#I am checking for the missing values and any duplicate are present in my data
print("Missing_Values",social_data.isna().sum())
print("Duplicate_values",social_data.duplicated().sum())

#I have the MIssing Values
