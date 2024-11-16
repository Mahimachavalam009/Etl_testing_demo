# Etl_testing_demo
ETL testing 

This is a demo project for live ETL testing


#Use-Case Scenario : A companies HR wants to get a few details of the current employees as a report, the job of the tester to get the report done within the deadline and to meet the HR requirements


```bash
Requirements : 1) the employee data is stored in a csv raw file 
                 need to used the ETL practices to extract, transform and load the dataset
                
                
                 
              
               2) the HR wants the dataset in a few requirements as follows : A. extract the data from employee_csv
                                                                              B. now select the dept_no = 10 and get the data of only those employees that belong to 
                                                                                 the particular dept.
                                                                              C. change the emp_names of the details to uppercase
                                                                              D. now create a new column which says "tot_salary"
                                                                                 where tot_salary = salary + commission
                                                                              E. now load the new data into a new file
                                                                              name it as target_csv
                                                                            
                                                                              
