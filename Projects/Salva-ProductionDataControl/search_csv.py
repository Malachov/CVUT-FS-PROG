import os
import datetime as dt
import pandas as pd

now = dt.datetime.now()
ago = now - dt.timedelta(days=1)
li = pd.DataFrame()

for root, dirs, files in os.walk("data"):
    for fname in files:
        path = os.path.join(root, fname)
        st = os.stat(path)
        mtime = dt.datetime.fromtimestamp(st.st_mtime)
        if mtime > ago:
            print("%s modified %s" % (path, mtime))
            df = pd.read_csv(path, index_col=None, header=0)
            li = li.append(df, ignore_index=True)

li.set_index("id", drop=True, inplace=True)
li.to_csv("data/analyze.csv")

maximum = li["teplota"].max()
minimum = li["teplota"].min()
