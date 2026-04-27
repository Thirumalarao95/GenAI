import pandas as pd
marks = [78,85,90,66,72]
df = pd.Series(marks)
df1 = df + 5
df2 = df - 2
df3 = df * 1.05
df4 = df/2
print("5 marks added",df1)
print("Subtract 2 marks",df2)
print("Multiply by 1.05",df3)
print("Divide by 2",df4)