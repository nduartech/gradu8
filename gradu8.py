class Student:
    def __init__(self):
        self.name = ""
        self.taken = []
        self.degree = "B.S."
        self.major = "Computer Science"
        self.concentration = ""

from flask import Flask, render_template, request
app = Flask(__name__)
app.secret_key = 's3cr3t'

my_server = Student()

def setup():
    return "hi"

@app.route("/")
def init():
    my_server.degree = "BS"
    my_server.major = "CS"
    return printHi()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
