import pandas as pd
students = {
    'Name': ['Amit','Neha','Rahul','Sneha','Pooja'],
    'Marks':[78,85,90,66,72],
    'Subject':['Math','Math','Science','Science','Math']
}
df = pd.DataFrame(students)
print(df)
group_df = df.groupby('Subject')
print("maximum_marks_per_subject",group_df['Marks'].max())
print("number_of_students_per_subject",group_df['Name'].count())