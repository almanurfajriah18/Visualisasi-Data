import streamlit as st

# Konfigurasi halaman
st.set_page_config(
    page_title="Praktikum 1 - Text Elements",
    layout="centered"
)

# Header dan informasi kelompok
st.title("1. Text Elements")
st.write("**Mata Kuliah:** Visualisasi Data")
st.write("**Dosen:** Imam Haromain, S.Si., M.Kom.")

st.markdown("---")

st.subheader("Anggota Kelompok:")
st.write("**1. Tria Maulida Sari - 0110222300**")
st.write("**2. Alma Nur Fajriah - 0110222222**")
st.write("**3. Rahma Dian Nurhikma - 0110222082**")

st.markdown("---")

# Bagian 1: Basic Text Elements
st.header("Basic Text Elements")
st.write("Berbagai komponen dasar untuk menampilkan teks dalam Streamlit")

st.subheader("Demonstrasi Text Elements")
st.header("Ini Header")
st.subheader("Ini Subheader")
st.text("Ini teks biasa tanpa format")
st.markdown("**Ini teks bold** dan *ini teks italic*")
st.caption("Ini caption biasanya dibawah gambar untuk penjelasan")

st.markdown("---")

# Bagian 2: Multi-line Markdown
st.header("Multi-line Markdown")
st.write("Menampilkan konten dengan format markdown yang lebih kompleks")

st.markdown("""
- ini baris 1 
- ini menggunakan markdown multi baris            
1. ini baris 2
2. ini menggunakan markdown multibaris
* ini baris 3
* ini mengguanakan markdown multibaris                  
""")

st.markdown("---")

# Bagian 3: Coba Mandiri
st.header("Coba Mandiri")
st.write("Implementasi tugas mandiri untuk praktikum")

st.header("Praktikum 1 Visualisasi Data")
st.subheader("Bagian 1 : Text Element")
st.markdown("""
- Alma Nur Fajriah - 0110222222
- Tria Maulida Sari - 0110222300  
- Rahma Dian Nurhikma - 0110222082
""")

st.markdown("---")

# Bagian 4: Plain Text & Markdown
st.header("Plain Text & Basic Markdown")

st.subheader("Plain Text")
st.text("Hi, \nWorld\t!")
st.text('Selamat Datang')
st.text('Streamlit')

st.subheader("Formatted Markdown")
st.markdown("**Hi, World**")

st.markdown("---")

# Bagian 5: LaTeX Mathematical Expressions
st.header("LaTeX Mathematical Expressions")
st.write("Menampilkan rumus matematika menggunakan LaTeX")

st.latex(r'''cos2\theta = 1 - 2sin^2\theta''')
st.latex("""(a+b)^2 = a^2 + b^2 + 2ab""")
st.latex(r'''\frac{\partial u}{\partial t}
         = h^2 \left( \frac{\partial^2 u}{\partial x^2}
         + \frac{\partial^2 u}{\partial y^2}
         + \frac{\partial^2 u}{\partial z^2} \right)''')

st.markdown("---")

# Bagian 6: Code Display
st.header("Code Display")
st.write("Menampilkan kode programming dengan syntax highlighting")

st.subheader("Python Code")
python_code = '''def hello():
    print("Hello, TriaMaul!")'''
st.code(python_code, language='python')

st.subheader("Java Code")
java_code = """public class CFG {
    public static void main(String args[]) {
        System.out.println("Hello Tria!");
    }
}"""
st.code(java_code, language='java')

st.subheader("Javascript Code")
javascript_code = """ <p id="demo"></p>
<script>
try {
    addlert("Welcome guest!");
}
catch(err) {
    document.getElementById("demo").innerHTML = err.message;
}
</script> """
st.code(javascript_code, language='javascript')