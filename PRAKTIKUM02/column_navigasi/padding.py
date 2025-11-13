import streamlit as st

# Header dan informasi kelompok
st.title("Columns with Padding")
st.write("**Mata Kuliah:** Visualisasi Data")
st.write("**Dosen:** Imam Haromain, S.Si, M.Kom")
st.markdown("---")

st.subheader("Anggota Kelompok")
st.write("**1. Tria Maulida Sari - 0110222300**")
st.write("**2. Rahma Dian Nurhikma - 0110222082**")
st.write("**3. Alma Nur Fajriah - 0110222222**")

# Masuk ke dalam materi praktikum

from PIL import Image
img = Image.open('../../PRAKTIKUM01/assets/img2.jpg')
st.title("Padding")

# Defining Padding with columns
col1, padding, col2 = st.columns((10, 2, 10))
with col1:
    col1.image(img)
with col2:
    col2.image(img)