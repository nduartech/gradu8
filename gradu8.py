class Student:
    def __init__(self):
        self.taken = []
        self.major = ""
        self.concentration = ""
        self.lcs = ""

from flask import Flask
app = Flask(__name__)

my_server = Student()

@app.route("/")
def data():
    return my_server

if __name__ == "__main__":
    app.run(host="0.0.0.0")
