import pandas as pd
import seaborn as sns   
import matplotlib.pyplot as plt
import numpy as np
student_data = pd.read_csv(r'D:\TuteDude\GenAI\seaborn\student_data.csv')
print(student_data.head(2))

sns.regplot(data=student_data, x="studytime", y="G3")
plt.title("Study Time vs Final Grade")
plt.show()

sns.lmplot(data=student_data, x="studytime", y="G3", hue="sex")
plt.title("Study Time vs Grade by Gender")
plt.show()