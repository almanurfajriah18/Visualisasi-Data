import streamlit as st
import pandas as pd
import numpy as np 

# Header dan informasi kelompok
st.title("MAP")
st.write("**Mata Kuliah:** Visualisasi Data")
st.write("**Dosen:** Imam Haromain, S.Si., M.Kom.")
st.markdown("---")

st.subheader("Anggota Kelompok:")
st.write("**1. Tria Maulida Sari - 0110222300**")
st.write("**2. Alma Nur Fajriah - 0110222222**")
st.write("**3. Rahma Dian Nurhikma - 0110222082**")
st.markdown("---")

#Masuk ke dalam materi praktikum
df = pd.DataFrame(
    np.random.randn(50, 2)/[10,10] + [15.4589, 75.0078],
    columns=["latitude","longtitude"]
)

df.rename(columns={'longtitude': 'longitude'}, inplace=True)
st.map(df)

