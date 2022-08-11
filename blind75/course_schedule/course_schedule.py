def canFinish(numCourses : 'int', prerequisites : 'list[list[int]]') -> bool:
    requirements = dict()
    # set up requirements
    for requirement in prerequisites:
        if requirement[0] in requirements:
            requirements[requirement[0]].append(requirement[1])
        else:
            requirements[requirement[0]] = [requirement[1]]

    currentlyVisiting = []

    def oneCourse(courseNumber : 'int') -> bool:
        if courseNumber not in requirements:
            return True
        elif courseNumber in currentlyVisiting:
            return False
        else:
            currentlyVisiting.append(courseNumber)
            for requirement in requirements[courseNumber]:
                if oneCourse(requirement) == False: return False
            return True

    return oneCourse(0)

print(canFinish(5,[[0,1],[0,2],[1,3],[1,4],[3,4]]))
