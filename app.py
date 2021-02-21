import os
import json
import pandas
from flask import Flask, jsonify, request, flash, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"txt", "pdf", "png", "jpg", "jpeg", "gif", "xls", "docx", "csv"}

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def read_file(filename):
    print("reading file name", filename)
    url = "uploads/" + filename
    print(url)
    df = pandas.read_csv(url)
    print(df.columns)
    result = df.to_json(orient="columns")
    parsed = json.loads(result)

    # f = open(url, "r")
    # print(f.read())
    return json.dumps(parsed, indent=4)


@app.route("/file", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if "file" not in request.files:
            flash("No file part")
            return "no file"
        file = request.files["file"]
        if file.filename == "":
            flash("No selected file")
            return "no file"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            message = {"status": 200, "message": "file Uploaded"}

            return read_file(filename)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/sum/<string:n>")
def getString(n):
    result = {
        "method": request.method,
        "data": request.form,
        "string": n,
        "recieved": True,
        "message": "its working good",
        "numbers": [2, 2, 2, 22, 2],
        "user": {"name": "Sagar sonwane", "age": 21, "isVergin": False},
    }
    return jsonify(result)


@app.route("/blog/<int:postID>")
def show_blog(postID):
    return "Blog Number %d" % postID


@app.route("/getData", methods=["POST", "GET"])
def getData():
    result = {
        "method": request.method,
        "data": request.form,
        "args": request.args,
        "files": request.files,
    }
    return jsonify(result)


def sum(a, b):
    return a + b


if __name__ == "__main__":
    app.run(debug=True)