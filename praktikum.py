import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('ebay_mens_perfume.csv')
print(df.head())
print(df.info())
print(df.isnull().sum())
print(df.columns)


plt.hist(df['price'], bins=20)
plt.title('Distribusi Harga Parfum')
plt.xlabel('Price')
plt.ylabel('Jumlah Produk')
plt.show()

top_brand = df['brand'].value_counts().head(10)

top_brand.plot(kind='bar')
plt.title('Top 10 Brand')
plt.xticks(rotation=45)
plt.show()


plt.scatter(df['price'], df['sold'])
plt.xlabel('Harga')
plt.ylabel('Terjual')
plt.title('Harga vs Penjualan')
plt.show()


location = df['itemLocation'].value_counts().head(10)

location.plot(kind='barh')
plt.title('Lokasi Terbanyak')
plt.show()


correlation = df[['price', 'sold']].corr()

sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Korelasi Harga vs Penjualan')
plt.show()


