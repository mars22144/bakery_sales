import pandas as pd
import matplotlib.pylab as mpatches
import seaborn as sbn

ds = pd.read_csv("csv/bakery_sales_dataset.csv", sep=",", encoding="latin1")

# tren penjualan(ganti to_period sesuai kebutuhan)
ds["Date"] = pd.to_datetime(ds["Date"])
penjualan = ds.groupby(ds["Date"].dt.to_period("M"))["Total_Sales"].sum().reset_index()

# product terlaris dan yang kurang laku
product_sales = ds.groupby("Product_Name")["Quantity_Sold"].sum().reset_index()
product_sales = product_sales.sort_values(by="Quantity_Sold", ascending=False)

print("=" * 15, "tren penjualan", "=" * 15)
print(penjualan.to_string(index=False))
print("=" * 15, "product terlaris dan kurang laku", "=" * 15)
print(product_sales.to_string(index=False))