import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

# ===============================
# LOAD DATA
# ===============================
df = pd.read_csv('data/ecommerce.csv', sep='\t')

print("=== DATA AWAL ===")
print(df.head())

# Pastikan format tanggal
df['Order_Date'] = pd.to_datetime(df['Order_Date'])

# ===============================
# 1. UNDERPERFORMER ANALYSIS
# ===============================

avg_price = df['Price_Per_Unit'].mean()
print("\nRata-rata harga:", avg_price)

high_price = df[df['Price_Per_Unit'] > avg_price]

print("\nProduk harga tinggi:")
print(high_price[['Product_Category', 'Price_Per_Unit', 'Quantity']].head())

# VISUALISASI SCATTER
plt.figure(figsize=(8,5))
plt.scatter(df['Price_Per_Unit'], df['Quantity'])

plt.xlabel('Price Per Unit')
plt.ylabel('Quantity')
plt.title('Produk Mahal vs Jumlah Terjual')

plt.savefig('images/scatter_underperformer.png')
plt.show()

# ===============================
# 2. RFM ANALYSIS
# ===============================

snapshot_date = df['Order_Date'].max() + dt.timedelta(days=1)

rfm = df.groupby('CustomerID').agg({
    'Order_Date': lambda x: (snapshot_date - x.max()).days,
    'Order_ID': 'count',
    'Total_Sales': 'sum'
})

rfm.columns = ['Recency', 'Frequency', 'Monetary']

print("\n=== RFM TABLE ===")
print(rfm.head())

# SCORING
rfm['R_Score'] = pd.qcut(rfm['Recency'], 5, labels=[5,4,3,2,1])
rfm['F_Score'] = pd.qcut(rfm['Frequency'].rank(method='first'), 5, labels=[1,2,3,4,5])
rfm['M_Score'] = pd.qcut(rfm['Monetary'], 5, labels=[1,2,3,4,5])

# GABUNG SKOR
rfm['RFM_Score'] = rfm['R_Score'].astype(str) + rfm['F_Score'].astype(str) + rfm['M_Score'].astype(str)

print("\n=== RFM SCORE ===")
print(rfm.head())

# TOP CUSTOMER
print("\n=== TOP CUSTOMER (Monetary Tertinggi) ===")
print(rfm.sort_values(by='Monetary', ascending=False).head())


# ===============================
# 3. Analisis Kontribusi Kategori 
# ===============================
print("\n=== ANALISIS EFISIENSI KATEGORI ===")

category = df.groupby('Product_Category').agg({
    'Total_Sales': 'sum',
    'Ad_Budget': 'sum'
})

category['Efficiency'] = category['Total_Sales'] / category['Ad_Budget']

# Urutkan dari paling tidak efisien
category_sorted = category.sort_values('Efficiency')

print(category_sorted)

# VISUALISASI BAR HORIZONTAL
plt.figure(figsize=(8,5))

category_sorted['Efficiency'].plot(kind='barh')

plt.title('Efisiensi Kategori (Sales / Ad Budget)')
plt.xlabel('Efficiency')
plt.ylabel('Category')

plt.savefig('images/kategori_efisiensi.png')
plt.show()

# Insight otomatis
print("\nINSIGHT KATEGORI:")
print("- Kategori dengan efisiensi rendah menunjukkan penggunaan iklan yang kurang optimal.")
print("- Kategori dengan efisiensi tinggi memiliki potensi untuk ditingkatkan anggaran iklannya.")

# ===============================
# 4. UJI HIPOTESIS SEDERHANA
# ===============================

print("\n=== UJI HIPOTESIS IKLAN ===")

# 1. Tentukan median
median_ads = df['Ad_Budget'].median()
print(f"Median Ad Budget: {median_ads}")

# 2. Bagi data jadi 2 kelompok
high_ads = df[df['Ad_Budget'] > median_ads]
low_ads = df[df['Ad_Budget'] <= median_ads]

# 3. Hitung rata-rata penjualan
high_mean = high_ads['Total_Sales'].mean()
low_mean = low_ads['Total_Sales'].mean()

print(f"Rata-rata Total Sales (Iklan Tinggi): {high_mean}")
print(f"Rata-rata Total Sales (Iklan Rendah): {low_mean}")

# 4. Jawab pertanyaan
print("\n=== KESIMPULAN HIPOTESIS ===")

if high_mean > low_mean:
    print("Hipotesis DITERIMA:")
    print("Peningkatan Ad_Budget di atas median cenderung meningkatkan Total_Sales.")
else:
    print("Hipotesis DITOLAK:")
    print("Peningkatan Ad_Budget tidak memberikan peningkatan signifikan pada Total_Sales.")
    
plt.figure(figsize=(6,4))

labels = ['Low Ads', 'High Ads']
values = [low_mean, high_mean]

plt.bar(labels, values)

plt.title('Perbandingan Rata-rata Sales')
plt.ylabel('Total Sales')

plt.savefig('images/uji_hipotesis.png')
plt.show()

# ===============================
# 5. PENDALAMAN RFM (SEGMENTASI)
# ===============================
print("\n=== SEGMENTASI PELANGGAN ===")

def segment_customer(row):
    if row['RFM_Score'] == '555':
        return 'VIP'
    elif row['R_Score'] >= 4 and row['F_Score'] >= 4:
        return 'Loyal'
    elif row['R_Score'] <= 2:
        return 'Churn Risk'
    else:
        return 'Regular'

rfm['Segment'] = rfm.apply(segment_customer, axis=1)

print(rfm['Segment'].value_counts())

plt.figure(figsize=(6,4))

rfm['Segment'].value_counts().plot(kind='bar')

plt.title('Distribusi Segment Pelanggan')
plt.xlabel('Segment')
plt.ylabel('Jumlah Pelanggan')

plt.savefig('images/rfm_segment.png')
plt.show()

# ===============================
# 6. REGRESI LINEAR SEDERHANA
# ===============================
# 🔧 FIX DATA
df = df.dropna(subset=['Ad_Budget', 'Total_Sales'])

print("\n=== REGRESI LINEAR ===")

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Feature & Target
X = df[['Ad_Budget']]
y = df['Total_Sales']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = LinearRegression()
model.fit(X_train, y_train)

# Output hasil
coef = model.coef_[0]
r2 = model.score(X_test, y_test)

print(f"Koefisien (Pengaruh Iklan): {coef}")
print(f"R2 Score (Akurasi Model): {r2}")

plt.figure(figsize=(6,4))

plt.scatter(X, y, alpha=0.5, label='Data')

# Garis regresi
plt.plot(X, model.predict(X), color='red', label='Garis Regresi')

plt.xlabel('Ad Budget')
plt.ylabel('Total Sales')
plt.title('Regresi Linear: Iklan vs Penjualan')
plt.legend()

plt.show()
