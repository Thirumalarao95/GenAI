import pandas as pd
import seaborn as sns   
import matplotlib.pyplot as plt
import numpy as np
student_data = pd.read_csv(r'D:\TuteDude\GenAI\seaborn\student_data.csv')
print(student_data.head(2))


sns.barplot(data=student_data, x="sex", y="G3")
plt.title("Average Final Grade by Gender")
plt.show()

sns.boxplot(data=student_data, x="school", y="G3")
plt.title("Grade Distribution by School")
plt.show()

sns.violinplot(data=student_data, x="sex", y="G3")
plt.title("Grade Distribution by Gender")
plt.show()

sns.countplot(data=student_data, x="sex")
plt.title("Number of Students by Gender")
plt.show()