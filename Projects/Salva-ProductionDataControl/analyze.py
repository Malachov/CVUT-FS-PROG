import analyze
import pandas as pd


def analyze_threshold(path):
    col_list = ["teplota"]
    df = pd.DataFrame()
    df = pd.read_csv(path, usecols=col_list)
    return df
