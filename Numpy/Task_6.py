import numpy as np
marks = np.array([78,85,90,66,72,88,95,60])
print(np.sort(marks))
print(np.percentile(marks, 25))
print(np.percentile(marks, 50))
print(np.percentile(marks, 75))
mean = np.mean(marks)
print("Mean:", mean)
count = marks[marks > mean]
print("Students Scored greater than Average:", count)