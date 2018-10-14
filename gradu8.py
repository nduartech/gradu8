import sys

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

    def __init__(self,ID,name,preReqs,children,concentrations,credits,level,priority):
        self.ID = ID
        self.name = name
        self.preReqs = preReqs
        self.children = children
        self.concentrations = concentrations
        self.credits = credits
        self.level = level
        self.priority = priority


class GlobalDictionary:
    
    classes = {}
    
    cs121 = Course(72717, "COMPSCI 121 Intro to Problem Solving w/ Computers", [], [72718], ["All"], 4, 1, 0)
    classes[72717] = cs121 

    cs187 = Course(72718, "COMPSCI 187 Programming with Data Structures", [[72717]], [72724, 62041, 55482, 55555, 72773, 62073, 72751,72752,72748,72721], ["All"], 4, 1, 0)
    classes[72718] = cs187

    m131 = Course(72684, "MATH 131 Calculus I", [[]], [76932,76894], ["All"], 4, 1, 0)
    classes[72684] = m131
    #72717, 72684

    m132 = Course(76932, "MATH 132 Calculus II", [[72684]], [76889,72748,72721], ["All"], 4, 1, 0)
    classes[76932] = m132

    m233 = Course(76889, "MATH 233 Multivariate Calculus", [[76932]], [], ["All"], 4, 2, 0)
    classes[76889] = m233

    # s515 = Course(80027, "STATISTIC 515 Statistics I", [[76932],[76889]], [72764], ["All"], 3, 1)
    # classs[80027] = s515

    m235 = Course(76894, "MATH 235 Introduction to Linear Algebra", [[72684]], [55482, 61195, 62073], ["All"], 3, 2, 0)
    classes[76894] = m235

    cs220 = Course(72751, "COMPSCI 220 Programming Methodology", [[72718]], [72705, 72726, 72764, 55540, 72792, 72841, 61195, 55480], ["All"], 4, 2, 0)
    classes[72751] = cs220

    cs230 = Course(72752, "COMPSCI 230 Computer Systems Principles", [[72718]], [72705, 72709, 72764, 55540, 72792, 72807, 80798, 72767, 72841, 61195, 55480], ["All"], 4, 2, 0)
    classes[72752] = cs230

    cs240 = Course(72748, "COMPSCI 240 Reasoning Under Uncertainty", [[72718], [76932]], [72705, 72764, 55508, 55482, 55443, 62073], ["All"], 4, 2, 0)
    classes[72748] = cs240

    cs250 = Course(72721, "COMPSCI 250 Introduction To Computation", [[72718], [76932]], [72705, 72724, 80798, 72841], ["All"], 4, 2, 0)
    classes[72721] = cs250

    cs305 = Course(72705, "COMPSCI 305 Social Issues in Computing", [[72751, 72752], [72748, 72721]], [], ["All"], 3, 3, 0)
    classes[72705] = cs305
    #220 or 230, 240 or 250 

    cs320 = Course(72726, "COMPSCI 320 Software Engineering", [[72751]], [80801], ["All"], 4, 3, 0)
    classes[72726] = cs320
    #220

    # cs326 = Course(72711, "COMPSCI 326 Web Programming", [[72751, 72752]], [80801, 62579], ["All"], 3)
    # classs[72711] = cs326
    #220 or 230     

    cs377 = Course(72709, "COMPSCI 377 Operating Systems", [[72752]], [72767, 72750, 62579], ["SOFTENG", "THEORYCMP", "CMPARCH", "SECURPRV", "NETWORK", "SOFTSYS", "PROGLANG"], 4, 3, 0)
    classes[72709] = cs377
    #230

    cs311 = Course(72724, "COMPSCI 311 Introduction to Algorithms", [[72718], [72721]], [55480], ["All"], 4, 3, 0)
    classes[72724] = cs311
    #187 and 250     

    cs383 = Course(72764, "COMPSCI 383 Artifical Intelligence", [[72751, 72752], [72748]], [55508, 55443], ["AI", "ROBVISGR"], 3, 3, 0)
    classes[72764] = cs383
    #220 or 230 and 240 or 515

    cs345 = Course(62041, "COMPSCI 345 Practice and Applications of Data Management", [[72718]], [55480, 62579], ["CMPARC"], 3, 3, 0)
    classes[62041] = cs345
    #187

    cs365 = Course(55540, "COMPSCI 365 Digital Forensics", [[72751, 72752]], [], ["SOFTENG", "SECURPRV"], 3, 3, 0)
    classes[55540] = cs365
    #220 or 230

    cs370 = Course(55508, "COMPSCI 370 Introduction to Computer Vision", [[72748, 72764]], [], ["AI", "ROBVISGR"], 3, 3, 0)
    classes[55508] = cs370
    #240 or 383

    cs373 = Course(55482, "COMPSCI 373 Introduction to Computer Graphics", [[72718], [76894, 72748]], [], [], 3, 3, 0)
    classes[55482] = cs373
    #187 and 235 or 240

    cs390N = Course(55555, "COMPSCI 390N Internet of Things", [[72718]], [], [], 3, 3, 0)
    classes[55555] = cs390N
    #187

    cs325 = Course(72712, "COMPSCI 325 Introduction to Human-Computer Interaction", [[]], [], ["SOFTENG", "SOFTSYS"], 3, 3, 0)
    classes[72712] = cs325

    cs328 = Course(72773, "COMPSCI 328 Mobile Health Sensing and Analytics", [[72718]], [], [], 3, 3, 0)
    classes[72773] = cs328
    #187

    cs335 = Course(72792, "COMPSCI 335 Inside the Box: How Computers Work", [[72751, 72752]], [], ["THEORYCMP", "SOFTSYS"], 3, 3, 0)
    classes[72792] = cs335
    #220 or 230

    cs391L = Course(72807, "COMPSCI 391L S-Computer Crime Law: Technologies of Investigation and Privacy", [[72752]], [], ["SECURPRV"], 3, 3, 0)
    classes[72807] = cs391L
    #230

    cs410 = Course(80798, "COMPSCI 410 Compiler Techniques", [[72752], [72721]], [], ["SOFTENG", "CMPARCH", "PROGLANG"], 3, 4, 0)
    classes[80798] = cs410
    #230 and 250

    cs453 = Course(72767, "COMPSCI 453 Computer Networks", [[72752, 72709]], [62579], ["SOFTENG", "THEORYCMP", "CMPARCH", "SECURPRV", "NETWORK", "SOFTSYS"], 3, 4, 0)
    classes[72767] = cs453
    #230 or 377

    cs460 = Course(72750, "COMPSCI 460 Introduction to Computer and Network Security", [[72709]], [62579], ["SOFTENG", "SECURPRV", "NETWORK", "SOFTSYS"], 3, 4, 0)
    classes[72750] = cs460
    #377
    
    cs491IP = Course(80801, "COMPSCI 491IP S-Programming the iPhone and iPad", [[72726]], [], [], 3, 4, 0)
    classes[80801] = cs491IP
    #320 or 326
                   
    cs497P = Course(72841, "COMPSCI 497P Special Topics - Programming Languages", [[72751], [72752], [72721]], [62579], [], 3, 4, 0)
    classes[72841] = cs497P
    #220 and 230 and 250
    
    cs403 = Course(61195, "COMPSCI 403 Introduction to Robotics: Perception, Mechanics, Dynamics & Control", [[76894], [72751, 72752]], [], ["AI", "ROBVISGR"], 3, 4, 0)
    classes[61195] = cs403
    #235 and 220 or 230
    
    cs445 = Course(55480, "COMPSCI 445 Information Systems", [[72751, 72752], [72724], [62041]], [], ["SOFTENG", "SRCHDATA", "THEORYCMP", "CMPARCH", "SECURPRV", "NETWORK", "SOFTSYS", "PROGLANG"], 3, 4, 0)
    classes[55480] = cs445
    #220 or 230, and 311 and 345

    cs446 = Course(55443, "COMPSCI 446 Search Engines", [[72748, 72764]], [], ["AI", "SRCHDATA"], 3, 4, 0)
    classes[55443] = cs446
    #240 or 383

    cs490P = Course(62579, "COMPSCI 490P Secure Distributed Systems", [[62041, 72709, 72767, 72750, 72841]], [], [], 3, 4, 0)
    classes[62579] = cs490P
    #326 or 345 or 377 or 453 or 460 or 497P

    cs491G = Course(55449, "COMPSCI 4901G S-Computer Networking Lab", [[72767]], [], ["NETWORK"], 3, 4, 0)
    classes[55449] = cs491G
    #453

    cs497C = Course(62073, "COMPSCI 497 C ST-Special Topics in Computer Graphics", [[72718], [76894, 72748]], [], [], 3, 4, 0)
    classes[62073] = cs497C
    #187 and 235 or 240

    cs503 = Course(81037, "COMPSCI 503 Embedded Computing Systems", [[72764, 61195]], [], ["AI"], 3, 5, 0)
    classes[81037] = cs503
    #383 or 403

    cs514 = Course(72796, "COMPSCI 514 Algorithms for Data Science", [[72748], [72724]], [], [], 3, 5, 0)
    classes[72796] = cs514
    #240 and 311

    cs520 = Course(72793, "COMPSCI 520 Theory and Practice of Software Engineering", [[72726]], [], ["SOFTENG", "CMPARCH"], 3, 5, 0)
    classes[72793] = cs520
    #320

    cs529 = Course(72749, "COMPSCI 529 Software Engineering Project Management", [[72726]], [], ["SOFTENG"], 3, 5, 0)
    classes[72749] = cs529
    #320

    cs575 = Course(80802, "COMPSCI 575 Combinatrics & Graph Theory", [[72721]], [], ["SOFTENG", "THEORYCMP"], 3, 5, 0)
    classes[80802] = cs575    
    #250
    
    cs585 = Course(55443, "COMPSCI 585 Introduction to Natural Language Processing", [[72748], [72751, 72752]], [72829], ["AI", "SRCHDATA"], 3, 5, 0)
    classes[72713] = cs585        
    #240 and 220 or 230

    cs589 = Course(72821, "COMPSCI 589 Machine Learning", [[72764], [76894]], [], ["AI"], 3, 5, 0)
    classes[72713] = cs589
    #383 and 235
        
    cs590A = Course(81567, "COMPSCI 590A System Defense and Test", [[]], [], [], 3, 5, 0)
    classes[81567] = cs590A

    cs590R = Course(72829, "COMPSCI 590R Applied Information Retrieval", [[72726], [72764, 55443, 55443]], [], [], 3, 5, 0)
    classes[72829] = cs590R         
    #320 and 383 or 446 or 585
    
    cs590S = Course(72801, "COMPSCI 590S Systems for Data Science", [[72724], [62041], [72709]], [], [], 3, 5, 0)
    classes[72801] = cs590S
    #311 and 345 and 377

    cs591M = Course(82434, "COMPSCI 591M Seminar-Bioinformatics and Computational Biology", [[72748, 80027]], [], [], 3, 5, 0)
    classes[82434] = cs591M
    #240 or 515
    
    cs592C = Course(82760, "COMPSCI 592C Seminar-Digital Civics", [[72751, 72752], [72712]], [], [], 3, 5, 0)
    classes[82760] = cs592C
    #220 or 230 and 325

    cs501 = Course(55423, "COMPSCI 501 Formal Language Theory", [[72724]], [], ["SOFTENG", "THEORYCMP", "CMPARCH"], 3, 5, 0)
    classes[55423] = cs501        
    #311

    cs535 = Course(55509, "COMPSCI 535 Computer Architecture", [[72792]], [], ["THEORYCMP", "CMPARCH", "SOFTSYS", "PROGLANG"], 3, 5, 0)
    classes[55509] = cs535        
    #335    

    cs590B = Course(61240, "COMPSCI 590B Detecting Interference in Networks", [[72767]], [], [], 3, 5, 0)
    classes[61240] = cs590B
    #453

    cs590C = Course(60945, "COMPSCI 590C Human Computer Interaction", [[72718], [72751, 72752]], [], [], 3, 5, 0)
    classes[60945] = cs590C
    #187 and 220 or 230

def createPriority(course,concentration):
        if not course.concentrations:
            return 0
        elif course.concentrations[0] == "All":
            return 10
        elif concentration in course.concentrations:
            return 5
        else:
            return 0

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


    def empty(self):
        return len(self.courses) == 0

    def peek(self):
        return self.courses[0]

    def get(self):
        i = 0
        global hundred3
        global hundred4
        if hundred3 >= 6:
            while i < len(self.courses)-1 and self.courses[i].level < 4:
                i += 1

        if self.courses[i].level == 3:
            hundred3 += 1
        elif self.courses[i].level >= 4:
            hundred4 += 1

        return self.courses.pop(i)


    def add(self,course):
        course.priority = createPriority(course,self.concentration)
        if course.priority == 0:
            self.courses.append(course)  
        elif course.priority == 10:
            self.courses.insert(0,course)
        else: 
            index = len(self.courses)
            while index > 0 and course.priority > self.courses[index-1].priority:
                index -= 1
            self.courses.insert(index,course)


from flask import Flask
from flask import render_template
app = Flask(__name__)
hundred3 = 0
hundred4 = 0

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
    toReturn.concentration = student.concentration

    #72717, 72684
    if len(student.taken) == 0:
        toReturn.add(gd.classes[72717])
        toReturn.add(gd.classes[72684])

    for possibleCourse in possible:
        if not checkID(possibleCourse,toReturn.courses) and possibleCourse.ID not in student.taken and checkPreReqs(possibleCourse.preReqs,student.taken):
            toReturn.add(possibleCourse)

    return toReturn

def checkID(possibleCourse,courses):
    for course in courses:
        if possibleCourse.ID == course.ID:
            return True
    return False

def checkPreReqs(preReqs, taken):

    # preReqs is a list of lists and there needs to be something
    # in taken for each of the lists inside
    for list in preReqs:
        found = False
        for course in list:
            if course == 72726:
                if 72711 in taken:
                    found = True
            if course == 72711:
                if 72726 in taken:
                    found = True
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
            elif course.name[8] == '3':
                hundred3 += 1
            elif course.name[8] == '4':
                hundred4 += 1

    return hundred3 >= 3 and hundred4 >= 3 and len(core_Courses) <=2 and units >= 120


def printSemester(semester,count):
    for course in semester:
        print(course.name)
    print('SEMESTER '+str(count))
    print('~')


def majorComplete(allSems, units):
    core_Courses = set([72717,72718,72684,76932,76889,72752,72751,76894,72748,72721,72705,72726,72724])
    global hundred3 
    global hundred4 
    for semester in allSems:
        for course in semester:
            if course.ID in core_Courses:
                core_Courses.remove(course.ID)

    return hundred3 >= 3 and hundred4 >= 3 and len(core_Courses) <= 1


def fastPath(student, creditThreshold):
    allSems = []
    explored = {}
    PQ = initializeQueue(student)
    nonCS = set([Course(0,"CHEMISTRY 111",[],[],[],4,1,0),Course(0,"GEOLOGY 101",[],[],[],4,1,0),Course(0,"ENGLISH 112",[],[],[],4,1,0),Course(0,"KINIES 100",[],[],[],4,1,0),Course(0,"COMP-LIT 114",[],[],[],4,1,0),Course(0,"ANTHRO 102",[],[],[],4,1,0),Course(0,"EDUCATION 115",[],[],[],4,1,0)])
    for tclass in student.taken:
        explored[tclass] = 1

    count = 1
    while True:
        semester = []
        credits = 0
        genEds = 0
        while credits < creditThreshold:
            while credits <= (creditThreshold-4) and len(nonCS) > 0:
                if genEds >= 2:
                    break
                semester.append(nonCS.pop())
                credits += 4
                genEds += 1

            if not PQ.empty() and (credits + PQ.peek().credits) <= creditThreshold:
                course = PQ.get()
                explored[course.ID] = 1
                semester.append(course)
                student.taken.append(course.ID)
                credits += course.credits

            if credits > (creditThreshold-4):
                break
        
        semester.append(Course(0,"Choose " + str(creditThreshold - credits)+ " credit course",[],[],[],creditThreshold-credits,1,0))   
        printSemester(semester,count)
        student.credits += creditThreshold
        PQ = initializeQueue(student)
        allSems.append(semester)
        count += 1
        global hundred3
        global hundred4
        if hundred3 >= 3 and hundred4 >= 3:
            credits_left = 0 if 120-student.credits < 0 else 120-student.credits
            print("You're major requirements are complete! Units to graduation: " + str(credits_left))
            return allSems

    return allSems


@app.route("/")
def index():
    return render_template('init.html')

@app.route("/student", methods = ['POST','GET'])
def student():
        s = Student([72717,72684],"AI",8)
        schedule = fastPath(s,19)
        return render_template('display.html',schedule)

if __name__ == "__main__":
    app.run(debug = True)
