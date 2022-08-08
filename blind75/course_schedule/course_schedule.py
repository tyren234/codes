def canFinish(numCourses : 'int', prerequisites : 'list[list[int]]') -> bool:
    requirements = {x:[] for x in range(numCourses)}
    # set up requirements
    for requirement in prerequisites:
        requirements[requirement[0]].append(requirement[1])

    visited = set()
    def oneCourse(course : int) -> bool:
        if course in visited:
            return False
        if requirements[course] == []:
            return True

        visited.add(course)

        for requirement in requirements[course]:
            if not oneCourse(requirement): return False
        visited.remove(course)
        requirements[course] = []
        return True

    for course in range(numCourses):
        if not oneCourse(course): return False
    return True


print(canFinish(5,[[0,1],[0,2],[1,3],[1,4],[3,4]]))
print(canFinish(20, [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]))
