import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sales_data = pd.read_csv(r'D:\TuteDude\GenAI\matplotlib\sample_sales_data.csv')
print(sales_data.head())  
marks = sales_data['Mobiles']  # replace with your numeric column

plt.figure()
plt.hist(marks, bins=5,color='red', edgecolor='black')
plt.title("Distribution of Mobiles")
plt.xlabel("Mobiles")
plt.ylabel("Frequency")
plt.show()