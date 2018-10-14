class Student(object):

    #taken is a list of ints, each representing a courseID
    #the student has earned credit for
    taken = []

    #concentration is a string, representing the student's
    #desired concentration
    concentration = ""

    credits = -1

    def __init__(self,taken,concent,credits):
        self.taken = taken
        self.concentration = concent
        self.credits = credits


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

    def __init__(self,ID,name,preReqs,children,concentrations,credits):
        self.ID = ID
        self.name = name
        self.preReqs = preReqs
        self.children = children
        self.concentrations = concentrations
        self.credits = credits



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


def initializeQueue(student):

    #possible is a list of the possible courses
    #a student could take next semester
    possible = []

    gd = GlobalDictionary()

    for takenCourseID in student.taken:
        takenCourse = gd.classes[takenCourseID]

        for childID in takenCourse.children:
            childCourse = gd.classes[childID]
            possible.append(childCourse)

    toReturn = PriorityQueue()

    for possibleCourse in possible:
        if possibleCourse not in toReturn.courses and possibleCourse.ID not in student.taken and checkPreReqs(possibleCourse.preReqs,student.taken):
            toReturn.add(possibleCourse)

    return toReturn



def checkPreReqs(preReqs, taken):

    # preReqs is a list of lists and there needs to be something
    # in taken for each of the lists inside
    for list in preReqs:
        found = False
        for course in list:
            if course in taken:
                found = True
        if not found:
            return False
    return True


def Optimal(allSems, units):
    core_Courses = set(["CS121","CS187","MATH131","MATH132","MATH233","STAT515","MATH235","CS230","CS220","CS240","CS250","CS311","CS320","CS326"])
    hundred3 = 0
    hundred4 = 0
    for semester in allSems:
        for course in semester:
            if course.name in core_Courses:
                core_Courses.remove(course.name)
            elif course.name[2] == '3':
                hundred3 += 1
            elif course.name[2] == '4':
                hundred4 += 1

    return hundred3 >= 3 and hundred4 >= 3 and len(core_Courses) <=2 and units >= 120


def fastPath(student):
    allSems = []
    explored = {}
    PQ = initializeQueue(student)
    nonCS = set([Course(0,"CHEM111",[],[],[],4),Course(0,"GEOL101",[],[],[],4),Course(0,"ENG112",[],[],[],4),Course(0,"KIN100",[],[],[],4),Course(0,"COMP-LIT114",[],[],[],4),Course(0,"ANTHRO102",[],[],[],4),Course(0,"EDUCq115",[],[],[],4)])
    for tclass in student.taken:
        explored[tclass] = 1
    while not Optimal(allSems, student.units) and len(nonCS) > 0:
        semester = []
        credits = 0
        while credits < 19:
            if not PQ.empty() and credits + PQ.peek().credits <= 19:
                course = PQ.get()
                explored[course.ID] = 1
                semester.add(course)
                student.taken.add(course.code)
                credits += course.credits
            else:
                while credits <= 15 and len(nonCS) > 0:
                    semester.add(nonCS.pop())
                    credits += 4
        student.units += credits
        PQ = initializeQueue(student)
        allSems.add(semester)

    return allSems


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/student")
def student():
    return redirect(url_for('schedule'))

@app.route("/schedule")
def schedule():
    return render_template('schedule.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0")
