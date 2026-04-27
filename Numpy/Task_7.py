import numpy as np
sales = np.array([1200,1500,900,2000,1800,1700,1600])
Total_sales = np.sum(sales)
Avegerage_sales = np.mean(sales)
Highest_sales = np.max(sales)
Lowest_sales = np.min(sales)
std_dev_sales = np.std(sales)
above_avg = sales[sales > Avegerage_sales]
print("Total Sales:", Total_sales)
print("Average Sales:", Avegerage_sales)
print("Highest Sales:", Highest_sales)
print("Lowest Sales:", Lowest_sales)
print("Standard Deviation of Sales:", std_dev_sales)
print("Sales above Average:", above_avg)
