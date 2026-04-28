import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sales_data = pd.read_csv(r'D:\TuteDude\GenAI\matplotlib\sample_sales_data.csv')
print(sales_data.head())  
Mobile = sales_data['Mobiles'].value_counts()

plt.figure()
plt.pie(Mobile, labels=Mobile.index, autopct='%1.1f%%')
plt.title("Market Share")
plt.show()