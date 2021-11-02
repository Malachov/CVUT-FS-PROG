import pandas as pd
import numpy as np

from pathlib import Path

mypath = (
    r"C:\Users\ondre\Desktop\ČVUT\NMG\Programování\CVUT-FS-PROG\Projects\Salva-ProductionDataControl\data"
)

for i in Path(mypath).glob("*"):
    print(i)
