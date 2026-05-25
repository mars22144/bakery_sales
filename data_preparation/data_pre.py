import pandas as pd

ds = pd.read_csv("csv/bakery_sales_dataset.csv", sep=",", encoding="latin1")
print(f"Jumlah baris : {ds.shape[0]}")
print(f"Jumlah kolom : {ds.shape[1]}")

# cek record yang kosong
nilai_hilang = ds.isnull().sum().sum()
print(f"\nJumlah record yang hilang: {nilai_hilang}")

# 5 data pertama dan terakhir
print("\n5 Data Pertama:")
print(ds.head(5))
print("\n5 Data Terakhir:")
print(ds.tail(5))

# cek tipe data
print("\nTipe Data Setiap Kolom:")
print(ds.dtypes)

# cek duplikasi data
duplikat = ds.duplicated().sum()
print(f"\nJumlah Data Duplikat: {duplikat}")

# conver tipe data(string ke datetime)
ds['Date'] = pd.to_datetime(ds['Date'])
print("\nKolom Date setelah konversi:", ds['Date'].dtype)

# tambah kolom data baru
ds['Month']      = ds['Date'].dt.to_period('M')
ds['Month_Name']  = ds['Date'].dt.strftime('%B')
ds['Day_of_Week'] = ds['Date'].dt.day_name()
print("\nKolom baru berhasil ditambahkan:")
print(ds[['Date', 'Month', 'Month_Name', 'Day_of_Week']].head(5))

# --- Konfirmasi Dataset Bersih ---
masalah = False

# missing value
if nilai_hilang > 0:
    masalah = True
    print(f"Missing values ditemukan : {nilai_hilang} nilai kosong")
    print("  Detail per kolom:")
    
    detail_missing = ds.isnull().sum()[ds.isnull().sum() > 0]
    
    baris_teks = "  - " + detail_missing.index.str.ljust(20) + " : " + detail_missing.astype(str) + " nilai kosong"
    print("\n".join(baris_teks))

    baris_missing = ds[ds.isnull().any(axis=1)]
    
    print(f"Baris yang missing value:")
    print(baris_missing.head(5).to_string(index=False))
else:
    print("Missing values  : Tidak ada")

# duplicate
if duplikat > 0:
    masalah = True
    print(f"\nDuplikat ditemukan : {duplikat} baris duplikat")

    baris_duplikat = ds[ds.duplicated(keep=False)]

    print("Detail kolom penyebab duplikat:")
    detail_duplikat = ds.apply(lambda x: x.duplicated().sum())
    detail_duplikat = detail_duplikat[detail_duplikat > 0]

    # Gabungkan hasilnya menjadi string
    baris_teks = "  - " + detail_duplikat.index.str.ljust(20) + " : " + detail_duplikat.astype(str) + " duplikat"
    print("\n".join(baris_teks))

    print(f"\nbaris duplikat:")
    print(baris_duplikat.head(5).to_string(index=False))
else:
    print("Duplikat: Tidak ada")

# datetime
if ds["Date"].dtype != "datetime64[ns]":
    masalah = True
    print(f"Kolom date blm datetime, tipe saat ini: {ds['Date'].dtype()}")

if masalah:
    print(f"Data blm bersih, silahkan perbaiki terlebih dahulu")
else:
    print("\n=== Ringkasan ===")
    print(f"Total baris    : {ds.shape[0]}")
    print(f"Total kolom    : {ds.shape[1]}")
    print(f"Missing values : {ds.isnull().sum().sum()}")
    print(f"Duplikat       : {ds.duplicated().sum()}")  
