import pandas as pd
import numpy as np

size = 100

df = pd.DataFrame()
df["teplota"] = abs(20 + 2.5 * np.random.randn(size))

df["jmeno"] = df["teplota"]
df["jmeno"].iloc[:50] = "Novak"
df["jmeno"].iloc[50:] = "Bures"
df["datum"] = df["jmeno"]
df["datum"] = pd.date_range(start="2021-11-01", end="2021/11/02", periods=size)

ids = np.random.randint(low=1e6, high=1e7, size=size)

df["id"] = df["jmeno"]
df["id"] = ids


df.to_csv("data/data_linka1.csv")
