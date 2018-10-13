class Student:
    def __init__(self):
        self.taken = []
        self.degree = ""
        self.major = ""
        self.concentration = ""
        self.lcs = ""

from flask import Flask
app = Flask(__name__)

my_server = Student()

@app.route("/")
def data():
    my_server.degree = "BS"
    my_server.major = "CS"
    return my_server.degree + " in " + my_server.major


if __name__ == "__main__":
    app.run(host="0.0.0.0")
