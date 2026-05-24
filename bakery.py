import pandas as pd
import matplotlib.pylab as mpatches
import matplotlib.cm as mcm

ds = pd.read_csv("csv/bakery_sales_dataset.csv", sep=",", encoding="latin1")

# product terlaris
pop_product = ds.groupby("Product_Name")["Quantity_Sold"].sum().reset_index()
pop_product = pop_product.sort_values(by="Quantity_Sold", ascending=False)



print(pop_product.to_string(index=False))