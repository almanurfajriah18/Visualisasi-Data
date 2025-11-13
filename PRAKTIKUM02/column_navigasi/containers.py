import streamlit as st

# Header dan informasi kelompok
st.title("Containers")
st.write("**Mata Kuliah:** Visualisasi Data")
st.write("**Dosen:** Imam Haromain, S.Si, M.Kom")
st.markdown("---")

st.subheader("Anggota Kelompok")
st.write("**1. Tria Maulida Sari - 0110222300**")
st.write("**2. Rahma Dian Nurhikma - 0110222082**")
st.write("**3. Alma Nur Fajriah - 0110222222**")

# Masuk ke dalam materi praktikum

import numpy as np
st.title("Container")
with st.container():
    st.write("element Inside Container")
    # Defining Chart Element
    st.line_chart(np.random.randn(40, 4))
    st.write("Element Outside Container")

# Menggunkan fungsi container.write()

st.title("Out of Order Container")
# Defining Containers
container_one = st.container()
container_one.write("Element One Inside Container")
st.write("Element Outside Container")
# Now insert few more elements in the container_one
container_one.write("Element Two Inside Container")
container_one.line_chart(np.random.randn(40, 4))