import pandas as pd
students = {
    'Name': ['Amit','Neha','Rahul','Sneha','Pooja'],
    'Marks':[78,85,90,66,72],
    'Subject':['Math','Math','Science','Science','Math']
}
df = pd.DataFrame(students)
print(df)
print(df.info())
print(df.describe())
print(df.head())
print(df.tail())
df2 = df.sort_values(by='Marks',ascending=False)
print(df2)
df2 = df2.reset_index(drop=True)
print(df2)