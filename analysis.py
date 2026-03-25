import pandas as pd
import matplotlib.pyplot as plt

# load data
df = pd.read_csv("dataset/Housing.csv")

# show basic info
print(df.head())

# plot 1: area vs price
plt.scatter(df["area"], df["price"])
plt.xlabel("Area")
plt.ylabel("Price")
plt.title("Area vs Price")
plt.show()

# plot 2: bedrooms vs price
plt.scatter(df["bedrooms"], df["price"])
plt.xlabel("Bedrooms")
plt.ylabel("Price")
plt.title("Bedrooms vs Price")
plt.show()

# average price by bedrooms
avg_price = df.groupby("bedrooms")["price"].mean()

avg_price.plot(kind="bar")
plt.xlabel("Bedrooms")
plt.ylabel("Average Price")
plt.title("Avg Price by Bedrooms")
plt.show()
