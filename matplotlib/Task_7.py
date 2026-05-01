import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sales_data = pd.read_csv(r'D:\TuteDude\GenAI\matplotlib\sample_sales_data.csv')
print(sales_data.head())  
mobile = sales_data['Mobiles'].sum()
laptop = sales_data['Laptops'].sum()

plt.pie([mobile, laptop], labels=['Mobiles', 'Laptops'], autopct='%1.1f%%')
plt.title("Market Share of Mobiles and Laptops Sales")
plt.show()