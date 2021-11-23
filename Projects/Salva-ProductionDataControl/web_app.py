from flask import Flask, render_template
from main import historical_data


app = Flask(__name__)

# This is root - main page
@app.route("/")
def html_table():

    return render_template(
        "table.html", tables=[historical_data.to_html(classes="data")], titles=historical_data.columns.values
    )


app.run(debug=True)
