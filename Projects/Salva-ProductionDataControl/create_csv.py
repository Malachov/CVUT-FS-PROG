import pandas as pd
import numpy as np


df = pd.DataFrame()
df["teplota"] = np.random.randn(100)

df["jmeno"] = df["teplota"]
df["jmeno"].iloc[:50] = "Novak"
df["jmeno"].iloc[50:] = "Bures"
df["datum"] = df["jmeno"]
df["datum"] = pd.date_range(start="2021-11-01", end="2021/11/02", periods=100)

ids = np.random.randint(low=1e6, high=1e7, size=100)

df["id"] = df["jmeno"]
df["id"] = ids


df.to_csv("data/data_linka2.csv")
