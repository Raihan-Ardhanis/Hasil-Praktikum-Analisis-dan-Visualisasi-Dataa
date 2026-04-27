# 📊 Analisis Data E-Commerce

## 📌 Deskripsi Proyek

Proyek ini bertujuan untuk menganalisis data transaksi e-commerce guna memahami performa produk, perilaku pelanggan, serta efektivitas strategi pemasaran. Analisis dilakukan menggunakan Python dengan pendekatan data analytics dan machine learning sederhana.

---

## 🎯 Business Questions

1. Apakah produk dengan harga tinggi memiliki volume penjualan yang rendah (*underperformer*)?
2. Siapa pelanggan terbaik berdasarkan analisis RFM (Recency, Frequency, Monetary)?
3. Kategori produk mana yang paling efisien dalam penggunaan anggaran iklan?
4. Apakah peningkatan anggaran iklan berpengaruh terhadap penjualan?
5. Seberapa besar pengaruh Ad_Budget terhadap Total_Sales (regresi linear)?

---

## 🧹 Data Wrangling

Langkah-langkah yang dilakukan:

* Mengubah kolom `Order_Date` ke format datetime
* Memeriksa dan menangani missing values (NaN)
* Mengelompokkan data berdasarkan kebutuhan analisis:

  * CustomerID (RFM)
  * Product_Category (Kategori)
* Menyiapkan dataset untuk analisis statistik dan machine learning

---

## 🔍 Analisis & Hasil

### 1. 📉 Underperformer Analysis

Produk dengan harga di atas rata-rata dianalisis terhadap jumlah penjualan.

📊 Visualisasi: Scatter Plot (Price vs Quantity)

**Insight:**

* Produk dengan harga tinggi cenderung memiliki jumlah pembelian lebih rendah
* Harga yang terlalu tinggi berpotensi menjadi penghambat penjualan

---

### 2. 👥 RFM Analysis (Segmentasi Pelanggan)

Pelanggan dikelompokkan berdasarkan:

* **Recency**: Terakhir transaksi
* **Frequency**: Frekuensi pembelian
* **Monetary**: Total pengeluaran

**Hasil:**

* Ditemukan pelanggan dengan skor tinggi (contoh: 555)
* Pelanggan ini dikategorikan sebagai **VIP**

**Insight:**

* Pelanggan VIP memiliki nilai bisnis tertinggi
* Pelanggan dengan skor rendah berpotensi churn

---

### 3. 📊 Analisis Efisiensi Kategori

Perbandingan:

* Total_Sales vs Ad_Budget per kategori

📊 Visualisasi: Bar Chart Horizontal

**Insight:**

* Tidak semua kategori efisien dalam penggunaan iklan
* Beberapa kategori memiliki biaya iklan tinggi namun penjualan rendah

---

### 4. 🧪 Uji Hipotesis Sederhana

Metode:

* Data dibagi menjadi:

  * Iklan Tinggi (> median)
  * Iklan Rendah (≤ median)
* Dibandingkan rata-rata penjualan

**Hasil:**

* Kelompok dengan iklan tinggi memiliki rata-rata penjualan lebih besar

**Kesimpulan:**

* Iklan memiliki pengaruh terhadap peningkatan penjualan

---

### 5. 📈 Regresi Linear

Model:

* X = Ad_Budget
* y = Total_Sales

**Hasil:**

* Koefisien positif → menunjukkan hubungan positif
* R² Score → menunjukkan kekuatan model dalam menjelaskan data

**Insight:**

* Semakin besar anggaran iklan, semakin tinggi potensi penjualan
* Model dapat digunakan untuk prediksi sederhana

---

## 📌 Visualisasi

Beberapa visualisasi yang dihasilkan:

* Scatter Plot (Underperformer)
* Bar Chart Efisiensi Kategori
* Bar Chart Uji Hipotesis
* Distribusi Segmentasi RFM
* Regresi Linear Plot

---

## 🚀 Recommendation

Berdasarkan hasil analisis:

1. Menurunkan harga atau memberikan promo pada produk yang mahal namun kurang laku
2. Memberikan reward kepada pelanggan VIP untuk meningkatkan loyalitas
3. Mengoptimalkan anggaran iklan pada kategori yang kurang efisien
4. Meningkatkan investasi pada kategori yang memberikan return tinggi
5. Menggunakan model regresi untuk mendukung pengambilan keputusan pemasaran

---

## ⚙️ Teknologi yang Digunakan

* Python
* Pandas
* Matplotlib
* Scikit-learn

---

## ▶️ Cara Menjalankan

```bash
pip install pandas matplotlib scikit-learn
python analisis_kelompok.py
```

---

## 👨‍💻 Penulis

Tugas Kelompok Analisis Data
Nayaka Naufal 'Aziz / 28
Raihan Ardhanis Raharja / 33
