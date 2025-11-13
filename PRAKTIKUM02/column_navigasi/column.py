import streamlit as st

st.title("columns")
st.write("Kelompok: 1")
st.markdown("""
    - Tria Maulida Sari (0110222300)
    - Nama (NIM)
    - Nama (NIM)
""")

col1, col2 = st.columns(2)

col1.write("Ini adalah kolom pertama")
col1.image("praktikum01/assets/img1.jpg")
col2.write("Ini adalah kolom kedua")