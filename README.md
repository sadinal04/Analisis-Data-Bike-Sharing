# 🚲 Analisis Data Bike Sharing Dashboard

![Python](https://img.shields.io/badge/Python-3.9-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red?logo=streamlit)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![License](https://img.shields.io/badge/License-MIT-green)

## 📖 Deskripsi

Proyek ini merupakan implementasi **Data Analysis** menggunakan **Bike Sharing Dataset** untuk mengeksplorasi pola penggunaan layanan bike sharing berdasarkan musim, waktu, cuaca, dan tipe pengguna.

Analisis dilakukan menggunakan **Exploratory Data Analysis (EDA)**, kemudian hasilnya divisualisasikan melalui **dashboard interaktif berbasis Streamlit** sehingga insight dapat dipahami dengan lebih mudah.

---

## 🎯 Tujuan Proyek

- Melakukan data cleaning dan preprocessing.
- Mengeksplorasi pola penyewaan sepeda berdasarkan berbagai faktor.
- Menjawab business questions menggunakan EDA.
- Membangun dashboard interaktif menggunakan Streamlit.
- Menyajikan insight yang dapat membantu pengambilan keputusan berbasis data.

---

## 📊 Key Insights

- 🍂 **Fall (Autumn)** merupakan musim dengan jumlah penyewaan tertinggi.
- 🌱 **Spring** memiliki rata-rata penyewaan paling rendah.
- 🚴 Jam sibuk terjadi pada **07.00–09.00** dan **17.00–19.00**, menunjukkan pola penggunaan untuk aktivitas bekerja.
- 👥 **Registered Users** mendominasi jumlah penyewaan dengan korelasi yang sangat tinggi terhadap total rental.
- 📈 Jumlah penyewaan meningkat sekitar **64.8%** dari tahun 2011 ke 2012.
- 🌤️ Suhu berpengaruh positif terhadap jumlah penyewaan, sedangkan kelembaban dan kecepatan angin memiliki pengaruh negatif.
- 📅 Sebagian besar hari termasuk kategori **High Usage**, menunjukkan tingginya tingkat pemanfaatan layanan.

---

## 🛠️ Teknologi

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Streamlit
- Jupyter Notebook

---

## 📂 Struktur Project

```
Analisis-Data-Bike-Sharing/
│
├── dashboard.py
├── Bike_Sharing_Analysis.ipynb
├── requirements.txt
├── README.md
├── data/
│   ├── day.csv
│   └── hour.csv
│
└── assets/
    └── dashboard.png
```

---

## 🚀 Setup Environment

### Menggunakan Anaconda

```bash
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

### Menggunakan Shell / Terminal

```bash
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```

---

## ▶️ Menjalankan Dashboard

```bash
streamlit run dashboard.py
```

---

## 🌐 Live Demo

**Dashboard Streamlit**

https://sadinal04-analisis-data-bike-sharing-dashboarddashboard-l3ldkz.streamlit.app/

---

## 📁 Repository

GitHub

https://github.com/sadinal04/Analisis-Data-Bike-Sharing

---

## 📈 Hasil Proyek

Melalui proyek ini berhasil:

- Membersihkan dan mempersiapkan dataset untuk analisis.
- Menghasilkan insight mengenai perilaku pengguna bike sharing.
- Mengidentifikasi faktor utama yang memengaruhi jumlah penyewaan.
- Mengembangkan dashboard interaktif untuk eksplorasi data secara real-time.
- Menyajikan visualisasi yang informatif untuk mendukung pengambilan keputusan.

---

## 👨‍💻 Author

**Sadinal Mufti**

- GitHub: https://github.com/sadinal04
- LinkedIn: https://www.linkedin.com/in/sadinalmufti/

---
⭐ Jika repository ini bermanfaat, jangan lupa berikan **Star** pada repository ini.
