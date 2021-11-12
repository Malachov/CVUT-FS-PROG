import analyze
import os
import datetime as dt

now = dt.datetime.now()
ago = now - dt.timedelta(days=1)

for root, dirs, files in os.walk("data"):
    for fname in files:
        path = os.path.join(root, fname)
        st = os.stat(path)
        mtime = dt.datetime.fromtimestamp(st.st_mtime)
        if mtime > ago:
            analyze.analyze_threshold(path)
            # print("%s modified %s" % (path, mtime))
