import pandas as pd
import matplotlib.pylab as mpatches
import seaborn as sbn

ds = pd.read_csv("csv/bakery_sales_dataset.csv", sep=",", encoding="latin1")

ds["Date"] = pd.to_datetime(ds["Date"])

# tren penjualan(ganti to_period sesuai kebutuhan)
penjualan = ds.groupby(ds["Date"].dt.to_period("M"))["Total_Sales"].sum().reset_index()
print(penjualan.to_string(index=False))