import pandas as pd
import eel
from pathlib import Path
import sys
import traceback
import predictit
import pandas

devel=0


def predict(stop):

    my_data = pd.read_csv("https://raw.githubusercontent.com/jbrownlee/Datasets/master/daily-min-temperatures.csv")
    predictions = predictit.main.predict(data=my_data.iloc[:stop], predicted_column="Temp", use_config_preset="fast", plotit=0, debug=0, printit=0, return_type='detailed_dictionary')
    result_df = predictions['complete_dataframe']
    if result_df.isnull().values.any():
        result_df = result_df.where(result_df.notnull(), None)
    eel.draw_plot({'x_axis': result_df.index.to_list(), 'y_axis': result_df.values.T.tolist(), 'names': result_df.columns.values.tolist()})


def run_gui(devel):

    gui_path = Path(__file__).resolve().parent / 'gui'

    def close_callback(page, sockets):
        pass
    app = None

    if devel:
        directory = gui_path / 'src'
        page = {'port': 8080}

    else:
        directory = gui_path /'dist'
        page = 'index.html'

    eel.init(directory.as_posix(), ['.vue', '.js', '.html'])

    eel.start(page, block=False, mode=app, cmdline_args=['--disable-features=TranslateUI'], close_callback=close_callback, host="localhost", port=8686, disable_cache=True),

    stop = 500

    while True:
        try:
            predict(stop)
            eel.sleep(1.0)
            stop += 10
        except:
            break


if __name__ == '__main__':

    try:
        run_gui(devel)
    except Exception:
        traceback.print_exc()

