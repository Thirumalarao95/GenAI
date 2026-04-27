import pandas as pd
marks = [78,85,90,66,72]
df = pd.Series(marks)
print(df)
print("Minimum mark:", min(df))
print("Maximum mark:", max(df))
print("Sum of marks:", sum(df))
print("Average mark:", df.mean())

filter_marks = df.apply(lambda x:x if x>= 70 else None).dropna()
print("Filtered marks (>=70):", filter_marks)
print("Count of STudents passed",len(filter_marks))