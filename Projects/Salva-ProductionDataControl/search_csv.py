import os
import datetime as dt

now = dt.datetime.now()
ago = now - dt.timedelta(minutes=30)

for root, dirs, files in os.walk("data"):
    for fname in files:
        path = os.path.join(root, fname)
        st = os.stat(path)
        mtime = dt.datetime.fromtimestamp(st.st_mtime)
        if mtime > ago:
            print("%s modified %s" % (path, mtime))
