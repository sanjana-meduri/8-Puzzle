import random
import collections
class Node:
    def __init__(self, state, parent):
        self.state = state
        self.parent = parent
        self.children = []
        self.dirFromParent = ""
    def addChild(self, child):
        self.children.append(child)
    def toString(self):
        return "" + str(self.state)

goalstate = "012345678"

def swap(s, i, j):
    l = list(str(s))
    l[i], l[j] = l[j], l[i]
    return "".join(l)
def inBounds(i):
    return i >= 0 and i < 9

def bfs(start_node):
    fringe = collections.deque()
    visited = set()
    fringe.append(start_node)
    while not len(fringe) == 0:
        v = fringe.popleft()
        if v.toString() == goalstate:
            return v
        dirs = "UDLR"
        for c in dirs:
            c = str(c)
            newStr = make_move(str(v.toString()), c)
            if newStr != "INVALID" and newStr not in visited and newStr != v.toString():
                child = Node(newStr, v)
                child.dirFromParent = c + ""
                v.addChild(child)
            visited.add(newStr)
        for c in v.children:
            fringe.append(c)
    return None


def make_move(str, dir):
    if dir == "U" and str.index("0") > 2:
        return swap(str, str.index("0"), str.index("0") - 3)
    if dir == "D" and str.index("0") < 6:
        return swap(str, str.index("0"), str.index("0") + 3)
    if dir == "R" and (str.index("0") - 2) % 3 != 0:
        return swap(str, str.index("0"), str.index("0") + 1)
    if dir == "L" and str.index("0") % 3 != 0:
        return swap(str, str.index("0"), str.index("0") - 1)
    return "INVALID"

def goal_test(str):
    return str == goalstate

def get_ij(str, i, j):
    return str[int(i) * 3 + int(j)]

def set_ij(str, i, j):
    newStr = (str + " ")[:-1]
    str[int(i) * 3 + int(j)] = newStr

def generateState():
    state = "012345678"
    dirs = "UDRL"
    rep = random.randrange(1000, 2000)
    for x in range(0, rep):
        newState = make_move(state, dirs[random.randrange(0, 4)])
        if newState != "INVALID":
            state = str(newState)
    print(state)
    print("# of shuffles:", rep)

def makeMatrix(s):
    s = str(s)
    s = s.replace("0", "_")
    return s[:3] + "\n" + s[3:6] + "\n" + s[6:]

def returnState():
    state = "012345678"
    dirs = "UDRL"
    rep = random.randrange(1000, 2000)
    for x in range(0, rep):
        newState = make_move(state, dirs[random.randrange(0, 4)])
        if newState != "INVALID":
            state = str(newState)
    return state

'''''
def generateState(maxMoves):
    state = "012345678"
    dirs = "UDRL"
    rep = random.randrange(0, maxMoves)
    for x in range(0, rep):
        newState = make_move(state, dirs[random.randrange(0, 4)])
        if newState != "INVALID":
            state = str(newState)
    print(state)
    #start with the goal state and randomly shuffle
'''

def printPath(start_node):
    goalNode = bfs(start_node)
    #moves = ""
    if goalNode != None:
        pointer = goalNode
        path = []
        while pointer.parent != None:
            path.append(pointer.parent.toString())
            #moves += (pointer.dirFromParent + ", ")
            pointer = pointer.parent
        path.reverse()
        path.append(goalNode.toString())
        print("Path: ", path)
        print("Total # of moves: ", len(path))
        #print("List of moves: " + moves[-2])
    else:
        print("There are no solutions to the puzzle you entered.")
'''''
def extension1():
    perms = set()
    count = 0
    solvable = 0
    maxPath = 0
    sumPath = 0
    while count < 1001:
        newStr = returnState()
        if newStr not in perms:
            perms.add(newStr)
            count += 1
    for s in perms:
        start_node = Node(s, None)
        path = returnPath(start_node)
        if path != None:
            solvable += 1
            sumPath += len(path)
            if len(path) > maxPath:
                maxPath = len(path)
    print("Solvable:", solvable + "/1000")
    print("Average Path Length:" + sumPath/solvable)
    print("Max Path Length", maxPath)
'''

def main():
    '''''
    max = input("Enter the max number of shuffles you want the state generator to perform.\t")
    generateState(int(max))
    '''''
    generateState()
    start = input("Enter the String.\t")
    printPath(Node(start, None))
    #print("Extension")
    #extension1()


if __name__ == "__main__":
    main()