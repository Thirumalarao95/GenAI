import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sales_data = pd.read_csv(r'D:\TuteDude\GenAI\matplotlib\sample_sales_data.csv')
print(sales_data.head())  
marks = sales_data['Years']  # replace with your numeric column

plt.figure()
plt.hist(marks, bins=10,color='red', edgecolor='black')
plt.title("Years Distribution")
plt.xlabel("Years")
plt.ylabel("Frequency")
plt.show()