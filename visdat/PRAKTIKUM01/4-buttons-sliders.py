import streamlit as st
import time

# Konfigurasi halaman
st.set_page_config(
    page_title="4. Buttons and Sliders",
    layout="centered"
)

# Header dan informasi kelompok
st.title("4. Buttons and Sliders")
st.write("**Mata Kuliah:** Visualisasi Data")
st.write("**Dosen:** Imam Haromain, S.Si., M.Kom.")

st.subheader("Anggota Kelompok:")
st.write("**1. Tria Maulida Sari - 0110222300**")
st.write("**2. Alma Nur Fajriah - 0110222222**")
st.write("**3. Rahma Dian Nurhikma - 0110222082**")

st.markdown("---")

# Button
st.header("Button")
button = st.button('Click Here')
if button:
    st.write("You have Clicked the Button")
else:
    st.write("You have not Clicked the Button")

# Radio Buttons
st.header("Radio Buttons")
gender = st.radio(
    "Select Gender", 
    ('Male', 'Female', 'Others'))
if gender == 'Male':
    st.write("You have selected Male.")
elif gender == 'Female':
    st.write("You have selected Female.")
else:
    st.write("You have selected Others.")

# Checkboxes
st.header("Checkboxes")
st.write("Select your Hobbies: ")
check_1 = st.checkbox('Books')
check_2 = st.checkbox('Movies')
check_3 = st.checkbox('Sports')

# Dropdown
st.header("Dropdown")
hobby = st.selectbox(
    'Choose your Hobby: ',
    ('Books', 'Movies', 'Sports')
)

# Multi-Select
st.header("Multi-Select")
hobbies = st.multiselect(
    'What are your hobbies',
    ['Reading', 'Cooking', 'Watching Movies/TV Series', 'Playing', 'Drawing', 'Hiking'], 
    ['Reading', 'Playing']
)

# Download Button
st.header("Download Button")
down_btn = st.download_button(
    label="Download Image",
    data=open("assets/img1.jpg", "rb"),
    file_name="img2.jpg",
    mime="image/jpeg"
)

# Progress Bar
st.header("Progress Bar")
download = st.progress(0)
for percentage in range(100):
    time.sleep(0.1)
    download.progress(percentage + 1)
st.write("Download Complete")

# Spinner
st.header("Spinner")
with st.spinner('Loading...'):
    time.sleep(5)
st.write('Hello Data Scientists')