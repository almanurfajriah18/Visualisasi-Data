import streamlit as st
import pandas as pd
import numpy as np #untuk data acak

# Header dan informasi kelompok
st.title("Area Chart")
st.write("**Mata Kuliah:** Visualisasi Data")
st.write("**Dosen:** Imam Haromain, S.Si., M.Kom.")
st.markdown("---")

st.subheader("Anggota Kelompok:")
st.write("**1. Tria Maulida Sari - 0110222300**")
st.write("**2. Alma Nur Fajriah - 0110222222**")
st.write("**3. Rahma Dian Nurhikma - 0110222082**")
st.markdown("---")

#Masuk ke dalam materu praktikum
df = pd.DataFrame(
    np.random.rand(40,4),
    columns=["C1","C2","C3","C4"]
)

st.area_chart(df)

