import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sales_data = pd.read_csv(r'D:\TuteDude\GenAI\matplotlib\sample_sales_data.csv')
print(sales_data.head())  
plt.figure()
plt.bar(sales_data['Years'], sales_data['Mobiles'], label='Mobiles')
plt.bar(sales_data['Years'], sales_data['Laptops'], bottom=sales_data['Mobiles'], label='Laptops')

plt.xlabel("Year")
plt.ylabel("Sales")
plt.title("Stacked Bar Chart")
plt.legend()
plt.show()