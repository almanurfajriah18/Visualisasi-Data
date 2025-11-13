import streamlit as st

# Header dan informasi kelompok
st.title("Sidebar")
st.write("**Mata Kuliah:** Visualisasi Data")
st.write("**Dosen:** Imam Haromain, S.Si, M.Kom")
st.markdown("---")

st.subheader("Anggota Kelompok")
st.write("**1. Tria Maulida Sari - 0110222300**")
st.write("**2. Rahma Dian Nurhikma - 0110222082**")
st.write("**3. Alma Nur Fajriah - 0110222222**")

# Masuk ke dalam materi praktikum

# Sidebar
st.sidebar.title("Sidebar")
st.sidebar.radio("Are you a New User", ["Yes", "No"])
st.sidebar.slider("Select a Number", 0, 10)