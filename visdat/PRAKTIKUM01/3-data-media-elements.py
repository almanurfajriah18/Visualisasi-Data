import streamlit as st
import base64
from PIL import Image

# Konfigurasi halaman
st.set_page_config(
    page_title="3. Data Media Elements",
    layout="centered"
)

# Header dan informasi kelompok
st.title("3. Data Media Elements")
st.write("**Mata Kuliah:** Visualisasi Data")
st.write("**Dosen:** Imam Haromain, S.Si., M.Kom.")

st.subheader("Anggota Kelompok:")
st.write("**1. Tria Maulida Sari - 0110222300**")
st.write("**2. Alma Nur Fajriah - 0110222222**")
st.write("**3. Rahma Dian Nurhikma - 0110222082**")

st.markdown("---")

# Menampilkan Satu Gambar
st.header("Menampilkan Satu Gambar")
st.image("assets/img1.jpg")
st.write("Image Courtesy: unsplash.com")

# Menampilkan Multiple Gambar
st.header("Menampilkan Multiple Gambar")
animal_images = [
    'assets/img1.jpg',
    'assets/img2.jpg',
    'assets/img3.jpg',
    'assets/img4.jpg',
    'assets/img5.jpg'
]
st.image(animal_images, width=150)
st.write("Image Courtesy: unsplash")

# Background Image Function
def add_local_background_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/jpg;base64,{encoded_string.decode()});
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Background Image
st.header("Background Image")
st.write("Image Courtesy: unsplash")
add_local_background_image("assets/img.jpg")

# Image Manipulation
st.header("Image Manipulation")

# Original Image
st.subheader("Original Image")
original_image = Image.open("assets/img2.jpg")
st.image(original_image)

# Resized Image
st.subheader("Resized Image")
resized_image = original_image.resize((600, 400))
st.image(resized_image)