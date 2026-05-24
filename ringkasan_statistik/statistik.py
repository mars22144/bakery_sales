import pandas as pd

ds = pd.read_csv("csv/bakery_sales_dataset.csv", sep=",", encoding="latin1")

print("=== Statistik Deskriptif ===")
print(ds[['Quantity_Sold', 'Unit_Price', 'Total_Sales']].describe().round(2))
# convert ke rupiah
kurs = 4460
ds["Total_Sales_IDR"] = ds["Total_Sales"] * kurs

def rupiah(x):
    return f"Rp {x:,.0f}".replace(",", ".")

# total keseluruhan
total_omset     = ds['Total_Sales_IDR'].sum()
total_transaksi = len(ds)
rata2_transaksi = ds['Total_Sales_IDR'].mean()
total_qty       = ds['Quantity_Sold'].sum()

print("\n=== Ringkasan Umum ===")
print(f"Total omset          : {total_omset:,.0f}")
print(f"Total transaksi      : {total_transaksi}")
print(f"Rata-rata/transaksi  : {rata2_transaksi:.2f}")
print(f"Total qty terjual    : {total_qty}")

# penjualan percabang
print("\n=== Penjualan per Cabang ===")
branch_stats = ds.groupby('Branch').agg(
    Total_Omset    = ('Total_Sales_IDR',   'sum'),
    Jml_Transaksi  = ('Order_ID',      'count'),
    Rata2_Transaksi= ('Total_Sales_IDR',   'mean'),
    Total_Qty      = ('Quantity_Sold',  'sum')
).round(2)
branch_stats['Total_Omset']     = branch_stats['Total_Omset'].apply(rupiah)
branch_stats['Rata2_Transaksi'] = branch_stats['Rata2_Transaksi'].apply(rupiah)
print(branch_stats)

# penjualan per kategori
print("\n=== Penjualan per Kategori ===")
cat_stats = ds.groupby('Category').agg(
    Total_Omset   = ('Total_Sales_IDR',  'sum'),
    Jml_Transaksi = ('Order_ID',     'count'),
    Total_Qty     = ('Quantity_Sold', 'sum')
).sort_values('Total_Omset', ascending=False).round(2)
cat_stats['Total_Omset'] = cat_stats['Total_Omset'].apply(rupiah)
print(cat_stats)

# penjualan per bulan
print("\n=== Penjualan per Bulan ===")
ds["Date"] = pd.to_datetime(ds["Date"])
ds['Month_Name']  = ds['Date'].dt.strftime('%B %Y')
monthly_stats = ds.groupby('Month_Name').agg(
    Total_Omset   = ('Total_Sales_IDR',  'sum'),
    Jml_Transaksi = ('Order_ID',     'count'),
    Total_Qty     = ('Quantity_Sold', 'sum')
).round(2)
monthly_stats['Total_Omset'] = monthly_stats['Total_Omset'].apply(rupiah)
print(monthly_stats)

# 5 produk terlaris
print("\n=== Top 5 Produk Berdasarkan Omset ===")
top_produk = ds.groupby('Product_Name')['Total_Sales_IDR'].sum().sort_values(ascending=False).head(5)
print(top_produk.apply(rupiah))

# metode pembayaran
print("\n=== Persentase Metode Pembayaran ===")
payment_dist = ds['Payment_Method'].value_counts()
payment_pct  = ds['Payment_Method'].value_counts(normalize=True) * 100
print(pd.DataFrame({'Jumlah': payment_dist, 'Persentase (%)': payment_pct.round(1)}))