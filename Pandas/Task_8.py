import pandas as pd
students = {
    'Name': ['Amit','Neha','Rahul','Sneha','Pooja'],
    'Marks':[78,85,90,66,72],
    'Subject':['Math','Math','Science','Science','Math']
}
df = pd.DataFrame(students)
pd.options.plotting.backend = "plotly" 

print(df.head(1))
df.plot(kind='bar',x = 'Name',y = 'Marks',title = 'Student Vs Marks')
df.plot(kind='line',x = 'Name',y = 'Marks',title = 'Student Vs Marks')
df.plot(kind='hist',x = 'Name',y = 'Marks',title = 'Student Vs Marks')