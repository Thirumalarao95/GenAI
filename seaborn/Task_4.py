import pandas as pd
import seaborn as sns   
import matplotlib.pyplot as plt
import numpy as np
student_data = pd.read_csv(r'D:\TuteDude\GenAI\seaborn\student_data.csv')
print(student_data.head(2))

sns.histplot(data=student_data, x="G1", y="G3")
plt.show()

sns.kdeplot(data=student_data, x="G1", y="G3", fill=True)
plt.show()