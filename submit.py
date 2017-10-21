
#do not modify the function names
#You are given L and M as input
#Each of your functions should return the minimum possible L value alongside the marker positions
#Or return -1,[] if no solution exists for the given L


# Variables = {0, M1, M2, M3, ...., M, L}
# Domain = {0,1, 2, 3, 4, ...., L}
# Constraints = Difference between each pair of markers has to be unique
# {M1-0 != M2- M1 != M3-M2 !=...., != ML - ML-1 != M3 - M1 != M4 - M1 !=.....}

# At each step, we pick a variable from the list and check the difference of the variable
# against all the already present differences in our set. We we find any difference already
# present, that means the constrain is not satisfied, so we do not add this variable to our
# solution list. When we are backtracking, the variable to be removed from the solution list,
# we remove all the unique differences that we inserted while adding it to the solution list.

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

# In Forward checking, we propagate the information from assigned variables to unassigned
# variables. We keep track of remaining legal values in domain for unassigned variables.
# As soon as any variable does not have any legal value in its domain, we backtrack. It
# # helps in early detection of failure. For implementation, as soon as we assign a mark
# we remove that variable from our domain. Along with this, we also remove the differences
# of that variable with other variables already present in our solution list.

def forwardChecking(start, marks, domain, status, M):

    if len(domain) < (M-2):
        return False

    if status:
        for item in marks:
            d1 = abs(item - start)
            if d1 in domain:
                domain.remove(d1)

    else:
        for item in marks:
            d1 = abs(item - start)
            if d1 not in domain:
                domain.append(d1)
    return True

# Recursive Backtracking looks for assignment for each variable from domain
# where the constraint is satisfied. If keeps on assigning consistent values
# to variables, if M marks are assigned, a solution is found. Else if we rea
# ch the end of the domain, we backtrack the last assigned value. Repeat the
# process for each assigned value, if solution is not found. Moreover, if for
# given L, a solutions exists, we check for L-1 for a solution the same way.
# We continue until for any 'l', no solution exists. We return the 'l+1' as
# our optimal solution.

def recursiveBacktracking(l, M, start, marks, domain, difference, isFc):
    global flag
    global ans

    if start >= l or flag == 1 or len(domain) < (M - 2):
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
            return 1

        if isFc:
            forwardChecking(start, marks, domain, True, M)
        if start + 1 in domain:
            recursiveBacktracking(l, M, start+1, marks, domain, difference, isFc)

        contraintCheck(marks, start, difference, False)
        domain.append(start)

        if isFc:
            forwardChecking(start, marks, domain, False, M)

    recursiveBacktracking(l, M, start+1, marks, domain, difference, isFc)

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
