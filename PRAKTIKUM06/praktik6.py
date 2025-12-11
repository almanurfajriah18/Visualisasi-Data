#import
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#header
st.write("**Mata Kuliah:** Visualisasi Data")
st.write("**Dosen:** Imam Haromain, S.Si, M.Kom")
st.markdown("---")

st.subheader("Anggota Kelompok")
st.write("**1. Alma Nur Fajriah - 0110222222**")
st.write("**2. Tria Maulida Sari - 0110222300**")
st.write("**3. Rahma Dian Nurhikma - 0110222082**")

# dataset
stores = ['Store A','Store B','Store C']
male = [150, 200, 180]
famela = [120, 230, 170]

# data transaksi penjualan
stores = ['Store A','Store B','Store C']
product_a = [200, 250, 300]
product_b = [150, 300, 200]

#data quarter
q1_male = [150, 180, 160]
q1_famela = [140, 200, 180]
q2_male = [170, 190, 175]
q2_famela = [130, 210, 160]

# 1 grafik stacked vertical bar chart
st.subheader("1. stacked vertical bar chart")

fig, ax = plt.subplots()
x = np.arange(len(stores))
ax.bar(x, male, label='Male', color='blue')
ax.bar(x, famela, bottom=male, label='Famela', color='pink')  # Fixed: bottom=male not bottom='Male'

ax.set_title('Population by gender and store')
ax.set_xlabel('Stores')
ax.set_ylabel('Population')
ax.set_xticks(x)
ax.set_xticklabels(stores)  # Fixed: set_xticklabels not set_xticklabel
ax.legend()
st.pyplot(fig) 


st.markdown("---")


# 2 grafik stacked vertical bar chart
st.subheader("2. grafik stacked vertical bar chart")

fig, ax = plt.subplots()
x = np.arange(len(stores))
ax.bar(x, product_a, label='Product A', color='blue')
ax.bar(x, product_b, bottom=product_a, label='Product B', color='green')  # Fixed: bottom=product_a not bottom='product_a'

ax.set_title('Sales Transaction by store')
ax.set_xlabel('Stores')
ax.set_ylabel('Sales')
ax.set_xticks(x)
ax.set_xticklabels(stores)  # Fixed: set_xticklabels not set__xticklabel
ax.legend()

st.pyplot(fig) 


st.markdown("---")


# 3 Grafik Kustomisasi stacked vertical bar chart
st.subheader("3. Grafik Kustomisasi stacked vertical bar chart")

# Create a new figure for customization
fig3, ax3 = plt.subplots()
x = np.arange(len(stores))

# Plot the bars
bars1 = ax3.bar(x, product_a, label='Product A', color='blue')
bars2 = ax3.bar(x, product_b, bottom=product_a, label='Product B', color='green')

# Add text labels
for i in range(len(x)):
    # Text for Product A (first bar segment)
    ax3.text(x[i], product_a[i]/2, str(product_a[i]), ha='center', va='center', color='white', fontweight='bold')
    # Text for Product B (second bar segment)
    ax3.text(x[i], product_a[i] + product_b[i]/2, str(product_b[i]), ha='center', va='center', color='black', fontweight='bold')

ax3.set_title('Sales Transaction by store with Labels')
ax3.set_xlabel('Stores')
ax3.set_ylabel('Sales')
ax3.set_xticks(x)
ax3.set_xticklabels(stores)
ax3.legend()

st.pyplot(fig3)


st.markdown("---")


# 4 Grafik Multiple Stacked vertical bar chart
st.subheader("4. Grafik Multiple Stacked vertical bar chart")

fig, ax = plt.subplots()
width = 0.35  # Slightly narrower width for better separation
x = np.arange(len(stores))

# Quarter 1 bars (positioned to the left)
ax.bar(x - width/2, q1_male, label='Q1 Male', color='lightblue', width=width)
ax.bar(x - width/2, q1_famela, bottom=q1_male, label='Q1 Famela', color='lightpink', width=width)

# Quarter 2 bars (positioned to the right)
ax.bar(x + width/2, q2_male, label='Q2 Male', color='blue', width=width)
ax.bar(x + width/2, q2_famela, bottom=q2_male, label='Q2 Famela', color='hotpink', width=width)

ax.set_title('Population by gender and store (Multiple Quarters)')
ax.set_xlabel('Stores')
ax.set_ylabel('Population')
ax.set_xticks(x)
ax.set_xticklabels(stores)  # Fixed: set_xticklabels not set_xticklabel
ax.legend()
st.pyplot(fig)