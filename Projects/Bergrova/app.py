import os
from flask import Flask, render_template, redirect, url_for, request, flash
from werkzeug.utils import secure_filename
from check import check

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'xlsx'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def front_page():
    return render_template("front_page.html")

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/upload", methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        for x in ['file', 'file2']:
            # check if the post request has the file part
            if x not in request.files:
               flash('No file part')
               return redirect(request.url)
            file = request.files[x]
            # If the user does not select a file, the browser submits an
            # empty file without a filename.
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('kontrola'))
    return render_template("upload.html")

@app.route("/kontrola", methods=['GET', 'POST'])
def kontrola():
    if request.method == 'POST':
        LT = request.form["LT"]
        LT_end = request.form["LT_end"]
        results = render_template("results.html")
        answ = check(LT, LT_end)
        return results.format(answ[0],answ[1],answ[2])
        

    return render_template("kontrola.html")
