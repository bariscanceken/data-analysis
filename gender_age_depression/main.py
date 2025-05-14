#Libraries
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid")

file_path = "gender_age_depression/data.csv"
df = pd.read_csv(file_path, sep="\t")

depression_question = ['Q3A', 'Q5A', 'Q10A', 'Q13A', 'Q16A', 'Q17A', 'Q21A','Q24A', 'Q26A', 'Q31A', 'Q34A', 'Q37A', 'Q38A', 'Q42A']

df['depression_score'] = df[depression_question].sum(axis=1)

df_male = df[(df['gender'] == 1) & (df['age'] < 100)][['gender', 'age', 'depression_score']]

df_female = df[(df['gender'] == 2) & (df['age'] < 100)][['gender', 'age', 'depression_score']]


avg_depression_age_female = df_female.groupby('age')['depression_score'].mean()
avg_depression_age_male = df_male.groupby('age')['depression_score'].mean()

plt.bar(avg_depression_age_female.index,avg_depression_age_female.values)
plt.xlabel('age')
plt.ylabel('depression_score')
plt.title('for woman age and depression_score average')
plt.show()

print(avg_depression_age_female)