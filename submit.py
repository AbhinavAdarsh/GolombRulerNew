#do not modify the function names
#You are given L and M as input
#Each of your functions should return the minimum possible L value alongside the marker positions
#Or return -1,[] if no solution exists for the given L

import time
start_time = time.time()

def contraintCheck(newmarks, mark, newdifference, status):
    # print "DiFF Before = ", newdifference
    temp = set()

    if status == True:
        for point in newmarks:
            diff = abs(mark - point)
            if diff not in newdifference and diff not in temp:
                temp.add(diff)
            else:
                return False

        for item in temp:
            newdifference.add(item)
    else:
       # print "mark in check", mark
        newmarks.remove(mark)
        for point in newmarks:
            diff = abs(mark - point)
            newdifference.remove(diff)
    # print "DiFF After = ", newdifference
    return True



def forwardChecking(start, newmarks, newdomain, status):
    if len(newdomain) == 0:
        return False

    if status == True:
        for item in newmarks:
            if item != start and abs(item - start) in newmarks:
                newdomain.remove(abs(item - start))
    else:
        for item in newmarks:
            if item != start:
                newdomain.append(start+item)

    return True

def recursiveBacktracking(L, M, start, newmarks, newdomain, newruler, newdifference, isFc):
    global flag
    global ans

    if start >= L or flag == 1 or len(newdomain) == 0:
        return
    #print "Marks =", newmarks, "start = ", start

    if contraintCheck(newmarks, start, newdifference, True) is True:
        newmarks.append(start)
        if isFc == False:
            newdomain.remove(start)
        if len(newmarks) == M:
            # print "Solution Found"
            newmarks.sort()
            # print "Sol =", newmarks
            if flag == 0:
                ans = newmarks[:]
                # print "Ans = ", ans
            flag = 1
            return newmarks[-1], newmarks
        if isFc == True:
            forwardChecking(start, newmarks, newdomain, True)

        recursiveBacktracking(L, M, start+1, newmarks, newdomain, newruler, newdifference, isFc)
        #print "backtrack ", start
        contraintCheck(newmarks, start, newdifference, False)
        #newmarks.remove(start)
        if isFc == False:
            newdomain.append(start)
        else:
            forwardChecking(start, newmarks, newdomain, False)

    recursiveBacktracking(L, M, start+1, newmarks, newdomain, newruler, newdifference, isFc)

#Your backtracking function implementation
def BT(L, M):


    final = []

    #For Case (L, M) = (1,2)
    if L == 1 and M == 2:
        return 1,[0,1]

    for l in range(L,0,-1):
        global ans
        global flag
        ans = []
        marks = [0,l]
        ruler = range(1,l)
        domain = range(1,l)
        difference = set()
        flag = 0
        recursiveBacktracking(l, M, 1, marks, domain, ruler, difference, False)
        #print l, "ans = ", ans
        if len(ans) != 0:
            final = ans[:]
        else:
            break

    if len(final) != 0:
        return final[-1],final

    "*** YOUR CODE HERE ***"
    return -1,[]


# Variables = {0, M1, M2, M3, ...., M, L}
# Domain = {1, 2, 3, 4, ...., L}
# Constraints = Difference between each pair of markers has to be unique
# {M1-0 != M2- M1 != M3-M2 !=...., != ML - ML-1 != M3 - M1 != M4 - M1 !=.....}

#Your backtracking + forwardchecking function implementation
def FC(L, M):

    final = []

    #For Case (L, M) = (1,2)
    if L == 1 and M == 2:
        return 1,[0,1]

    for l in range(L,0,-1):
        global ans
        global flag
        ans = []
        marks = [0,l]
        ruler = range(1,l)
        domain = range(1,l)
        difference = set()
        flag = 0
        recursiveBacktracking(l, M, 1, marks, domain, ruler, difference, True)
        #print l, "ans = ", ans
        if len(ans) != 0:
            final = ans[:]
        else:
            break

    if len(final) != 0:
        return final[-1],final

    "*** YOUR CODE HERE ***"
    return -1,[]

#Bonus: backtracking + constraint propagation
def CP(L, M):
    "*** YOUR CODE HERE ***"
    return -1,[]

flag = 0
ans = []
print BT(11,5)

flag = 0
ans = []
print FC(25,7)

print("--- %s seconds ---" % (time.time() - start_time))