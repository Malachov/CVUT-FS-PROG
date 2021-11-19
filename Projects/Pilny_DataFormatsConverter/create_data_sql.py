import pandas as pd
import numpy as np
import mydatapreprocessing


size = 101

df = pd.DataFrame()
df["Teplota"] = abs(20 + 2.5 * np.random.randn(size))

df["Jmeno"] = df["Teplota"]
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
mydatapreprocessing.database.database_write(
    server=".", database="Moje_data", trusted_connection=True, df=df, table="data1", if_exists="replace"
)
