import pandas as pd
import seaborn as sns   
import matplotlib.pyplot as plt
import numpy as np
student_data = pd.read_csv(r'D:\TuteDude\GenAI\seaborn\student_data.csv')
print(student_data.head(2))


g = sns.FacetGrid(student_data, col="sex")  # split by gender
g.map(sns.scatterplot, "studytime", "G3")
plt.show()

g = sns.FacetGrid(student_data, row="school")
g.map(sns.scatterplot, "studytime", "G3")
plt.show()

sns.relplot(data=student_data, x="studytime", y="G3", hue="sex", col="school")
plt.show()

sns.catplot(data=student_data, x="sex", y="G3", kind="box", col="school")
plt.show()

sns.displot(data=student_data, x="G3", col="sex", kde=True)
plt.show()