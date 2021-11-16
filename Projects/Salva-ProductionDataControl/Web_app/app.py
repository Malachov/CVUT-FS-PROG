from flask import Flask, render_template, redirect, jsonify, abort

# TODO vytisknout tabulku historical_data - knihovna tabulate

app = Flask(__name__)

# This is root - main page
@app.route("/")
def hello_world():
    return "<p>Welcome</p>"


app.run(debug=True)
