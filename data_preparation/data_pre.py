import pandas as pd

ds = pd.read_csv("csv/bakery_sales_dataset.csv", sep=",", encoding="latin1")
print(f"Jumlah baris : {ds.shape[0]}")
print(f"Jumlah kolom : {ds.shape[1]}")

# 5 data pertama dan terakhir
print("\n5 Data Pertama:")
print(ds.head(5))
print("\n5 Data Terakhir:")
print(ds.tail(5))

# --- 3. Cek Tipe Data ---
print("\nTipe Data Setiap Kolom:")
print(ds.dtypes)

# --- 4. Cek Missing Values ---
print("\nJumlah Missing Values per Kolom:")
print(ds.isnull().sum())

# Persentase missing values
missing_pct = (ds.isnull().sum() / len(ds)) * 100
print("\nPersentase Missing Values:")
print(missing_pct)

# --- 5. Cek Data Duplikat ---
duplikat = ds.duplicated().sum()
print(f"\nJumlah Data Duplikat: {duplikat}")

# --- 6. Konversi Tipe Data ---
# Ubah kolom Date dari string ke datetime
ds['Date'] = pd.to_datetime(ds['Date'])
print("\nKolom Date setelah konversi:", ds['Date'].dtype)

# --- 7. Feature Engineering ---
# Tambah kolom Month dan Month_Name dari Date
ds['Month']      = ds['Date'].dt.to_period('M')
ds['Month_Name']  = ds['Date'].dt.strftime('%B %Y')
ds['Day_of_Week'] = ds['Date'].dt.day_name()

print("\nKolom baru berhasil ditambahkan:")
print(ds[['Date', 'Month', 'Month_Name', 'Day_of_Week']].head())

# --- 8. Konfirmasi Dataset Bersih ---
print("\n=== Dataset siap digunakan ===")
print(f"Total baris    : {ds.shape[0]}")
print(f"Total kolom    : {ds.shape[1]}")
print(f"Missing values : {ds.isnull().sum().sum()}")
print(f"Duplikat       : {ds.duplicated().sum()}")