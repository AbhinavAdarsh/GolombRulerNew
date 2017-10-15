#do not modify the function names
#You are given L and M as input
#Each of your functions should return the minimum possible L value alongside the marker positions
#Or return -1,[] if no solution exists for the given L


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
    # print "Marks =", newmarks, "start = ", start

    if contraintCheck(newmarks, start, newdifference, True) is True:
        newmarks.append(start)
        newdomain.remove(start)
        if len(newmarks) == M:
            print "Solution Found"
            newmarks.sort()
            # print "Sol =", newmarks
            if flag == 0:
                ans = newmarks[:]
                # print "Ans = ", ans
            flag = 1
            return newmarks[-1], newmarks

        recursiveBacktracking(L, M, start+1, newmarks, newdomain, newruler, newdifference)
        # print "backtrack ", start
        contraintCheck(newmarks, start, newdifference, False)
        #newmarks.remove(start)
        newdomain.append(start)

    recursiveBacktracking(L, M, start+1, newmarks, newdomain, newruler, newdifference)


def BT(L, M, start):
    global ans
    marks = [0,L]
    ruler = range(1,L)
    domain = range(1,L)
    difference = set()

    recursiveBacktracking(L, M, 1, marks, domain, ruler, difference)

    if len(ans) != 0:
        return ans[-1],ans

    return -1, []
    "*** YOUR CODE HERE ***"
    # return -1,[]
flag = 0
ans = []
print BT(6,4,1)
flag = 0
ans = []
print BT(85,12,1)



#Your backtracking+Forward checking function implementation
def FC(L, M):
    "*** YOUR CODE HERE ***"
    return -1,[]

#Bonus: backtracking + constraint propagation
def CP(L, M):
    "*** YOUR CODE HERE ***"
    return -1,[]


