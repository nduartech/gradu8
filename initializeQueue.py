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
            
            
            
            
