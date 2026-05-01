import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Reading the csv file into DataFrame
cars_data = pd.read_csv('D:\TuteDude\GenAI\MachineLearning\cars.csv')
print(cars_data.head())
print(cars_data.dtypes)

#Here I am plotting the scatter plot
sns.scatterplot(data=cars_data, x='Engine HP', y='city mpg')
plt.title("Horsepower vs MPG")
plt.show()

#Now i am plotting the heatmap plot for the numeric columns onmly
corr = cars_data.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

#Here I am plotting the bar plot f
sns.barplot(data=cars_data, x='Model', y='city mpg')
plt.title("Average MPG by Model")
plt.show()

#Here I am plotting the box plot
sns.boxplot(data=cars_data, x='Model', y='city mpg')
plt.title("MPG Distribution by City")
plt.show()


