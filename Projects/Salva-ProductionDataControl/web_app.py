from flask import Flask, render_template
import pandas as pd

historical_data = pd.read_csv("historical_data.csv")
historical_data.set_index("id", drop=True, inplace=True)

app = Flask(__name__)

# This is root - main page
@app.route("/")
def html_table():
    historical_data = pd.read_csv("historical_data.csv")
    historical_data.set_index("id", drop=True, inplace=True)
    return render_template(
        "table.html", tables=[historical_data.to_html(classes="data")], titles=historical_data.columns.values
    )


app.run(debug=True)
