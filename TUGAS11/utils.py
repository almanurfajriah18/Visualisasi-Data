# -*- coding: utf-8 -*-
"""
utils.py
Fungsi helper untuk aplikasi Streamlit
"""

import pandas as pd
import numpy as np
from datetime import datetime

def load_and_clean_data(file_path='harga_pertanian.csv'):
    """
    Memuat dan membersihkan data dari file CSV
    
    Parameters:
    file_path (str): Path ke file CSV
    
    Returns:
    pandas.DataFrame: Data yang sudah dibersihkan
    """
    print("🔍 Memuat data dari:", file_path)
    
    # 1. Load data
    try:
        df = pd.read_csv(file_path)
        print(f"   ✓ Data berhasil dimuat: {len(df)} baris, {len(df.columns)} kolom")
    except Exception as e:
        print(f"   ✗ Error memuat data: {e}")
        return None
    
    # 2. Cleaning data
    print("🧹 Memulai proses cleaning data...")
    
    # Konversi tipe data
    df['periode_update'] = pd.to_datetime(df['periode_update'], format='%Y-%m', errors='coerce')
    df['jumlah'] = pd.to_numeric(df['jumlah'], errors='coerce')
    
    # Tambah kolom bulan dan tahun
    df['bulan'] = df['periode_update'].dt.month
    df['tahun'] = df['periode_update'].dt.year
    
    # Hapus harga 0 atau negatif
    df_clean = df[df['jumlah'] > 0].copy()
    print(f"   ✓ Data dibersihkan: {len(df_clean)} baris valid")
    
    return df_clean

def get_summary_stats(df):
    """
    Mendapatkan statistik ringkasan dari data
    
    Parameters:
    df (pandas.DataFrame): Data yang sudah dibersihkan
    
    Returns:
    dict: Dictionary berisi statistik
    """
    stats = {
        'total_data': len(df),
        'total_komoditas': df['kategori'].nunique(),
        'total_kabupaten': df['nama_kabupaten_kota'].nunique(),
        'tahun_awal': int(df['tahun'].min()),
        'tahun_akhir': int(df['tahun'].max()),
        'harga_min': df['jumlah'].min(),
        'harga_max': df['jumlah'].max(),
        'harga_rata': df['jumlah'].mean(),
    }
    return stats

def get_bulan_indonesia(bulan_angka):
    """
    Konversi angka bulan ke nama bulan Indonesia
    
    Parameters:
    bulan_angka (int): Angka bulan (1-12)
    
    Returns:
    str: Nama bulan dalam Bahasa Indonesia
    """
    bulan_dict = {
        1: 'Januari', 2: 'Februari', 3: 'Maret', 4: 'April',
        5: 'Mei', 6: 'Juni', 7: 'Juli', 8: 'Agustus',
        9: 'September', 10: 'Oktober', 11: 'November', 12: 'Desember'
    }
    return bulan_dict.get(bulan_angka, f"Bulan {bulan_angka}")