
#do not modify the function names
#You are given L and M as input
#Each of your functions should return the minimum possible L value alongside the marker positions
#Or return -1,[] if no solution exists for the given L


# Variables = {0, M1, M2, M3, ...., M, L}
# Domain = {1, 2, 3, 4, ...., L}
# Constraints = Difference between each pair of markers has to be unique
# {M1-0 != M2- M1 != M3-M2 !=...., != ML - ML-1 != M3 - M1 != M4 - M1 !=.....}

import time
start_time = time.time()

def contraintCheck(marks, mark, difference, status):

    temp = set()

    if status:
        for point in marks:
            diff = abs(mark - point)
            if diff not in difference and diff not in temp:
                temp.add(diff)
            else:
                return False

        for item in temp:
            difference.add(item)
    else:

        marks.remove(mark)
        for point in marks:
            diff = abs(mark - point)
            difference.remove(diff)

    return True


def forwardChecking(start, marks, domain, status):

    if len(domain) == 0:
        return False

    if status:
        for item in marks:
            if item != start and abs(item - start) in domain:
                domain.remove(abs(item - start))
    else:
        for item in marks:
            if item != start and abs(start - item) not in domain:
                domain.append(abs(start - item))
    return True

def recursiveBacktracking(L, M, start, marks, domain, difference, isFc):
    global flag
    global ans

    if start >= L or flag == 1 or len(domain) == 0:
        return

    if contraintCheck(marks, start, difference, True) is True:
        marks.append(start)
        if not isFc:
            domain.remove(start)
        if len(marks) == M:
            marks.sort()
            if flag == 0:
                ans = marks[:]
            flag = 1
            return marks[-1], marks

        if isFc:
            forwardChecking(start, marks, domain, True)
        if start + 1 in domain:
            recursiveBacktracking(L, M, start+1, marks, domain, difference, isFc)

        contraintCheck(marks, start, difference, False)
        domain.append(start)

        if isFc:
            forwardChecking(start, marks, domain, False)

    recursiveBacktracking(L, M, start+1, marks, domain, difference, isFc)

#Your backtracking function implementation

def BT(L, M):

    final = []

    for l in range(L,0,-1):
        global ans
        global flag
        ans = []
        marks = [0,l]
        domain = range(1,l)
        difference = set()
        flag = 0

        if not domain:
            return marks
        recursiveBacktracking(l, M, 1, marks, domain, difference, False)

        if len(ans):
            final = ans[:]
        else:
            break

    if len(final):
        return final[-1],final

    "*** YOUR CODE HERE ***"
    return -1,[]

#Your backtracking + forwardchecking function implementation

def FC(L, M):

    final = []

    for l in range(L,0,-1):
        global ans
        global flag
        ans = []
        marks = [0,l]
        domain = range(1,l)
        difference = set()
        flag = 0

        if not domain:
            return marks
        recursiveBacktracking(l, M, 1, marks, domain, difference, True)

        if len(ans):
            final = ans[:]
        else:
            break

    if len(final):
        return final[-1],final

    "*** YOUR CODE HERE ***"
    return -1,[]

#Bonus: backtracking + constraint propagation

def CP(L, M):
    "*** YOUR CODE HERE ***"
    return -1,[]


#print BT(6,4)
print FC(6,4)

print("--- %s seconds ---" % (time.time() - start_time))
