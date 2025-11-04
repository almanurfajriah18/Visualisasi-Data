import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import base64
from PIL import Image
import datetime
import time

# =============================================
# 🎨 KONFIGURASI HALAMAN
# =============================================
st.set_page_config(
    page_title="Nyoba",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =============================================
# 👥 INFORMASI KELOMPOK
# =============================================
st.title("🎨 Praktikum 1 Visualisasi Data")
st.write("**Mata Kuliah:** Visualisasi Data")
st.write("**Dosen:** Imam Haromain, S.Si., M.Kom.")

st.markdown("---")

st.subheader("👥 Anggota Kelompok:")
col1, col2, col3 = st.columns(3)
with col1:
    st.success("**1. Tria Maulida Sari**")
    st.caption("0110222300")
with col2:
    st.info("**2. Alma Nur Fajriah**")
    st.caption("0110222222")
with col3:
    st.warning("**3. Rahma Dian Nurhikma**")
    st.caption("0110222082")

st.markdown("---")

# =============================================
# 📝 BAGIAN 1: TEXT ELEMENTS
# =============================================
st.header("📝 1. Text Elements")
st.write("Berbagai komponen untuk menampilkan teks dengan format yang berbeda")

# Basic Text Elements
st.subheader("🎯 Basic Text Elements")
st.header("Ini Header 🎪")
st.subheader("Ini Subheader 🎭")
st.caption("Ini caption kecil di bawah 🎪")

# Displaying Plain Text
st.subheader("📄 Plain Text")
st.text("Hi, \nWorld\t!")
st.text('Selamat Datang di Streamlit! ✨')

# Displaying Markdown
st.subheader("🎨 Markdown Format")
st.markdown("**Hi, World!** - *Teks miring* - ~~Coret~~")
st.markdown("**Tria Maulida Sari** - *0110222300*")

# Displaying LaTeX
st.subheader("🧮 LaTeX Mathematical Expressions")
col1, col2 = st.columns(2)
with col1:
    st.latex(r'''cos2\theta = 1 - 2sin^2\theta''')
    st.latex("""(a+b)^2 = a^2 + b^2 + 2ab""")
with col2:
    st.latex(r'''\frac{\partial u}{\partial t}
             = h^2 \left( \frac{\partial^2 u}{\partial x^2}
             + \frac{\partial^2 u}{\partial y^2}
             + \frac{\partial^2 u}{\partial z^2} \right)''')

# Displaying Code
st.subheader("💻 Code Display")
col1, col2, col3 = st.columns(3)

with col1:
    st.write("**Python Code**")
    python_code = '''def hello():
    print("Hello, TriaMaul!")'''
    st.code(python_code, language='python')

with col2:
    st.write("**Java Code**")
    java_code = """public class CFG {
    public static void main(String args[]) {
        System.out.println("Hello Tria!");
    }
}"""
    st.code(java_code, language='java')

with col3:
    st.write("**JavaScript Code**")
    js_code = """<p id="demo"></p>
<script>
try {
    addlert("Welcome guest!");
}
catch(err) {
    document.getElementById("demo").innerHTML = err.message;
}
</script>"""
    st.code(js_code, language='javascript')

st.markdown("---")

# =============================================
# 📊 BAGIAN 2: DATA ELEMENTS
# =============================================
st.header("📊 2. Data Elements")
st.write("Komponen untuk menampilkan berbagai jenis data secara interaktif")

# Data Frame Dasar
st.subheader("🎪 Data Frame Interaktif")
df_large = pd.DataFrame(
    np.random.randn(30, 10),
    columns=(f'Kolom_{i}' for i in range(10))
)
st.dataframe(df_large)

# Data Frame dengan Highlight
st.subheader("🎨 Data Frame dengan Highlight")
styled_df = df_large.style.highlight_min(axis=0, color='#FFD700')
st.dataframe(styled_df)

# Tabel Statis
st.subheader("📋 Tabel Statis")
st.table(df_large.head(10))

# Metrics dan KPI
st.subheader("📈 Metrics Cards")
st.metric(label="Temperature 🌡️", value="31 °C", delta="1.2 °C")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Rainfall 🌧️", "100 cm", "10 cm")
with col2:
    st.metric(label="Population 👥", value="123 Billions", delta="1 Billion", delta_color="inverse")
with col3:
    st.metric(label="Customers 🛍️", value=100, delta=10, delta_color="off")

# Metrics Tambahan
st.metric(label="Speed 🚀", value=None, delta=0)
st.metric("Trees 🌳", "91,456", "-1,132,649")

# Super Function Write
st.subheader("🔄 Fungsi write() sebagai Superfunction")
st.write('Berikut data contoh:', df_large.head(5), 'Data dalam format dataframe!\n', "✨ Write adalah fungsi super!")

# Visualisasi dengan Altair
st.subheader("📊 Chart dengan Altair")
df_chart = pd.DataFrame(
    np.random.randn(10, 2),
    columns=['Nilai_A', 'Nilai_B']
)
chart = alt.Chart(df_chart).mark_bar().encode(
    x='Nilai_A', 
    y='Nilai_B', 
    tooltip=['Nilai_A', 'Nilai_B']
).properties(title="Chart Interaktif 🎯")
st.write(chart)

# Magic Commands
st.subheader("✨ Magic Commands")
st.write("Menampilkan output tanpa fungsi Streamlit secara eksplisit")

"Hasil 5 + 4 =", 5+4

nilai_magic = 42
'Nilai magic:', nilai_magic

"""
# 🎩 Fitur Magic
**Markdown bekerja tanpa fungsi!**

- Item list pertama ✨
- Item list kedua 🎉
- Item list ketiiiiga 🎈
"""

df_magic = pd.DataFrame({'Kategori': ['X', 'Y'], 'Nilai': [1, 2]})
'DataFrame Magic:', df_magic

st.markdown("---")

# =============================================
# 🖼️ BAGIAN 3: IMAGE ELEMENTS
# =============================================
st.header("🖼️ 3. Image Elements")
st.write("Menampilkan dan memanipulasi gambar")

# Single Image
st.subheader("🖼️ Menampilkan Satu Gambar")
try:
    st.image("assets/img1.jpg", caption="Gambar Contoh 1 🌟", use_column_width=True)
except:
    st.warning("⚠️ File gambar tidak ditemukan. Pastikan folder 'assets' ada!")

# Multiple Images
st.subheader("🎭 Menampilkan Beberapa Gambar")
try:
    animal_images = ['assets/img1.jpg', 'assets/img2.jpg', 'assets/img3.jpg', 'assets/img4.jpg', 'assets/img5.jpg']
    st.image(animal_images, width=150, caption=[f"Gambar {i+1}" for i in range(5)])
except:
    st.info("🔧 Tambahkan gambar Anda di folder 'assets' untuk melihat demo ini!")

# Image Manipulation
st.subheader("🎨 Manipulasi Gambar")
try:
    original_image = Image.open("assets/img2.jpg")
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Gambar Asli**")
        st.image(original_image, use_column_width=True)
    with col2:
        st.write("**Gambar Di-resize**")
        resized_image = original_image.resize((400, 300))
        st.image(resized_image, use_column_width=True)
except:
    st.warning("⚠️ File gambar untuk manipulasi tidak ditemukan")

st.markdown("---")

# =============================================
# 🎮 BAGIAN 4: INTERACTIVE ELEMENTS
# =============================================
st.header("🎮 4. Interactive Elements")
st.write("Komponen interaktif untuk user input")

# Button
st.subheader("🔄 Button")
button_clicked = st.button('Klik Aku! 🎯')
if button_clicked:
    st.balloons()
    st.success("🎉 Yeay! Anda menekan tombol!")
else:
    st.info("🔘 Tombol belum ditekan")

# Radio Button
st.subheader("📻 Radio Button")
gender = st.radio(
    "Pilih Jenis Kelamin:",
    ('Laki-laki 👨', 'Perempuan 👩', 'Lainnya 🎭')
)
st.write(f"Anda memilih: **{gender}**")

# Checkboxes
st.subheader("☑️ Checkboxes")
st.write("Pilih hobi Anda:")
check1 = st.checkbox('Membaca 📚')
check2 = st.checkbox('Menonton Film 🎬')
check3 = st.checkbox('Olahraga ⚽')
if check1 or check2 or check3:
    st.success("Hobi terpilih! 🎯")

# Dropdown
st.subheader("📋 Dropdown Menu")
hobby = st.selectbox(
    'Pilih Hobi Favorit:',
    ('Membaca 📖', 'Bermain Game 🎮', 'Traveling ✈️', 'Memasak 👨‍🍳')
)
st.write(f"Hobi favorit: **{hobby}**")

# Multi-Select
st.subheader("🎯 Multi-Select")
hobbies = st.multiselect(
    'Apa hobi Anda? (bisa pilih banyak)',
    ['Membaca', 'Memasak', 'Menonton Film/Series', 'Bermain', 'Menggambar', 'Hiking'],
    ['Membaca', 'Bermain']
)
st.write(f"Hobi yang dipilih: **{', '.join(hobbies)}**")

# Progress Bar
st.subheader("📊 Progress Bar")
if st.button("Mulai Download 🚀"):
    download_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.02)
        download_bar.progress(percent_complete + 1)
    st.success("✅ Download Selesai!")

# Spinner
st.subheader("⏳ Spinner")
if st.button("Tunggu Sebentar..."):
    with st.spinner('Loading... Harap tunggu 🕒'):
        time.sleep(3)
    st.success('🎉 Selesai! Halo Data Scientists!')

st.markdown("---")

# =============================================
# 📝 BAGIAN 5: INPUT ELEMENTS
# =============================================
st.header("📝 5. Input Elements")
st.write("Berbagai jenis input dari user")

# Text Input
st.subheader("📝 Text Input")
name = st.text_input("Masukkan nama Anda:")
if name:
    st.write(f"Halo, **{name}**! 👋")

# Text Area
st.subheader("📄 Text Area")
review = st.text_area("Tulis review Anda:")
if review:
    st.write("Review Anda:", review)

# Number Input
st.subheader("🔢 Number Input")
number = st.number_input(
    "Masukkan angka (0-10):",
    min_value=0,
    max_value=10,
    value=5,
    step=2
)
st.write(f"Angka yang dipilih: **{number}**")
st.caption("Min: 0, Max: 10, Default: 5, Step: 2")

# Date and Time
st.subheader("📅 Date & Time Input")
col1, col2 = st.columns(2)
with col1:
    selected_time = st.time_input("Pilih waktu:")
with col2:
    selected_date = st.date_input(
        "Pilih tanggal:",
        value=datetime.date(2024, 1, 1),
        min_value=datetime.date(1970, 1, 1),
        max_value=datetime.date(2024, 12, 31)
    )

# Color Picker
st.subheader("🎨 Color Picker")
selected_color = st.color_picker("Pilih warna favorit:")
st.write(f"Warna yang dipilih: **{selected_color}**")
st.markdown(f'<div style="background-color:{selected_color}; padding: 20px; border-radius: 10px; color: white; text-align: center;">Warna Pilihan Anda ✨</div>', unsafe_allow_html=True)

# File Uploader
st.subheader("📤 File Uploader")
uploaded_file = st.file_uploader("Upload file CSV", type=["csv"])
if uploaded_file is not None:
    file_details = {
        "Nama File": uploaded_file.name,
        "Tipe File": uploaded_file.type,
        "Ukuran File": f"{uploaded_file.size} bytes"
    }
    st.write("📋 Detail File:")
    st.json(file_details)
    
    df_uploaded = pd.read_csv(uploaded_file)
    st.write("📊 Preview Data:")
    st.dataframe(df_uploaded.head())

# Form
st.subheader("📝 Form Terstruktur")
with st.form(key='my_form'):
    st.write("**Form Data Diri**")
    name_form = st.text_input("Nama Lengkap")
    email_form = st.text_input("Email")
    submit_button = st.form_submit_button(label='Submit 🚀')
    
    if submit_button:
        if name_form and email_form:
            st.success(f"✅ Data berhasil disimpan! Nama: {name_form}, Email: {email_form}")
        else:
            st.error("❌ Harap isi semua field!")

st.markdown("---")

# =============================================
# 🎁 BONUS FEATURES
# =============================================
st.header("🎁 Bonus Features")

# Download Button
st.subheader("📥 Download Button")
try:
    csv_data = df_large.to_csv(index=False)
    st.download_button(
        label="📥 Download Data sebagai CSV",
        data=csv_data,
        file_name="sample_data.csv",
        mime="text/csv",
        help="Klik untuk mengunduh data contoh"
    )
except:
    st.info("🔧 Data tidak tersedia untuk download")

# Background Image (Optional)
st.subheader("🎨 Background Image")
if st.checkbox("Tampilkan Background Image (demo)"):
    st.info("🔧 Fitur background image membutuhkan file gambar di folder 'assets'")

# Sidebar Info
with st.sidebar:
    st.title("ℹ️ Informasi")
    st.markdown("""
    **Navigasi Praktikum:**
    - 📝 Text Elements
    - 📊 Data Elements  
    - 🖼️ Image Elements
    - 🎮 Interactive Elements
    - 📝 Input Elements
    """)
    
    st.markdown("---")
    st.subheader("🎯 Tips")
    st.info("""
    Gunakan menu sidebar untuk navigasi yang lebih mudah!
    
    Semua komponen Streamlit sudah ditampilkan dalam demo ini.
    """)
    
    if st.button("🎊 Tampilkan Celebration!"):
        st.balloons()
        st.snow()