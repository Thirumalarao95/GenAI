#importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import sklearn
#Reading Data from the JSON file into DataFrame 
json_data = pd.read_json('D:\TuteDude\GenAI\MachineLearning\iris.json')
#Printing the DataFrame
print(json_data)