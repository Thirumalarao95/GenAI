import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sales_data = pd.read_csv(r'D:\TuteDude\GenAI\matplotlib\sample_sales_data.csv')

plt.bar(sales_data['Years'], sales_data['Mobiles'], color='red')

plt.xlabel('Years')
plt.ylabel('Mobiles')
plt.title('Mobiles Sales by Year')
plt.show()


plt.barh(sales_data['Years'], sales_data['Mobiles'], color='red')

plt.xlabel('Years')
plt.ylabel('Mobiles')
plt.title('Horizontal Laptops Vs Mobiles')#sales_data.plot(kind='bar', x='Cost', y='Profit', color='red')
#sales_data['Revenue'].plot(kind='bar', stacked=True)
plt.show()
