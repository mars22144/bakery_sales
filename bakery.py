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
categories = ds.groupby("Category")["Total_Sales"].sum().reset_index()

# penjualan tiap cabang
cabang_sales = ds.groupby("Branch")["Total_Sales"].sum().reset_index()
cabang_sales = cabang_sales.sort_values(by="Total_Sales", ascending=False)

# 1 figure 4 subplot
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(15, 10))
fig.suptitle("Grafik penjualan", fontsize=16, fontweight="bold")

# grafik tren penjualan
penjualan_subplot = penjualan.copy()
penjualan_subplot["Date"] = penjualan_subplot["Date"].astype(str)
sbn.lineplot(ax=ax1, data=penjualan_subplot, x="Date", y="Total_Sales", marker="o", color="b", linewidth=2)
ax1.set_title("Penjualan Trend Bulanan", fontsize=12, fontweight="bold")
ax1.set_xlabel("Bulan")
ax1.set_ylabel("Total")
ax1.grid(True, linestyle="--", alpha=0.6)

# grafik product terlaris dan kurang laris
sbn.barplot(ax=ax2, data=product_sales, x="Quantity_Sold", y="Product_Name")
ax2.set_title("Penjualan Product Terlaris dan Kurang Laris", fontsize=12, fontweight="bold")
ax2.set_xlabel("Total")
ax2.set_ylabel("Nama Product")

# grafik kategori
ax3.pie(categories["Total_Sales"], labels=categories["Category"], autopct="%1.1f%%", startangle=140, colors=sbn.color_palette("Pastel1"))
ax3.set_title("Penjualan Berdasarkan Kategori", fontsize=12, fontweight="bold")

# Penjualan per cabang
sbn.barplot(ax=ax4, data=cabang_sales, x= "Branch", y="Total_Sales", palette="Set2")
ax4.set_title("Penjualan Setiap Cabang", fontsize=12, fontweight="bold")
ax4.set_xlabel("Cabang")
ax4.set_ylabel("Total")


print("=" * 15, "tren penjualan", "=" * 15)
print(penjualan.to_string(index=False))
print("=" * 15, "product terlaris dan kurang laku", "=" * 15)
print(product_sales.to_string(index=False))
print("=" * 15, "penjualan berdasarkan kategori", "=" * 15)
print(categories.to_string(index=False))
print("=" * 15, "penjualan tiap cabang", "=" * 15)
print(cabang_sales.to_string(index=False))
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()