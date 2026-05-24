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

# 1 figure 4 subplot
fig, axes = plt.subplots(nrows=2, ncols= 2, figsize=(15, 10))
fig.suptitle("Grafik penjualan", fontsize=16, fontweight="bold")

# grafik tren penjualan
penjualan_subplot = penjualan.copy()
penjualan_subplot["Date"] = penjualan_subplot["Date"].dt.to_timestamp()
sbn.lineplot(ax=axes[0, 0], data=penjualan_subplot, x="Date", y="Total_Sales", marker="o", color="b", linewidth=2)
axes[0, 0].set_title("Penjualan Trend Bulanan", fontsize=16, fontweight="bold")
axes[0, 0].set_xlabel("Bulan")
axes[0, 0].set_ylabel("Total")
axes[0, 0].grid(True, linestyle="--", alpha=0.6)

# grafik product terlaris dan kurang laris
plt.figure(figsize=(10, 5))
sbn.barplot(data=product_sales, x="Quantity_Sold", y="Product_Name", palette="Blues_r")
plt.title("Grafik Penjualan Product yang laris dan yang kurang laku")
plt.xlabel("Total")
plt.ylabel("Product")


print("=" * 15, "tren penjualan", "=" * 15)
print(penjualan.to_string(index=False))
print("=" * 15, "product terlaris dan kurang laku", "=" * 15)
print(product_sales.to_string(index=False))
print("=" * 15, "penjualan berdasarkan kategori", "=" * 15)
print(categories.to_string(index=False))
print("=" * 15, "penjualan tiap cabang", "=" * 15)
print(cabang_sales.to_string(index=False))
plt.tight_layout()
plt.show()