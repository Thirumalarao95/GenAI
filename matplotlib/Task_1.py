#importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Reading the CSV file and displaying the first few rows and columns
sales_data = pd.read_csv(r'D:\TuteDude\GenAI\matplotlib\sample_sales_data.csv')
print(sales_data.info())
print(sales_data.head())
print(sales_data.columns)

#Plotting the scatter plot for Mobiles sold over the years
plt.plot(sales_data['Years'], sales_data['Mobiles'], color='red')
plt.title("Sales Trends Over Time")
plt.xlabel("Years")
plt.ylabel("Mobiles Sold")
plt.show()

#Plotting the scatter plot for Laptops sold over the years
plt.plot(sales_data['Years'], sales_data['Laptops'], color='blue')
plt.title("Sales Trends Over Time")
plt.xlabel("Years")
plt.ylabel("Laptops Sold")
plt.show()
