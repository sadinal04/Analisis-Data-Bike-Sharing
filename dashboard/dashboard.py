import numpy as np
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Dapatkan path absolut berdasarkan lokasi file script
base_path = os.path.dirname(__file__)  # Lokasi direktori script ini berada

# Path ke masing-masing file
day_file_path = os.path.join(base_path, "day.csv")
hour_file_path = os.path.join(base_path, "hour.csv")

# Baca file CSV menjadi DataFrame Pandas
df_day = pd.read_csv(day_file_path)
df_hour = pd.read_csv(hour_file_path)

# Mapping kategori
df_day['season'] = df_day['season'].map({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})
df_day['workingday'] = df_day['workingday'].map({0: 'Weekend/Holiday', 1: 'Working Day'})
df_day['year'] = df_day['yr'].map({0: '2011', 1: '2012'})

df_hour['year'] = df_hour['yr'].map({0: '2011', 1: '2012'})

# Streamlit UI
st.title("🚲 **Dashboard Analisis Penyewaan Sepeda**")

# Sidebar untuk filter tahun
st.sidebar.header("🔍 Filter")
tahun_options = ["2011", "2012", "2011-2012"]
tahun = st.sidebar.selectbox("📅 Pilih Tahun:", tahun_options)

# Filter data berdasarkan pilihan tahun
if tahun == "2011-2012":
    df_filtered = df_day
    df_hour_filtered = df_hour
else:
    df_filtered = df_day[df_day["year"] == tahun]
    df_hour_filtered = df_hour[df_hour["year"] == tahun]

# --- VISUALISASI 1: Pengaruh Musim & Hari Kerja ---
with st.container():
    st.subheader("🌦️ Pengaruh Musim & Hari Kerja")
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig, ax = plt.subplots(figsize=(5, 4))
        sns.barplot(x="season", y="cnt", data=df_filtered, estimator=np.mean, color="#1F78B4", ax=ax)
        ax.set_title("Rata-rata Penyewaan Berdasarkan Musim")
        ax.set_xlabel("")
        ax.set_ylabel("Rata-rata Penyewaan")
        st.pyplot(fig)

    with col2:
        fig, ax = plt.subplots(figsize=(5, 4))
        sns.barplot(x="workingday", y="cnt", data=df_filtered, estimator=np.mean, color="#1F78B4", ax=ax)
        ax.set_title("Rata-rata Penyewaan: Hari Kerja vs. Libur")
        ax.set_xlabel("")
        ax.set_ylabel("")
        st.pyplot(fig)

# --- VISUALISASI 2: Penyewaan per Jam ---
with st.container():
    st.subheader("⏰ Rata-rata Penyewaan Sepeda per Jam")
    
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(x="hr", y="cnt", data=df_hour_filtered, estimator=np.mean, errorbar=None, marker="o", color="b")
    ax.set_xticks(range(0, 24))
    ax.set_title("Rata-rata Penyewaan Sepeda per Jam dalam Sehari")
    ax.set_xlabel("Jam")
    ax.set_ylabel("Rata-rata Penyewaan Sepeda")
    ax.grid(True)
    st.pyplot(fig)

# --- VISUALISASI 3: Perbandingan Casual & Registered Users per Hari ---
with st.container():
    st.subheader("📅 Perbandingan Rata-rata Casual & Registered Users per Hari")

    # Mapping hari dalam seminggu
    weekday_mapping = {
        0: "Minggu",
        1: "Senin",
        2: "Selasa",
        3: "Rabu",
        4: "Kamis",
        5: "Jumat",
        6: "Sabtu"
    }

    df_grouped = df_filtered.groupby("weekday")[["casual", "registered"]].mean().reset_index()
    df_grouped["weekday"] = df_grouped["weekday"].replace(weekday_mapping)

    fig, ax = plt.subplots(figsize=(10, 5))
    df_grouped.set_index("weekday").plot(kind="bar", stacked=True, color=["#FFA07A", "#4682B4"], ax=ax)

    ax.set_title("Rata-rata Penyewaan Sepeda per Hari")
    ax.set_xlabel("")
    ax.set_ylabel("Rata-rata Penyewaan Sepeda")
    ax.set_xticklabels(df_grouped["weekday"], rotation=0)
    plt.legend(["Casual", "Registered"], loc="upper right")

    st.pyplot(fig)

# --- VISUALISASI 4: Tren Penyewaan per Tahun ---
with st.container():
    st.subheader("📈 Tren Penyewaan Sepeda per Tahun")

    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(x="year", y="cnt", data=df_day, estimator=np.sum, color="#4682B4", ax=ax)

    ax.set_xlabel("")
    ax.set_ylabel("Total Penyewaan")
    ax.set_title("Tren Penyewaan Sepeda per Tahun")

    st.pyplot(fig)

# --- VISUALISASI 5: Korelasi Cuaca & Penyewaan ---
with st.container():
    st.subheader("🌡️ Korelasi Faktor Cuaca dan Penyewaan Sepeda")

    selected_columns = ["cnt", "temp", "hum", "windspeed"]
    correlation_matrix = df_day[selected_columns].corr()

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5, ax=ax)

    ax.set_title("Heatmap Korelasi Faktor Cuaca & Penyewaan")

    st.pyplot(fig)

# --- VISUALISASI 6: Distribusi Kategori Penyewaan Sepeda ---
with st.container():
    st.subheader("📊 Distribusi Kategori Penyewaan Sepeda")

    df = df_filtered.copy()
    bins = [0, 1000, 3000, df['cnt'].max()]
    labels = ['Low Usage', 'Medium Usage', 'High Usage']

    df['Kategori_Penyewaan'] = pd.cut(df['cnt'], bins=bins, labels=labels)
    category_counts = df['Kategori_Penyewaan'].value_counts().sort_index()

    # Warna khusus untuk kategori "High Usage"
    colors = ["#4682B4", "#4682B4", "#FF4500"]  # Biru untuk Low & Medium, Oranye-merah untuk High Usage

    fig, ax = plt.subplots(figsize=(6, 4))
    category_counts.plot(kind="bar", color=colors, ax=ax)

    ax.set_title("Distribusi Kategori Penyewaan Sepeda")
    ax.set_xlabel("")
    ax.set_ylabel("Jumlah Hari")
    ax.set_xticklabels(labels, rotation=0)
    ax.grid(axis="y", linestyle="--", alpha=0.5)

    st.pyplot(fig)

    # Menambahkan keterangan kategori
    st.markdown("""
    **Keterangan Kategori:**
    - 🟦 **Low Usage**: Penyewaan kurang dari 1000 kali per hari
    - 🟦 **Medium Usage**: Penyewaan antara 1000 - 3000 kali per hari
    - 🟥 **High Usage**: Penyewaan lebih dari 3000 kali per hari
    """)


st.caption('Copyright © Sadinal Mufti 2025')
