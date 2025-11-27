import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Jurusan': ['Ilmu Komputer', 'Sistem Informasi', 'Teknik Informatika', 'Data Science'],
    'Jumlah Mahasiswa': [120, 150, 100, 80]
}
df = pd.DataFrame(data)

# Streamlit App
st.title("Basic Bar Chart - Jumlah Mahasiswa per Jurusan")
st.bar_chart(df.set_index('Jurusan'))

############################################

# Streamlit App
st.title("Basic Bar Chart Menggunakan Matplotlib")

fig, ax = plt.subplots()
ax.bar(data['Jurusan'], data['Jumlah Mahasiswa'], color='skyblue')
ax.set_title('Jumlah Mahasiswa per Jurusan')
ax.set_xlabel('Jurusan')
ax.set_ylabel('Jumlah Mahasiswa')

st.pyplot(fig)

############################################

st.title("Kustomisasi Basic Bar Chart")

fig, ax = plt.subplots()
colors = ['blue', 'green', 'orange', 'purple']
bars = ax.bar(data['Jurusan'], data['Jumlah Mahasiswa'], color=colors)
ax.set_title('Jumlah Mahasiswa per Jurusan')
ax.set_xlabel('Jurusan')
ax.set_ylabel('Jumlah Mahasiswa')

# Menambahkan nilai pada batang
for bar in bars:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5,
            str(bar.get_height()), ha='center')

st.pyplot(fig)

############################################

st.title("Multiple Basic Bar Chart")

# Data tambahan
data_2023 = [120, 150, 100, 80]
data_2024 = [140, 160, 110, 90]

x = range(len(data['Jurusan']))
width = 0.4

fig, ax = plt.subplots()
ax.bar(x, data_2023, width=width, label='2023', color='skyblue')
ax.bar([p + width for p in x], data_2024, width=width, label='2024', color='orange')

ax.set_title('Jumlah Mahasiswa per Jurusan (2023 vs 2024)')
ax.set_xlabel('Jurusan')
ax.set_ylabel('Jumlah Mahasiswa')
ax.set_xticks([p + width / 2 for p in x])
ax.set_xticklabels(data['Jurusan'])
ax.legend()

st.pyplot(fig)


############################################