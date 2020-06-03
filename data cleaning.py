# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 20:56:39 2020

@author: Edward Liang
"""

import pandas as pd

df =pd.read_csv('C:/Users/Edward Liang/Documents/ds_salary_proj/glassdoor_jobs.csv')

# salary pasing



df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['employer_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary' in x.lower() else 0)


df = df[df['Salary Estimate'] != '-1']
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_Kd = salary.apply(lambda x: x.replace('K', '').replace('$', ''))

min_hr = minus_Kd.apply(lambda x: x.lower().replace('per hour', '').replace('employer provided salary:','') )

df['min_salary'] = min_hr.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = min_hr.apply(lambda x: int(x.split('-')[1]))

df['avg_salary'] = (df.min_salary + df.max_salary)/2

# Company name text only

df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] < 0 else x['Company Name'][:-3], axis =1)


# state field
df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1])
df['job_state'].value_counts()
df.columns
df['same_state'] = df.apply(lambda x: 1 if x['Location'] == x['Headquarters'] else 0, axis = 1)


# age of company
df['age'] = df['Founded'].apply(lambda x: x if x < 1 else 2020 - x)


# parsing of job desc (python, etc.)

df['Job Description'][0]

#Python
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
#r Studio
df['r_yn'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() else 0)


#Spark
df['spark_yn'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)

#aws
df['aws_yn'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)

#azure
df['azure_yn'] = df['Job Description'].apply(lambda x: 1 if 'azure' in x.lower() else 0)

#sql
df['sql_yn'] = df['Job Description'].apply(lambda x: 1 if 'sql' in x.lower() else 0)

#machine learning
df['ml_yn'] = df['Job Description'].apply(lambda x: 1 if 'machine learning' in x.lower() else 0)



df_out = df.drop(['Unnamed: 0'], axis = 1)

df_out.to_csv('C:/Users/Edward Liang/Documents/ds_salary_proj/salary_data_cleaned.csv', index = False)





