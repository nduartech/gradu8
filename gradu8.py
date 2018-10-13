class Student(object):
    
    #taken is a list of ints, each representing a courseID
    #the student has earned credit for
    taken = []
    
    #concentration is a string, representing the student's
    #desired concentration
    concentration = ""

    def __init__(self,taken,concent):
        self.taken = taken
        self.concentration = concent

    
class Course(object):
        
    #If the ID is -1, it hasn't been initialized
    ID = -1
    
    name = ""
    
    #pre-reqs is a list of lists, each one representing
    #the pre-reqs (two elements in the list is an either/or situation)
    preReqs = []
    
    #children is a list of ints, each representing a courseID
    children = []
    
    #concentrations is a list of strings, each representing a concentration type
    #"All" means it's required, and should have a high priority
    concentrations = []
    
    #If credits is -1, it hasn't been properly initialized
    credits = -1

    def __init__(self,ID,name,preReqs,children,concentrations):
        self.ID = ID
        self.name = name
        self.preReqs = preReqs
        self.children = children
        self.concentrations = concentrations


class PriorityQueue(object):
    courses = []
    concentration = ""
    size = 0

    def __init__(self):
        self.courses = []
        self.concentration = ""
        self.size = 0

    def empty(self):
        return self.size == 0

    def peek(self):
        return self.courses[0]

    def get(self):
        self.size -= 1
        return self.courses.pop(0)

    def add(self,course):
        if self.concentration not in course.concentrations and "All" not in course.concentrations:
            self.courses.append(course)
        elif course.concentrations[0] == "All":
            self.courses.insert(0,course)
        else:
            index = len(courses)
            while concentration not in self.courses[index-1].concentrations:
                index -= 1
            self.courses.insert(index,course)

        self.size += 1


from flask import Flask
app = Flask(__name__)


@app.route("/")
def data():
    PQ = PriorityQueue()
    course1 = Course(1,"CS121",[],[],[])
    PQ.add(course1)

    course = PQ.get()
    return course.name

if __name__ == "__main__":
    app.run(host="0.0.0.0")
