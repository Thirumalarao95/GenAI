import pandas as pd
marks = [78,85,90,66,72]
df = pd.Series(marks)
print(df)
print(df.index)
print(type(df))
print(df[0])
print(df[-2::])