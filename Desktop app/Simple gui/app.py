import eel
import tkinter as tk
from tkinter import filedialog
import traceback
import plotly as pl
import mydatapreprocessing as mdp

import config


def load_data(source_path):

    data = mdp.load_data.load_data(
        source_path,
        request_datatype_suffix=config.request_datatype_suffix,
        predicted_table=config.predicted_table,
    )
    data = mdp.preprocessing.data_consolidation(data)
    data, _, _ = mdp.preprocessing.preprocess_data(data, standardizeit="standardize")

    fig = pl.graph_objs.Figure()

    for i in data.columns:
        fig.add_trace(pl.graph_objs.Scatter(x=data.index, y=data[i], name=i))

    fig.layout.update(
        yaxis=dict(title="Values"),
        showlegend=True,
        legend_orientation="h",
        paper_bgcolor="#d9f0e8",
        hoverlabel={"namelength": -1},
        height=400,
        margin={"b": 35, "t": 35, "pad": 4},
    )

    plot_div = pl.offline.plot(fig, include_plotlyjs=False, output_type="div")

    #                  'content', 'into_paragraph', 'id_parent', 'id_created', 'label', 'added_class'
    eel.add_HTML_element(plot_div, False, "plot_container", "plot", "Interactive plot", ["plot"])
    eel.execute("plot_container")


@eel.expose
def load_data_from_file():
    try:
        root = tk.Tk()
        root.withdraw()
        root.wm_attributes("-topmost", 1)

        source_path = filedialog.askopenfilename(filetypes=[("csv", ".csv")])
        load_data(source_path)

    except Exception:
        traceback.print_exc()


@eel.expose
def load_data_from_url(url):
    try:
        load_data(url)

    except Exception:
        traceback.print_exc()


def run_gui():

    eel.init("gui")

    eel.start(
        "index.html",
        mode="chrome",
        cmdline_args=["--disable-features=TranslateUI"],
        host="localhost",
        disable_cache=True,
    ),


if __name__ == "__main__":

    try:
        run_gui()

    except Exception:
        traceback.print_exc()
