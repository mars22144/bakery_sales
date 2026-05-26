import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn

ds = pd.read_csv("csv/bakery_sales_dataset.csv", sep=",", encoding="latin1")

# convert ke rupiah
kurs = 4460
ds["Total_Sales_IDR"] = ds["Total_Sales"] * kurs

def rupiah(x):
    return f"Rp {x:,.0f}".replace(",", ".")

# tren penjualan
ds["Date"] = pd.to_datetime(ds["Date"])
ds["Year_Month"] = ds["Date"].dt.strftime("%Y-%m")
penjualan = ds.groupby("Year_Month")["Total_Sales_IDR"].sum().reset_index()

# product terlaris dan yang kurang laku
product_sales = ds.groupby("Product_Name")["Quantity_Sold"].sum().reset_index()
product_sales = product_sales.sort_values(by="Quantity_Sold", ascending=False)

# penjualan berdasarkan kaetogri
categories = ds.groupby("Category")["Total_Sales_IDR"].sum().reset_index()

# penjualan tiap cabang
cabang_sales = ds.groupby("Branch")["Total_Sales_IDR"].sum().reset_index()
cabang_sales = cabang_sales.sort_values(by="Total_Sales_IDR", ascending=False)

# 1 figure 4 subplot
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(15, 10))
fig.suptitle("Grafik penjualan", fontsize=16, fontweight="bold")

# grafik tren penjualan
sbn.lineplot(ax=ax1, data=penjualan, x="Year_Month", y="Total_Sales_IDR", marker="o", color="b", linewidth=2)
ax1.set_title("Penjualan Trend Bulanan", fontsize=12, fontweight="bold")
ax1.set_xlabel("Bulan")
ax1.set_ylabel("Total(Rp)")
ax1.grid(True, linestyle="--", alpha=0.6)
ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x)).replace(",", ".")))

# grafik product terlaris dan kurang laris
sbn.barplot(ax=ax2, data=product_sales, x="Quantity_Sold", y="Product_Name")
ax2.set_title("Penjualan Setiap Product", fontsize=12, fontweight="bold")
ax2.set_xlabel("Total")
ax2.set_ylabel("Nama Product")

# grafik kategori
ax3.pie(categories["Total_Sales_IDR"], labels=categories["Category"], autopct="%1.1f%%", startangle=140, colors=sbn.color_palette("Pastel1"))
ax3.set_title("Omset Penjualan Berdasarkan Kategori", fontsize=12, fontweight="bold")

# Penjualan per cabang
sbn.barplot(ax=ax4, data=cabang_sales, x= "Branch", y="Total_Sales_IDR")
ax4.set_title("Omset Penjualan Setiap Cabang", fontsize=12, fontweight="bold")
ax4.set_xlabel("Cabang")
ax4.set_ylabel("Total(Rp)")
ax4.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x)).replace(",", ".")))

plt.tight_layout(rect=[0, 0, 1, 0.95])

print("=" * 15, "tren penjualan", "=" * 15)
penjualan = penjualan.sort_values(by="Year_Month")
penjualan["Total_Sales_IDR"] = penjualan["Total_Sales_IDR"].apply(rupiah)
print(penjualan.to_string(index=False))

print("=" * 15, "product terlaris dan kurang laku", "=" * 15)
print(product_sales.to_string(index=False))

print("=" * 15, "penjualan berdasarkan kategori", "=" * 15)
categories = categories.sort_values(by="Total_Sales_IDR", ascending=False)
categories["Total_Sales_IDR"] = categories["Total_Sales_IDR"].apply(rupiah)
print(categories.to_string(index=False))

print("=" * 15, "penjualan tiap cabang", "=" * 15)
cabang_sales = cabang_sales.sort_values(by="Total_Sales_IDR", ascending=False)
cabang_sales["Total_Sales_IDR"] = cabang_sales["Total_Sales_IDR"].apply(rupiah)
print(cabang_sales.to_string(index=False))

plt.show()