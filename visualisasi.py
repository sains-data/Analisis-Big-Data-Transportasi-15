import pandas as pd
import matplotlib.pyplot as plt

# Load data CSV
df = pd.read_csv(r"C:\bigdata-transjakarta\data\gold_export.csv")

# Isi data preview
print(df.head())

# Ganti nilai kosong di corridorName dengan 'Unknown'
df['corridorName'] = df['corridorName'].fillna('Unknown')

# 1. Bar chart Top 10 durasi terlama
top10 = df.sort_values(by='avgDurationMinutes', ascending=False).head(10)

plt.figure(figsize=(10,6))
plt.bar(top10['corridorName'], top10['avgDurationMinutes'], color='tomato')
plt.xticks(rotation=45, ha='right')
plt.title('Top 10 Koridor dengan Rata-rata Durasi Terlama')
plt.xlabel('Koridor')
plt.ylabel('Durasi (menit)')
plt.tight_layout()
plt.show()

# 2. Histogram distribusi durasi perjalanan
plt.figure(figsize=(8,5))
plt.hist(df['avgDurationMinutes'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribusi Rata-rata Durasi Perjalanan per Koridor')
plt.xlabel('Durasi (menit)')
plt.ylabel('Jumlah Koridor')
plt.tight_layout()
plt.show()

# 3. Boxplot durasi perjalanan
plt.figure(figsize=(6,4))
plt.boxplot(df['avgDurationMinutes'].dropna())
plt.title('Boxplot Rata-rata Durasi Perjalanan Koridor')
plt.ylabel('Durasi (menit)')
plt.tight_layout()
plt.show()

# 4. Barplot rata-rata durasi per grup corridorID (awalan)
df['corridorGroup'] = df['corridorID'].astype(str).str.extract(r'(^[A-Za-z0-9]+)')
grouped = df.groupby('corridorGroup')['avgDurationMinutes'].mean().reset_index()

plt.figure(figsize=(8,5))
plt.bar(grouped['corridorGroup'], grouped['avgDurationMinutes'], color='mediumseagreen')
plt.title('Rata-rata Durasi Perjalanan per Grup Koridor')
plt.xlabel('Grup Koridor (Awalan corridorID)')
plt.ylabel('Durasi Rata-rata (menit)')
plt.tight_layout()
plt.show()

# 5. Scatter plot durasi vs corridorID numeric (jika memungkinkan)
df['corridorID_num'] = pd.to_numeric(df['corridorID'], errors='coerce')

plt.figure(figsize=(8,5))
plt.scatter(df['corridorID_num'], df['avgDurationMinutes'], alpha=0.7)
plt.title('Scatterplot Durasi vs corridorID (numeric)')
plt.xlabel('corridorID (numeric)')
plt.ylabel('Durasi Rata-rata (menit)')
plt.tight_layout()
plt.show()
