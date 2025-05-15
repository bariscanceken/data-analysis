import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid")
pd.set_option('display.max_rows', None)

file_path = "data.csv"
df = pd.read_csv(file_path, sep="\t")

stress_questions = ['Q6A', 'Q8A', 'Q14A', 'Q15A', 'Q18A', 'Q22A', 'Q25A', 'Q27A', 'Q30A', 'Q35A', 'Q36A', 'Q39A']
df['stress_score'] = df[stress_questions].sum(axis=1)

e_primary = df[df['education'] == 1][['education', 'age', 'stress_score']]
e_secondary = df[df['education'] == 2][['education', 'age', 'stress_score']]
e_highschool = df[df['education'] == 3][['education', 'age', 'stress_score']]
e_university = df[df['education'] == 4][['education', 'age', 'stress_score']]

avg_education_stress_p = e_primary.groupby('education')['stress_score'].mean()
avg_education_stress_s = e_secondary.groupby('education')['stress_score'].mean()
avg_education_stress_h = e_highschool.groupby('education')['stress_score'].mean()
avg_education_stress_u = e_university.groupby('education')['stress_score'].mean()


print(avg_education_stress_p,"\n\n\n",avg_education_stress_s,"\n\n\n",avg_education_stress_h,"\n\n\n",avg_education_stress_u)


