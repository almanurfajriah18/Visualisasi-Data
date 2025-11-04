import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt

# Konfigurasi halaman
st.set_page_config(
    page_title="2. Data Elements",
    layout="centered"
)

# Header dan informasi kelompok
st.title("2. Data Elements")
st.write("**Mata Kuliah:** Visualisasi Data")
st.write("**Dosen:** Imam Haromain, S.Si., M.Kom.")

st.subheader("Anggota Kelompok:")
st.write("**1. Tria Maulida Sari - 0110222300**")
st.write("**2. Alma Nur Fajriah - 0110222222**")
st.write("**3. Rahma Dian Nurhikma - 0110222082**")

st.markdown("---")

# Pendahuluan
st.write('Data element dalam Streamlit adalah komponen yang digunakan untuk menampilkan berbagai jenis data secara interaktif di aplikasi Streamlit.')

# Data Frame Dasar
st.header("Data Frame")
st.write('Dibawah ini adalah data frame dengan data acak')

# Membuat data frame dengan data acak
df = pd.DataFrame(
    np.random.randn(30, 10),
    columns=('col_no %d' % i for i in range(10)))

# Menampilkan dataframe
st.dataframe(df) 

# Highlighting minimum value
st.header("Highlight Minimum Value di Dataframe")
st.dataframe(df.style.highlight_min(axis=0))

# Tabel statis
st.header("Tabel Statis")
st.table(df.head(10))

# Metrics
st.header("Metrics")
st.metric(label="Temperature", value="31 C", delta="1.2 C")

# Metrics dalam columns
c1, c2, c3 = st.columns(3)
c1.metric("Rainfall", "100 cm", "10 cm")
c2.metric(label="Population", value="123 Billions", delta="1 Billions", delta_color="inverse")
c3.metric(label="Customers", value=100, delta=10, delta_color="off")

# Metrics tambahan
st.metric(label="Speed", value=None, delta=0)
st.metric("Trees", "91456", "-1132649")

# Fungsi write sebagai superfunction
st.header("The write() Function as a Superfunction")
st.write('Here is our Data', df.head(5), 'Data is in dataframe format.\n', "\nWrite is Super function")

# Chart dengan Altair
st.header("Chart dengan Altair")
df_chart = pd.DataFrame(
    np.random.randn(10, 2),
    columns=['a', 'b'])
chart = alt.Chart(df_chart).mark_bar().encode(
    x='a', 
    y='b', 
    tooltip=['a', 'b'])
st.write(chart)

# Magic Commands
st.header("Magic Commands")

# Math calculations dengan magic
"Adding 5 & 4 =", 5+4

# Displaying variable dengan magic
a = 5
'a', a

# Markdown dengan magic
"""
# Magic Feature
Markdown working without defining its function explicitly.
"""

# Dataframe dengan magic
df_magic = pd.DataFrame({'col': [1, 2]})
'dataframe', df_magic

# Chart dengan matplotlib dan magic
st.header("Chart dengan Matplotlib")
s = np.random.logistic(10, 5, size=5)
fig, ax = plt.subplots()
ax.hist(s, bins=15)
"chart", fig