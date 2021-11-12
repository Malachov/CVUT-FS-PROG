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
            # analyze.analyze_threshold(path)
            print("%s modified %s" % (path, mtime))
            col_list = ["teplota"]
            df = pd.read_csv(path, index_col=None, header=0, usecols=col_list)
            li = li.append(df, ignore_index=True)

# frame = pd.concat(li, axis=0, ignore_index=True)
li.reset_index()
li.to_csv("data/analyze.csv")
