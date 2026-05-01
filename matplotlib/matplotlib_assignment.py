
#importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Reading the CSV file and displaying the first few rows and columns
file_path = r'D:\TuteDude\GenAI\matplotlib\sample_sales_data.csv'
sales_data = pd.read_csv(file_path)
print(sales_data.info())
print(sales_data.head())
print(sales_data.columns)

## Task _1
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

#Task_2
#Plotting the scatter plot for Mobiles vs Laptops sold over the years
#Displaying the relationship between the number of Mobiles and Laptops sold over the years. This can help us understand if there is any correlation between the sales of Mobiles and Laptops.
plt.scatter(sales_data['Mobiles'], sales_data['Laptops'], color='red')
plt.title("Sales Trends Over Time")
plt.xlabel("Mobiles Sold")
plt.ylabel("Laptops Sold")
plt.show()

#Task _3
#Creating a vertical bar chart of laptops and Mobiles columns.
plt.bar(sales_data['Years'], sales_data['Mobiles'], color='red')

plt.xlabel('Years')
plt.ylabel('Mobiles')
plt.title('Mobiles Sales by Year')
plt.show()
#Creating a horizontal bar chart of laptops and Mobiles columns.
plt.barh(sales_data['Years'], sales_data['Mobiles'], color='red')

plt.xlabel('Years')
plt.ylabel('Mobiles')
plt.title('Horizontal Laptops Vs Mobiles')
plt.show()

# Task-4

x = np.arange(len(sales_data['Years']))
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

# Task-5
plt.figure()
plt.bar(sales_data['Years'], sales_data['Mobiles'], label='Mobiles')
plt.bar(sales_data['Years'], sales_data['Laptops'], bottom=sales_data['Mobiles'], label='Laptops')

plt.xlabel("Year")
plt.ylabel("Sales")
plt.title("Stacked Bar Chart")
plt.legend()
plt.show()

# Task-6

marks = sales_data['Mobiles'] 

plt.figure()
plt.hist(marks, bins=5,color='red', edgecolor='black')
plt.title("Distribution of Mobiles")
plt.xlabel("Mobiles")
plt.ylabel("Frequency")
plt.show()

# Task-7

mobile = sales_data['Mobiles'].sum()
laptop = sales_data['Laptops'].sum()

plt.pie([mobile, laptop], labels=['Mobiles', 'Laptops'], autopct='%1.1f%%')
plt.title("Market Share of Mobiles and Laptops Sales")
plt.show()