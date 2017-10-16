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

#Your backtracking function implementation
def recursiveBacktracking(L, M, start, newmarks, newdomain, newruler, newdifference):
    global flag
    global ans

    if start >= L or flag == 1:
        return
    #print "Marks =", newmarks, "start = ", start

    if contraintCheck(newmarks, start, newdifference, True) is True:
        newmarks.append(start)
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

        recursiveBacktracking(L, M, start+1, newmarks, newdomain, newruler, newdifference)
        #print "backtrack ", start
        contraintCheck(newmarks, start, newdifference, False)
        #newmarks.remove(start)
        newdomain.append(start)

    recursiveBacktracking(L, M, start+1, newmarks, newdomain, newruler, newdifference)

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
        recursiveBacktracking(l, M, 1, marks, domain, ruler, difference)
        #print l, "ans = ", ans
        if len(ans) != 0:
            final = ans[:]
        else:
            break

    if len(final) != 0:
        return final[-1],final

    "*** YOUR CODE HERE ***"
    return -1,[]


#Your backtracking+Forward checking function implementation
def FC(L, M):

    "*** YOUR CODE HERE ***"
    return -1,[]

#Bonus: backtracking + constraint propagation
def CP(L, M):
    "*** YOUR CODE HERE ***"
    return -1,[]

flag = 0
ans = []
print BT(1,2)
print("--- %s seconds ---" % (time.time() - start_time))