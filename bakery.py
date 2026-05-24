import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn

ds = pd.read_csv("csv/bakery_sales_dataset.csv", sep=",", encoding="latin1")

# tren penjualan(ganti to_period sesuai kebutuhan)
ds["Date"] = pd.to_datetime(ds["Date"])
penjualan = ds.groupby(ds["Date"].dt.to_period("M"))["Total_Sales"].sum().reset_index()

# product terlaris dan yang kurang laku
product_sales = ds.groupby("Product_Name")["Quantity_Sold"].sum().reset_index()
product_sales = product_sales.sort_values(by="Quantity_Sold", ascending=False)

# penjualan berdasarkan kaetogri
categories = ds.groupby("Category")["Quantity_Sold"].sum().reset_index()

# penjualan tiap cabang
cabang_sales = ds.groupby("Branch")["Total_Sales"].sum().reset_index()
cabang_sales = cabang_sales.sort_values(by="Total_Sales", ascending=False)

# grafik tren penjualan
plt.figure(figsize=(10, 5))
penjualan["Date"] = penjualan["Date"].dt.to_timestamp()

sbn.lineplot(data=penjualan, x="Date", y="Total_Sales", marker="o", color="b")
plt.title("Tren Penjualan Bulanan")
plt.xlabel("Bulan")
plt.ylabel("Total Penjualan")
plt.grid(True)


print("=" * 15, "tren penjualan", "=" * 15)
print(penjualan.to_string(index=False))
print("=" * 15, "product terlaris dan kurang laku", "=" * 15)
print(product_sales.to_string(index=False))
print("=" * 15, "penjualan berdasarkan kategori", "=" * 15)
print(categories.to_string(index=False))
print("=" * 15, "penjualan tiap cabang", "=" * 15)
print(cabang_sales.to_string(index=False))
plt.show()