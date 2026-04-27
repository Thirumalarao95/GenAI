import pandas as pd
students = {
    'Name': ['Amit','Neha','Rahul','Sneha','Pooja'],
    'Marks':[78,85,90,66,72],
    'Subject':['Math','Math','Science','Science','Math']
}
df = pd.DataFrame(students)
print(df)
print("Printing the First 3 rows",df.head(3))
print("Printing the last 2 rows",df.tail(2))
print(df.shape)
print(df.columns)