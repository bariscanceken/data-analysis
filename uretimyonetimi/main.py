#Kütüphaneler
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from math import sqrt
sns.set(style="whitegrid")


# 12 aylık satış verileri
urun_satislari = {
    'adet':   [60, 66, 74, 95, 116, 124, 172, 286, 319, 375, 746, 863],
    'ciro_b': [33078, 36445, 42789, 56763, 56131, 64621, 120936, 167359, 212020, 260622, 517036, 605446],
    'ciro_n': [25348, 26335, 31600, 39944, 43954, 52011, 90410, 133848, 165376, 202777, 431717, 484629]
}

# Aylar
aylar = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"]

#DataFrame haline getirme
df = pd.DataFrame(urun_satislari)
df["Ay"] = aylar
print(df)

#Korelasyon Analizi
numeric_df = df.select_dtypes(include=['number'])
corr_matrix = numeric_df.corr()
sns.heatmap(corr_matrix, annot=True)
plt.show()

#Tahminleme ve Görüntüleme için Linear Regression 
linear_reg = LinearRegression()
x = df.index.values.reshape(-1,1)
y = df['ciro_n'].values.reshape(-1,1)
linear_reg.fit(x,y)
aylar = []
for i in range(0,13):
    aylar.append(i)
array = np.array(aylar).reshape(-1,1)
plt.scatter(x,y,alpha = 0.5)
plt.xlabel("Aylar")
plt.ylabel("Net Ciro")
y_head = linear_reg.predict(array)
plt.plot(array,y_head,color = "red")
plt.show()

#Değerlendirme
#mae Ortalama Mutlak Hata
y_head = linear_reg.predict(x)
mae = mean_absolute_error(y, y_head)
print("Model her ay ortalama:" ,mae,"sapıyor.")
n = 40 # hangi ayı tahmin etmek istiyorsak
print(f"{n}. ayda ciro_n:",linear_reg.predict([[n]]),"bekleniyor.")
