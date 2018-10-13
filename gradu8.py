from flask import Flask

app = Flask(__name__)

class Student(object):
	semester = ""
	taken = []
	concentration = ""

	def __init__(self,semester,taken,concentration):
		self.semester = semester
		self.taken = taken
		self.concentration = concentration

@app.route("/")
def hello():
	S = Student("FA18",[],"AI")
	return S.semester + " " + S.concentration

if __name__ == "__main__":
  app.run()
