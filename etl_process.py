#ETL - Extract, Transform and load
#this is a part of the manual testing as well as automation testing, this is a branch of testing

import pandas as pd
import pytest


#we have to make sure to pass 3 Quality test cases respectively
#step- 1 to extract the data from csv to py file

#step- 2 to convert the data's of employee names to uppercase

#step- 3 to load the salary 
#tot_salary = salary + commission 

#step- 4 to load the new data to target.csv

#here the ETL testing process is taking place

df = pd.read_csv('employee.csv').Uppercase 

#*we have to basically collect the dept_no 10 details of the employees from the raw data
df = df[['dept_no'] == 10]
#test_etl.py


df = new_colummn
new_column = tot_salary
tot_salary = commision + salary
