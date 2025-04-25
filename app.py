import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Data bawaan
df = pd.DataFrame({
    'Kategori': ['Elektronik', 'Pakaian', 'Makanan', 'Minuman', 'Perabotan'],
    'Penjualan': [150, 100, 200, 180, 120],
    'Stok': [30, 50, 70, 40, 20]
})

st.title("📊 Dashboard Penjualan & Stok Produk")

# Input Judul dari User
judul = st.text_input("Masukkan judul grafik", "Grafik Penjualan Produk")

# Pilih kolom angka
kolom = st.selectbox("Pilih data yang ingin divisualisasikan", ['Penjualan', 'Stok'])

# Slider untuk skala
faktor = st.slider("Perbesar nilai", 1, 10, 1)

# Tampilkan DataFrame
if st.checkbox("Tampilkan Data"):
    st.dataframe(df)

# Hitung kolom baru
df['Hasil x Faktor'] = df[kolom] * faktor

# Visualisasi
fig, ax = plt.subplots()
df.plot(kind='bar', x='Kategori', y='Hasil x Faktor', ax=ax)
ax.set_title(judul)
st.pyplot(fig)
