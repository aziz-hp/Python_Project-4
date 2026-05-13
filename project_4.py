## 1. Ma'lumotlar To'plamini Tayyorlash
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

## Dataset yaratish
data = {
    'Yil': [2018, 2019, 2020, 2021, 2022, 2023],
    'YaIM_mlrd_USD': [52.8, 59.9, 60.2, 69.6, 80.4, 90.8],
    'Aholi_mln': [32.6, 33.2, 33.9, 34.6, 35.4, 36.4],
    'Eksport_mlrd_USD': [14.0, 17.5, 15.1, 16.6, 19.3, 24.4],
    'Import_mlrd_USD': [19.5, 24.3, 20.0, 25.5, 30.7, 38.1],
    'Inflyatsiya_foiz': [14.3, 15.2, 11.1, 10.0, 12.3, 8.8]
}

df = pd.DataFrame(data)
print(df)

## 2. Python Analitikalari
## A. YaIM O'sish Dinamikasi (Line Plot)
plt.figure(figsize=(10, 5))
sns.lineplot(data=df, x='Yil', y='YaIM_mlrd_USD', marker='o', color='green')
plt.title("O'zbekiston YaIM o'sish dinamikasi (2018-2023)")
plt.ylabel("YaIM (mlrd USD)")
plt.grid(True)
plt.show()

## B. Tashqi Savdo Balansi (Bar Chart)
df[['Yil', 'Eksport_mlrd_USD', 'Import_mlrd_USD']].set_index('Yil').plot(kind='bar')
plt.title("Eksport va Import solishtirmasi")
plt.ylabel("Milliard USD")
plt.xticks(rotation=0)
plt.show()

## C. Aholi Jon Boshiga YaIM (Feature Engineering)
df['YaIM_per_capita'] = (df['YaIM_mlrd_USD'] / df['Aholi_mln']) * 1000
print(df[['Yil', 'YaIM_per_capita']])

## D. Korrelyatsiya Matritsasi (Heatmap)
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Ko'rsatkichlar o'rtasidagi korrelyatsiya")
plt.show()

## E. Inflyatsiya Trendi (Scatter Plot)
plt.figure(figsize=(8, 4))
sns.scatterplot(data=df, x='Yil', y='Inflyatsiya_foiz', size='Inflyatsiya_foiz', hue='Inflyatsiya_foiz', palette='Reds')
plt.title("Inflyatsiya darajasi o'zgarishi (%)")
plt.show()

## F. Statistik Tavsif (Descriptive Statistics)
summary = df.describe()
print(summary)