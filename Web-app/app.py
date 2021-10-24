from flask import Flask, render_template, redirect, jsonify, abort

app = Flask(__name__)

# This is root - main page
@app.route("/")
def hello_world():
    return "<p>Welcome</p>"


# This is example of another route
@app.route("/hello")
def hello():
    return "Hello, World"


# Example of query parameter
@app.route("/user/<username>")
def get_user(username):
    return f"Hello, {username}"


# Example of using template
@app.route("/template")
def template():
    return render_template("mypage.html")


# Example of using css
# Example css taken from https://codepen.io/miroot/pen/qwIgC
@app.route("/templatecss")
def templatecss():
    return render_template("mypagecss.html")


# Example of using static file
@app.route("/image")
def image():
    return render_template("image.html")


# Example of redirect
@app.route("/redirectpage")
def redirectpage():
    return redirect("/")


# Example of returning data
@app.route("/data")
def data():
    mydata = {"One": 1, "Two": 2}
    return jsonify(mydata)


# Example of POST method
var = []


@app.route("/edit", methods=["POST"])
def edit():
    var.append(666)

    # If want to send response code
    # return f"{var}", 202

    return f"{var}"


# Example of return error code


@app.route("/forbiden")
def forbiden():
    abort(401, description="Login first.")
