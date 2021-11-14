@eel.expose
def predict():
    try:
        # Open dialog window where user can choose which files to use
        root = tk.Tk()
        root.withdraw()
        root.wm_attributes('-topmost', 1)
        title = 'Select file'

        source_path = filedialog.askopenfilename(title=title, filetypes=[("csv", ".csv")])

        config.update({'data': source_path, 'predicted_column': 2, 'plotit': 0, 'printit': 0, 'return_type': 'detailed_dictionary'})

        predictions = predictit.main.predict()

        result_df = predictions['complete_dataframe']

        if result_df.isnull().values.any():
            result_df = result_df.where(result_df.notnull(), None)

        result_dict = {'x_axis': result_df.index.to_list(), 'y_axis': result_df.values.T.tolist(), 'names': result_df.columns.values.tolist()}

        return result_dict

    except Exception:
        traceback.print_exc()
