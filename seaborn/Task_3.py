import pandas as pd
import seaborn as sns   
import matplotlib.pyplot as plt
import numpy as np
student_data = pd.read_csv(r'D:\TuteDude\GenAI\seaborn\student_data.csv')
print(student_data.head(2))

sns.histplot(student_data["G3"], bins=15)
plt.show()

sns.kdeplot(student_data["G3"], fill=True)
plt.show()

sns.rugplot(student_data["G3"])
plt.show()

sns.histplot(student_data["G3"], kde=True)
plt.show()