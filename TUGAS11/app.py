# -*- coding: utf-8 -*-
"""
app.py
Dashboard Harga Komoditas Pertanian
Kelompok:
- Tria Maulida Sari - 0110222300
- Rahma Dian Nurhikma
- Alma Nur Fajria - 0110222222

Dashboard untuk visualisasi data harga komoditas pertanian
"""

# ============================================
# IMPORT LIBRARY
# ============================================
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from utils import load_and_clean_data, get_summary_stats, get_bulan_indonesia

# ============================================
# KONFIGURASI HALAMAN
# ============================================
st.set_page_config(
    page_title="Dashboard Harga Pertanian",
    page_icon="🌾",
    layout="wide"
)

# ============================================
# FUNGSI UTAMA
# ============================================
def main():
    """
    Fungsi utama untuk menjalankan dashboard
    """
    
    # ============================================
    # HEADER DAN JUDUL
    # ============================================
    st.title("📊 DASHBOARD HARGA KOMODITAS PERTANIAN")
    st.markdown("---")
    
    # ============================================
    # SIDEBAR - FILTER DATA
    # ============================================
    st.sidebar.title("🔧 FILTER DATA")
    st.sidebar.markdown("---")
    
    # Load data
    df = load_and_clean_data('harga_pertanian.csv')
    
    if df is None:
        st.error("❌ File 'harga_pertanian.csv' tidak ditemukan!")
        st.info("""
        Pastikan file CSV ada di folder yang sama dengan app.py
        Atau upload file melalui sidebar
        """)
        return
    
    # Filter tahun
    tahun_list = sorted(df['tahun'].unique().tolist())
    selected_year = st.sidebar.selectbox(
        "Pilih Tahun:",
        tahun_list
    )
    
    # Filter komoditas
    komoditas_list = df['kategori'].unique().tolist()
    selected_komoditas = st.sidebar.multiselect(
        "Pilih Komoditas:",
        komoditas_list,
        default=['BERAS MEDIUM', 'BERAS PREMIUM', 'GABAH KERING GILING']
    )
    
    if not selected_komoditas:
        st.warning("⚠️ Silakan pilih minimal 1 komoditas")
        return
    
    # Filter data berdasarkan pilihan
    df_filtered = df[
        (df['tahun'] == selected_year) &
        (df['kategori'].isin(selected_komoditas))
    ]
    
    st.sidebar.markdown("---")
    st.sidebar.info("""
    **Dashboard ini menampilkan:**
    - Tren harga komoditas
    - Perbandingan antar wilayah
    - Distribusi harga
    """)
    
    # ============================================
    # BAGIAN 1: STATISTIK DATA
    # ============================================
    st.header("📈 STATISTIK DATA")
    
    # Hitung statistik
    stats = get_summary_stats(df_filtered)
    
    # Tampilkan dalam kolom
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Data", f"{stats['total_data']:,}")
    
    with col2:
        st.metric("Jenis Komoditas", stats['total_komoditas'])
    
    with col3:
        st.metric("Jumlah Kabupaten", stats['total_kabupaten'])
    
    with col4:
        st.metric("Tahun", selected_year)
    
    st.markdown("---")
    
    # ============================================
    # BAGIAN 2: TREN HARGA PER BULAN
    # ============================================
    st.header("📈 TREN HARGA PER BULAN")
    
    # Buat line chart untuk setiap komoditas
    fig1, ax1 = plt.subplots(figsize=(12, 6))
    
    colors = ['blue', 'red', 'green', 'orange', 'purple', 'brown']
    
    for i, komoditas in enumerate(selected_komoditas):
        # Filter data per komoditas
        data_komoditas = df_filtered[df_filtered['kategori'] == komoditas]
        
        # Group by bulan
        harga_per_bulan = data_komoditas.groupby('bulan')['jumlah'].mean().sort_index()
        
        # Plot
        ax1.plot(
            harga_per_bulan.index,
            harga_per_bulan.values,
            marker='o',
            linewidth=2,
            label=komoditas,
            color=colors[i % len(colors)]
        )
    
    # Setting plot
    bulan_nama = ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 
                  'Jul', 'Ags', 'Sep', 'Okt', 'Nov', 'Des']
    
    ax1.set_xticks(range(1, 13))
    ax1.set_xticklabels(bulan_nama)
    ax1.set_xlabel('Bulan')
    ax1.set_ylabel('Harga Rata-rata (Rp/Kg)')
    ax1.set_title(f'Tren Harga Komoditas - Tahun {selected_year}')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    st.pyplot(fig1)
    
    # Tabel data di bawah grafik
    with st.expander("📋 Lihat Data Rinci per Bulan"):
        pivot_data = df_filtered.pivot_table(
            values='jumlah',
            index='bulan',
            columns='kategori',
            aggfunc='mean'
        ).round(0)
        
        # Ganti index bulan dengan nama
        pivot_data.index = [get_bulan_indonesia(b) for b in pivot_data.index]
        
        st.dataframe(pivot_data)
    
    st.markdown("---")
    
    # ============================================
    # BAGIAN 3: PERBANDINGAN WILAYAH
    # ============================================
    st.header("🏙️ PERBANDINGAN HARGA PER WILAYAH")
    
    # Pilih komoditas untuk analisis wilayah
    komoditas_wilayah = st.selectbox(
        "Pilih komoditas untuk analisis wilayah:",
        selected_komoditas,
        key="wilayah_select"
    )
    
    # Hitung rata-rata per wilayah
    harga_per_wilayah = df_filtered[df_filtered['kategori'] == komoditas_wilayah]\
        .groupby('nama_kabupaten_kota')['jumlah']\
        .mean()\
        .sort_values(ascending=False)
    
    # Ambil top 10
    top_wilayah = harga_per_wilayah.head(10)
    
    # Buat bar chart horizontal
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    
    bars = ax2.barh(
        range(len(top_wilayah)),
        top_wilayah.values,
        color='skyblue'
    )
    
    # Setting plot
    ax2.set_yticks(range(len(top_wilayah)))
    ax2.set_yticklabels(top_wilayah.index)
    ax2.set_xlabel('Harga Rata-rata (Rp/Kg)')
    ax2.set_title(f'10 Wilayah dengan Harga {komoditas_wilayah} Tertinggi')
    ax2.invert_yaxis()  # Tertinggi di atas
    
    # Tambah nilai di bar
    for i, (bar, harga) in enumerate(zip(bars, top_wilayah.values)):
        ax2.text(
            harga + 500,
            bar.get_y() + bar.get_height()/2,
            f'Rp {harga:,.0f}',
            va='center'
        )
    
    st.pyplot(fig2)
    
    st.markdown("---")
    
    # ============================================
    # BAGIAN 4: DISTRIBUSI HARGA
    # ============================================
    st.header("📊 DISTRIBUSI HARGA")
    
    # Buat boxplot
    fig3, ax3 = plt.subplots(figsize=(10, 6))
    
    # Siapkan data untuk boxplot
    box_data = []
    for komoditas in selected_komoditas:
        box_data.append(df_filtered[df_filtered['kategori'] == komoditas]['jumlah'])
    
    # Plot boxplot
    box = ax3.boxplot(
        box_data,
        labels=selected_komoditas,
        patch_artist=True
    )
    
    # Warna untuk setiap box
    colors_box = ['lightblue', 'lightgreen', 'lightcoral', 'lightyellow', 'lightgray']
    for patch, color in zip(box['boxes'], colors_box):
        patch.set_facecolor(color)
    
    # Setting plot
    ax3.set_ylabel('Harga (Rp/Kg)')
    ax3.set_title('Distribusi Harga per Komoditas')
    ax3.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    
    st.pyplot(fig3)
    
    # ============================================
    # BAGIAN 5: DATA DETAIL
    # ============================================
    st.header("📋 DATA DETAIL")
    st.markdown("---")
    
    # Tampilkan data dalam tabel
    st.dataframe(
        df_filtered[[
            'kategori',
            'nama_kabupaten_kota', 
            'jumlah',
            'periode_update',
            'satuan'
        ]].rename(columns={
            'kategori': 'Komoditas',
            'nama_kabupaten_kota': 'Kabupaten/Kota',
            'jumlah': 'Harga',
            'periode_update': 'Periode',
            'satuan': 'Satuan'
        }),
        height=400
    )
    
    # ============================================
    # FOOTER
    # ============================================
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: gray;'>
        <p>Dashboard Harga Pertanian • Dibuat dengan Streamlit</p>
        <p>Data diperbarui: """ + pd.Timestamp.now().strftime("%d %B %Y") + """</p>
    </div>
    """, unsafe_allow_html=True)

# ============================================
# JALANKAN APLIKASI
# ============================================
if __name__ == "__main__":
    main()