import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sales_data = pd.read_csv(r'D:\TuteDude\GenAI\matplotlib\sample_sales_data.csv')
print(sales_data.head())
print(sales_data.columns)
plt.scatter(sales_data['Mobiles'], sales_data['Laptops'], color='red')
plt.title("Sales Trends Over Time")
plt.xlabel("Mobiles Sold")
plt.ylabel("Laptops Sold")
plt.show()
