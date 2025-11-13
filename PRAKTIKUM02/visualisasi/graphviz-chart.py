import streamlit as st
import pandas as pd
import numpy as np 
import graphviz as graphviz

# Header dan informasi kelompok
st.title("Graphviz Chart")
st.write("**Mata Kuliah:** Visualisasi Data")
st.write("**Dosen:** Imam Haromain, S.Si., M.Kom.")
st.markdown("---")

st.subheader("Anggota Kelompok:")
st.write("**1. Tria Maulida Sari - 0110222300**")
st.write("**2. Alma Nur Fajriah - 0110222222**")
st.write("**3. Rahma Dian Nurhikma - 0110222082**")
st.markdown("---")

#Masuk ke dalam materu praktikum
st.graphviz_chart("""
    digraph {
         "Training Data" -> "ML Algorithm"
         "ML Algorithm" -> "Model"
         "Model" -> "Results Forecasting"        
         "New Data" -> "Model"
         }
""")


