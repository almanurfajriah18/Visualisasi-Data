import streamlit as st

st.title("Google Colab Link")

st.markdown("""
### 📌 Link Google Colab
Klik tombol di bawah ini untuk membuka notebook:

<a href="https://colab.research.google.com/drive/1-uzCTEkrX-vBtS_FTe7guQ5ayGIaMmNy?usp=sharing" target="_blank">
    <button style="
        background-color:#4CAF50;
        color:white;
        padding:10px 20px;
        font-size:16px;
        border:none;
        border-radius:5px;
        cursor:pointer;
    ">
        Buka Google Colab
    </button>
</a>
""", unsafe_allow_html=True)
