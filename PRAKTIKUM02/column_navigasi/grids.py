import streamlit as st

# Header dan informasi kelompok
st.title("Grids")
st.write("**Mata Kuliah:** Visualisasi Data")
st.write("**Dosen:** Imam Haromain, S.Si, M.Kom")
st.markdown("---")

st.subheader("Anggota Kelompok")
st.write("**1. Tria Maulida Sari - 0110222300**")
st.write("**2. Rahma Dian Nurhikma - 0110222082**")
st.write("**3. Alma Nur Fajriah - 0110222222**")

# Masuk ke dalam materi praktikum
from PIL import Image
img = Image.open('../../PRAKTIKUM01/assets/img3.jpg')
st.title("Grids")

# Defining no of Rows
for a in range (4):
# Defining no. of columns with size
    cols = st.columns((1, 1, 1, 1))
    cols[0].image(img)
    cols[1].image(img)
    cols[2].image(img)  
    cols[3].image(img)