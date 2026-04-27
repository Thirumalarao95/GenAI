import pandas as pd
students = {
    'Name': ['Amit','Neha','Rahul','Sneha','Pooja'],
    'Marks':[78,85,90,66,72],
    'Subject':['Math','Math','Science','Science','Math']
}
df = pd.DataFrame(students)
print(df)
greaterthan75 = df[df['Marks'] >= 75]
math_students = df[df['Subject'] == 'Math']
avg = df['Marks'].mean()
morethan_avg_marks = df[df['Marks'] > avg]
failed_students = df[df['Marks'] < 70]
print("Students with marks greater than or equal to 75:\n", greaterthan75)
print("Students who are studying Math:\n", math_students)
print("Average marks:", avg)
print("Students with marks greater than average:\n", morethan_avg_marks)
print("Students who failed (marks less than 70):\n", failed_students)
