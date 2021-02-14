from flask import Flask, jsonify, request

app = Flask(__name__)


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
    result = {"method": request.method, "data": request.form, "args": request.args,, "files":request.files}
    return jsonify(result)


def sum(a, b):
    return a + b


if __name__ == "__main__":
    app.run(debug=True)