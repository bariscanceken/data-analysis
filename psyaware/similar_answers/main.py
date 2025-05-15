import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid")
pd.set_option('display.max_rows', None)

file_path = "data.csv"
df = pd.read_csv(file_path, sep="\t")

all_questions = [col for col in df.columns if col.startswith('Q') and col.endswith('A')]

same_answer_counts = {}

for q in all_questions:
    most_common_count = df[q].value_counts().max()  # en çok tekrar eden cevap sayısı
    same_answer_counts[q] = most_common_count

sorted_questions = sorted(same_answer_counts.items(), key=lambda x: x[1], reverse=True)

print("En çok aynı cevabı alan sorular ve tekrar sayıları:")
for question, count in sorted_questions:
    print(f"{question}: {count} kez")