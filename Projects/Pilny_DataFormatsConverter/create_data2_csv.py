import pandas as pd
import numpy as np

size = 101

df = pd.DataFrame()
df["Teplota_2"] = abs(20 + 2.5 * np.random.randn(size))

df["Jmeno"] = df["Teplota_2"]
df["Jmeno"] = np.random.randint(low=0, high=10, size=size)


df.loc[df["Jmeno"] == 0, "Jmeno"] = "Valasek"
df.loc[df["Jmeno"] == 1, "Jmeno"] = "Lukas"
df.loc[df["Jmeno"] == 2, "Jmeno"] = "Vitek"
df.loc[df["Jmeno"] == 3, "Jmeno"] = "Pavla"
df.loc[df["Jmeno"] == 4, "Jmeno"] = "Petra"
df.loc[df["Jmeno"] == 5, "Jmeno"] = "Eliska"
df.loc[df["Jmeno"] == 6, "Jmeno"] = ""
df.loc[df["Jmeno"] == 7, "Jmeno"] = "Ondra"
df.loc[df["Jmeno"] == 8, "Jmeno"] = "Radek"
df.loc[df["Jmeno"] == 9, "Jmeno"] = "Tomas"

df["Datum"] = df["Jmeno"]
df["Datum"] = pd.date_range(start="2021-11-01", end="2021/11/06", periods=size)

ids = np.random.randint(low=50000, high=59999, size=size)

df["Id"] = df["Jmeno"]
df["Id"] = ids

df = df.drop(columns=["Jmeno", "Id"])

df["Stroj"] = df["Datum"]
df["Stroj"] = np.random.randint(low=0, high=3, size=size)
df.loc[df["Stroj"] == 0, "Stroj"] = "Stroj1"
df.loc[df["Stroj"] == 1, "Stroj"] = "Stroj2"
df.loc[df["Stroj"] == 2, "Stroj"] = ""
df.loc[df["Stroj"] == 3, "Stroj"] = "Stroj1"
df.loc[df["Stroj"] == 4, "Stroj"] = "Stroj2"

df.to_csv("data/data2.csv", index=False)
df.to_excel("data/data2.xlsx", index=False)
df.to_parquet("data/data2.parquet", index=False)
