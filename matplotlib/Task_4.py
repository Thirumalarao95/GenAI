import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
sales_data = pd.read_csv(r'D:\TuteDude\GenAI\matplotlib\sample_sales_data.csv')
print(sales_data.head())    



x = np.arange(len(sales_data['Years']))  # the label locations
width = 0.40

plt.figure()
plt.bar(x - width/2, sales_data['Mobiles'], width, label='Mobiles')
plt.bar(x + width/2, sales_data['Laptops'], width, label='Laptops')

plt.xlabel("Year")
plt.ylabel("Sales")
plt.title("Sales Comparison")
plt.xticks(x, sales_data['Years'])
plt.legend()
plt.show()