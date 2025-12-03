"""
After the eda process, there is need to start with cleaning process
import the following to start with cleaning process.

"""
import pandas as pd
import numpy as np

"""
Upload dataset directly from repo

"""
df = pd.read_csv("https://raw.githubusercontent.com/Dee-M123/DM-Project1-Portfolio-HR-Analytics/refs/heads/main/Data/Uncleaned_employees_final_dataset%20(1).csv")

df.head() # as simple check to see if everything is aspected 
df.tail(3) # same goes here 

# Data has already been explored - we can move ahead with cleaning

"""
As we only have two duplicated rows, these can be droped to avoid affecting 
of numerical calculations.

"""

df = df.drop_duplicates()

"""
Cleaning numeric data types to make sure they are uniform
also making sure that categorical columns have no whitespace in them,
like with the duplicates, we do not need inflated columns

"""
# strip whitespace for object (categorical/text) cols
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].astype(str).str.strip()

# convert binary / booly numeric columns to int
df["KPIs_met_more_than_80"] = df["KPIs_met_more_than_80"].astype(int)
df["awards_won"] = df["awards_won"].astype(int)

# ensure numeric columns are numeric
numeric_cols = ["no_of_trainings","age","previous_year_rating","length_of_service","KPIs_met_more_than_80","awards_won","avg_training_score"]
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

"""
Handling missing values

For this specific data set, there are a number of reasons missing values in the education and previous_year_rating column; both are quite relevant, so droping the rows is not an option.  

"""

"""
Every single employe with miss information has exactly one year of service
"""

df[df["previous_year_rating"].isna()]["length_of_service"].describe() # To verify

df["previous_year_rating"].isna().astype(int) # view missing entry 


df["is_new_hire"] = df["previous_year_rating"].isna().astype(int) # missing because they a new hire and have no previous year - hence why a column is created.

df["previous_year_rating"] = df["previous_year_rating"].fillna(0) #filling in the missing data with 0 to denote not applicable 

df = df[['employee_id', 'department', 'region', 'education', 'gender',
       'recruitment_channel', 'no_of_trainings', 'age', 'previous_year_rating','is_new_hire','length_of_service', 'KPIs_met_more_than_80', 'awards_won',
       'avg_training_score']] #restructured the order of the columns 

  
df.head(2) # to view if expectations are meet the change made

"""
For education, we can simply replace nan with unknown, that is still useful information to have for HR analytics

"""
df["education"] = df["education"].fillna("Unknown")

df.isnull().sum() # to verify that all columns have no missing values anymore 

"""
We want to make sure gender is clearly defined with one specific denotation that can not be mistaken, by having uniform letter-casing

"""

df["gender"] = df["gender"].str.lower().replace({"m":"Male","f":"Female","male":"Male","female":"Female"})

df["gender"] # Checking if gender is uniform and in manner understandable by all

""" 
Regional data is unevenly distributed, grouping regions with lower records into samll sub-regions is ideal in this case

"""
region_counts = df["region"].value_counts()
small_regions = region_counts[region_counts < (0.03*len(df))].index  # <3% threshold - as numbers lower than are not enough to have an office space

df["region_grouped"] = df["region"].replace(small_regions, "Other")
df.head() #check if column exists as expected 

df = df[['employee_id', 'department', 'region','region_grouped', 'education', 'gender',
       'recruitment_channel', 'no_of_trainings', 'age', 'previous_year_rating',
       'is_new_hire', 'length_of_service', 'KPIs_met_more_than_80',
       'awards_won', 'avg_training_score']] #restructured the column order

df[['region','region_grouped']].value_counts() # to verify if side by side view tracks 

"""
Checking how to hundle any exisitng outliers, assessing if there is a need to drop them or not.

"""


import matplotlib.pyplot as plt
import seaborn as sns

for col in ["no_of_trainings","age","previous_year_rating","length_of_service","KPIs_met_more_than_80","awards_won","avg_training_score"]:
    plt.figure(figsize=(6,3))
    sns.boxplot(x=df[col])
    plt.title(col)
    plt.show()

# The outliers in this plots can not be dropped as they would be useful in the overall understanding of the data and problem statements

"""
After cleaning all the data, it can be save and uploaded to repo

"""

df.to_csv("cleaned_employees_dataset.csv", index=False) 
