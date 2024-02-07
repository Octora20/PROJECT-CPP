# Import library
import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("data.csv")

# Menampilkan lima baris pertama data
print(data.head())

# Deskripsi statistik singkat dari data
print(data.describe())

# Visualisasi data (contoh: histogram)
plt.hist(data["Usia"], bins=30, color='red', edgecolor='black')
plt.xlabel("Usia")
plt.ylabel("Jumlah Manusia")
plt.title("Histogram Usia")
plt.show()
