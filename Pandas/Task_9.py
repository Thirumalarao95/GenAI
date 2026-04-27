import pandas as pd
sales = {
    'Day':['Mon','Tue','Wed','Thu','Fri'],
    'Revenue':[1200,1500,900,2000,1800]
}

df = pd.DataFrame(sales)
print(df)
print("Total_Revenue",df['Revenue'].sum())
print("Average_Revenue_Daily",df['Revenue'].mean())
print("Maximum_Revenue",df['Revenue'].max())
print("Minimum_Revenue",df['Revenue'].min())
df.plot(kind='bar',x = 'Day',y = 'Revenue',title = 'Daily Revenue')