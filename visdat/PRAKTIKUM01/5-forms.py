import streamlit as st
import pandas as pd
import datetime

# Konfigurasi halaman
st.set_page_config(
    page_title="5. Forms",
    layout="centered"
)

# Header dan informasi kelompok
st.title("5. Forms")
st.write("**Mata Kuliah:** Visualisasi Data")
st.write("**Dosen:** Imam Haromain, S.Si., M.Kom.")

st.subheader("Anggota Kelompok:")
st.write("**1. Tria Maulida Sari - 0110222300**")
st.write("**2. Alma Nur Fajriah - 0110222222**")
st.write("**3. Rahma Dian Nurhikma - 0110222082**")

st.markdown("---")

# Text Input
st.header("Text Input")
name = st.text_input("Enter your name")
st.write("Your name is: ", name)

# Text Area
st.header("Text Area")
input_text = st.text_area("Enter your Review")
st.write("You entered:", input_text)

# Number Input
st.header("Number Input")
st.number_input("Enter your number")
num = st.number_input("Enter your number", 0, 10, 5, 2)
st.write("Min. Value is 0, Max. value is 10")
st.write("Default Value is 5, Step Size value is 2")
st.write("Total value after adding Number entered with step value is:", num)

# Time Input
st.header("Time Input")
st.time_input("Select Your Time")

# Date Input
st.header("Date Input")
st.date_input("Select Date")

# Date Input with Constraints
st.header("Date Input with Constraints")
st.date_input(
    "Select Date", 
    value=datetime.date(1989, 12, 25),
    min_value=datetime.date(1970, 1, 1),
    max_value=datetime.date(2022, 12, 31)
)

# Color Picker
st.header("Color Picker")
color_code = st.color_picker("Select your Color")
st.write("Selected color code:", color_code)

# File Uploader
st.header("CSV File Upload")
data_file = st.file_uploader("Upload CSV file", type=["csv"])
details = st.button("Check Details")

if details:
    if data_file is not None:
        file_details = {
            "file_name": data_file.name,
            "file_type": data_file.type,
            "file_size": data_file.size
        }
        st.write("File Details:")
        st.write(file_details)
        df = pd.read_csv(data_file)
        st.write("Data Preview:")
        st.dataframe(df)
    else:
        st.write("No CSV File is Uploaded")

# Form
st.header("Form with Submit")
my_form = st.form(key='form')
a = my_form.text_input(label='Enter any text')
submitted = my_form.form_submit_button(label='Submit')

if submitted:
    st.write("Submitted text:", a)