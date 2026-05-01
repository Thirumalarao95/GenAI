#importing all the packages which are required for my project
import sqlite3
import pandas as pd

#Establisinhg the Database connection to connect with my Database
conn = sqlite3.connect("D:\TuteDude\GenAI\MachineLearning\sample.db")

#reading the data from the database and storing it into DatFrame
Emp_df = pd.read_sql("select * from employees",conn)
#Closing the Database connection
conn.close()
#print the result dataframe
print("Employees Data :", Emp_df)