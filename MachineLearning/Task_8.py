import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Reading the csv file into DataFrame
cars_data = pd.read_csv('D:\TuteDude\GenAI\MachineLearning\cars.csv')
print(cars_data.head())
print(cars_data.dtypes)

#Plotting the histogram plot
sns.histplot(cars_data['highway MPG'],color = 'Blue',kde=True)
plt.title("Prices of Cars")
plt.xlabel("Prices")
plt.ylabel("Frequency")
plt.show()

#Plotting the count plot
sns.countplot(cars_data['Make'],color = 'Blue')
plt.show()
sns.countplot(cars_data['Model'],color = 'Red')
plt.show()

#Plotting the box plot
sns.boxplot(cars_data['MSRP'],color='Black')
plt.title("Displaying the Prices vs Model")
plt.xlabel("Model")
plt.xlabel("Make")
plt.show()