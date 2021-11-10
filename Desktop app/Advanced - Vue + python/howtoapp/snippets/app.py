import pandas as pd
import eel
import tkinter as tk
from tkinter import filedialog 
from pathlib import Path
import sys
import traceback
import predictit
import multiprocessing

devel=1

@eel.expose
def predict():
    try:
        root = tk.Tk()
        root.withdraw()
        root.wm_attributes('-topmost', 1)

        source_path = filedialog.askopenfilename(filetypes=[("csv", ".csv")])

        predictions = predictit.main.predict(data=source_path, predicted_column=2, plotit=0, printit=0, return_type='detailed_dictionary')

        result_df = predictions['complete_dataframe']

        if result_df.isnull().values.any():
            result_df = result_df.where(result_df.notnull(), None)

        return {'x_axis': result_df.index.to_list(), 'y_axis': result_df.values.T.tolist(), 'names': result_df.columns.values.tolist()}

    except Exception:
        multiprocessing.freeze_support()
        traceback.print_exc()


def run_gui(devel):

    if getattr(sys, 'frozen', False):
        gui_path = Path(sys._MEIPASS) / 'gui'
    else:
        gui_path = Path(__file__).resolve().parent / 'gui'

    if devel:
        directory = gui_path / 'src'
        app = None
        page = {'port': 8080}

        def close_callback(page, sockets):
            pass

    else:
        directory = gui_path /'dist'
        close_callback = None
        app = 'chrome'
        page = 'index.html'

    eel.init(directory.as_posix(), ['.vue', '.js', '.html'])

    eel.start(page, mode=app, cmdline_args=['--disable-features=TranslateUI'], close_callback=close_callback, host='localhost', port=8686, disable_cache=True),


if __name__ == '__main__':
    multiprocessing.freeze_support()
    try:
        run_gui(devel)
    except Exception:
        traceback.print_exc()
