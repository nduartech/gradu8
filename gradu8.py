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


class GlobalDictionary:
    
    classes = {}
    
    cs121 = Course(72717, "COMPSCI 121 Intro to Problem Solving w/ Computers", [], [72718], ["All"], 4)
    classes[72717] = cs121

    cs187 = Course(72718, "COMPSCI 187 Programming with Data Structures", [[72717]], [72724, 62041, 55482, 55555, 72773, 62073], ["All"], 4)
    classes[72718] = cs187

    m131 = Course(72684, "MATH 131 Calculus I", [[]], [76932, 72684], ["All"], 4)
    classes[72684] = m131

    m132 = Course(76932, "MATH 132 Calculus II", [[72684],[76889]], [78304, 51439], ["All"], 4)
    classes[76932] = m132

    m233 = Course(76889, "MATH 233 Multivariate Calculus", [[76932]], [], ["All"], 4)
    classes[76889] = m233

    s515 = Course(80027, "STATISTIC 515 Statistics I", [[76932],[76889]], [72764], ["All"], 3)
    classes[80027] = s515

    m235 = Course(76894, "MATH 235 Introduction to Linear Algebra", [[72684]], [55482, 61195, 62073], ["All"], 3)
    classes[76894] = m235

    cs220 = Course(72751, "COMPSCI 220 Programming Methodology", [[72718]], [72705, 72726, 72711, 72764, 55540, 72792, 72841, 61195, 55480], ["All"], 4)
    classes[72751] = cs220

    cs230 = Course(72752, "COMPSCI 230 Computer Systems Principles", [[72718]], [72705, 72711, 72709, 72764, 55540, 72792, 72807, 80798, 72767, 72841, 61195, 55480], ["All"], 4)
    classes[72752] = cs230

    cs240 = Course(72748, "COMPSCI 240 Reasoning Under Uncertainty", [[72718], [76932]], [72705, 72764, 55508, 55482, 55443, 62073], ["All"], 4)
    classes[72748] = cs240

    cs250 = Course(72721, "COMPSCI 250 Introduction To Computation", [[72718], [76932]], [72705, 72724, 80798, 72841], ["All"], 4)
    classes[72721] = cs250

    cs305 = Course(72705, "COMPSCI 305 Social Issues in Computing", [[72751, 72752], [72748, 72721]], [], ["All"], 3)
    classes[72705] = cs305
    #220 or 230, 240 or 250

    cs320 = Course(72726, "COMPSCI 320 Software Engineering", [[72751]], [80801], ["SOFTENG", "AI", "SRCHDATA", "ROBVISGR", "THEORYCMP", "CMPARCH", "NETWORK", "SOFTSYS", "PROGLANG"], 4)
    classes[72726] = cs320
    #220

    cs326 = Course(72711, "COMPSCI 326 Web Programming", [[72751, 72752]], [80801, 62579], [], 3)
    classes[72711] = cs326
    #220 or 230

    cs377 = Course(72709, "COMPSCI 377 Operating Systems", [[72752]], [72767, 72750, 62579], ["SOFTENG", "THEORYCMP", "CMPARCH", "SECURPRV", "NETWORK", "SOFTSYS", "PROGLANG"], 4)
    classes[72709] = cs377
    #230

    cs311 = Course(72724, "COMPSCI 311 Introduction to Algorithms", [[72718], [72721]], [55480], ["All"], 4)
    classes[72724] = cs311
    #187 and 250

    cs383 = Course(72764, "COMPSCI 838 Artifical Intelligence", [[72751, 72752], [72748, 80027]], [55508, 55443], ["AI", "ROBVISGR"], 3)
    classes[72724] = cs383
    #220 or 230 and 240 or 515

    c111 = Course(71902, "CHEM 111 Gen Chem-Sci", [[]], [71902], [], 4)
    classes[71902] = c111

    c112 = Course(71914, "CHEM 112 Gen Chem-Sci", [[71902]], [], [], 4)
    classes[71914] = c112
    #111

    cs345 = Course(62041, "COMPSCI 345 Practice and Applications of Data Management", [[72718]], [55480, 62579], [], 3)
    classes[62041] = cs345
    #187

    cs365 = Course(55540, "COMPSCI 365 Digital Forensics", [[72751, 72752]], [], ["SOFTENG", "SECURPRV"], 3)
    classes[55540] = cs365
    #220 or 230

    cs370 = Course(55508, "COMPSCI 370 Introduction to Computer Vision", [[72748, 72764]], [], ["AI", "ROBVISGR"], 3)
    classes[55508] = cs370
    #240 or 383

    cs373 = Course(55482, "COMPSCI 373 Introduction to Computer Graphics", [[72718], [76894, 72748]], [], [], 3)
    classes[55482] = cs373
    #187 and 235 or 240

    cs390N = Course(55555, "COMPSCI 390N Internet of Things", [[72718]], [], [], 3)
    classes[55555] = cs390N
    #187

    cs325 = Course(72712, "COMPSCI 325 Introduction to Human-Computer Interaction", [[]], [], ["SOFTENG", "SOFTSYS"], 3)
    classes[72712] = cs325

    cs328 = Course(72773, "COMPSCI 328 Mobile Health Sensing and Analytics", [[72718]], [], [], 3)
    classes[72773] = cs328
    #187

    cs335 = Course(72792, "COMPSCI 335 Inside the Box: How Computers Work", [[72751, 72752]], [], ["THEORYCMP", "SOFTSYS"], 3)
    classes[72792] = cs335
    #220 or 230

    cs391L = Course(72807, "COMPSCI 391L S-Computer Crime Law: Technologies of Investigation and Privacy", [[72752]], [], ["SECURPRV"], 3)
    classes[72807] = cs391L
    #230

    cs410 = Course(80798, "COMPSCI 410 Compiler Techniques", [[72752], [72721]], [], ["SOFTENG", "CMPARCH", "PROGLANG"], 3)
    classes[80798] = cs410
    #230 and 250

    cs453 = Course(72767, "COMPSCI 453 Computer Networks", [[72752, 72709]], [62579], ["SOFTENG", "THEORYCMP", "CMPARCH", "SECURPRV", "NETWORK", "SOFTSYS"], 3)
    classes[72767] = cs453
    #230 or 377

    cs460 = Course(72750, "COMPSCI 460 Introduction to Computer and Network Security", [[72709]], [62579], ["SOFTENG", "SECURPRV", "NETWORK", "SOFTSYS"], 3)
    classes[72750] = cs460
    #377
    
    cs491IP = Course(80801, "COMPSCI 491IP S-Programming the iPhone and iPad", [[72726, 72711]], [], [], 3)
    classes[80801] = cs491IP
    #320 or 326
                   
    cs497P = Course(72841, "COMPSCI 497P Special Topics - Programming Languages", [[72751], [72752], [72721]], [62579], [], 3)
    classes[72841] = cs497P
    #220 and 230 and 250
    
    cs403 = Course(61195, "COMPSCI 403 Introduction to Robotics: Perception, Mechanics, Dynamics & Control", [[76894], [72751, 72752]], [], ["AI", "ROBVISGR"], 3)
    classes[61195] = cs403
    #235 and 220 or 230
    
    cs445 = Course(55480, "COMPSCI 445 Information Systems", [[72751, 72752], [72724], [62041]], [], ["SOFTENG", "SRCHDATA", "THEORYCMP", "CMPARCH", "SECURPRV", "NETWORK", "SOFTSYS", "PROGLANG"], 3)
    classes[55480] = cs445
    #220 or 230, and 311 and 345

    cs446 = Course(55443, "COMPSCI 446 Search Engines", [[72748, 72764]], [], ["AI", "SRCHDATA"], 3)
    classes[55443] = cs446
    #240 or 383

    cs490P = Course(62579, "COMPSCI 490P Secure Distributed Systems", [[72711, 62041, 72709, 72767, 72750, 72841, ]], [], [], 3)
    classes[62579] = cs490P
    #326 or 345 or 377 or 453 or 460 or 497P

    cs491G = Course(55449, "COMPSCI 4901G S-Computer Networking Lab", [[72767]], [], ["NETWORK"], 3)
    classes[55449] = cs491G
    #453

    cs497C = Course(62073, "COMPSCI 497 C ST-Special Topics in Computer Graphics", [[72718], [76894, 72748]], [], [], 3)
    classes[62073] = cs497C
    #187 and 235 or 240


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
    core_Courses = set([72717,72718,72684,76932,76889,80027,76894,72752,72751,72748,72721,72705,72724,72726,72711])
    hundred3 = 0
    hundred4 = 0
    for semester in allSems:
        for course in semester:
            if course.ID in core_Courses:
                core_Courses.remove(course.ID)
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
    while not Optimal(allSems, student.credits) and len(nonCS) > 0:
        print("first loop")
        semester = []
        credits = 0
        while credits < 19 and not PQ.empty():
            print("second loop")
            print(credits)
            if not PQ.empty() and credits + PQ.peek().credits <= 19:
                course = PQ.get()
                explored[course.ID] = 1
                semester.append(course)
                student.taken.append(course.ID)

                credits += course.credits
            else:
                while credits <= 15 and len(nonCS) > 0:
                    print("third loop")
                    semester.append(nonCS.pop())
                    credits += 4
        student.credits += credits
        PQ = initializeQueue(student)
        allSems.append(semester)

    return allSems


@app.route("/")
def index():
    student = Student([72717,72684],"AI",8)
    schedule = fastPath(student)
    semester1 = schedule[0]
    class1 = semester1[0]
    return class1.name
    # return render_template('index.html')

@app.route("/student")
def student():
    return redirect(url_for('schedule'))

@app.route("/schedule")
def schedule():
    return render_template('schedule.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0")
