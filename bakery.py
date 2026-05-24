import pandas as pd
import matplotlib.pylab as mpatches
import matplotlib.cm as mcm

ds = pd.read_csv("csv/bakery_sales_dataset.csv", sep=",", encoding="latin1")

pop_product = ds["Product_Name"].value_counts().idxmax()

print(pop_product)