import random
import collections
from time import time

goalstate = "012345678"

class Node:
    def __init__(self, state, parent):
        self.state = state
        self.parent = parent
        self.children = []
        self.dirFromParent = ""
        if self.parent == None:
            self.depth = 0
        else:
            self.depth = self.parent.depth + 1
    def addChild(self, child):
        self.children.append(child)
    def toString(self):
        return "" + str(self.state)

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
        for c in v.children:
            fringe.append(c)
            visited.add(c.state)
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

def makeMatrix(s):
    s = str(s)
    s = s.replace("0", "_")
    return " ".join(list(s[:3])) + "\n" + " ".join(s[3:6]) + "\n" + " ".join(s[6:]) + "\n"

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

def getLength(start_node):
    goalNode = bfs(start_node)
    moves = ""
    if goalNode != None:
        pointer = goalNode
        path = []
        while pointer.parent != None:
            path.append(pointer.parent.toString())
            moves += (pointer.dirFromParent + ", ")
            pointer = pointer.parent
        path.reverse()
        path.append(goalNode.toString())
        return (str(len(path)))
    else:
        return ("There are no solutions to the puzzle you entered.")

def printPath(start_node):
    goalNode = bfs(start_node)
    moves = ""
    if goalNode != None:
        pointer = goalNode
        path = []
        while pointer.parent != None:
            path.append(pointer.parent.toString())
            moves += (pointer.dirFromParent + ", ")
            pointer = pointer.parent
        path.reverse()
        path.append(goalNode.toString())
        print("Path: ")
        for s in path:
            print(makeMatrix(s))
        print("Length of path:", len(path))
        if len(moves[:-2]) == 0:
            print("# of moves:", 0)
            print("List of moves: NO MOVES")
        else:
            print("# of moves:", len(moves[:-2].split(", ")))
            print("List of moves:", moves[:-2])
    else:
        print("There are no solutions to the puzzle you entered.")

def main():
    #generateState()
    #start = input("Enter the String.\t")
   # printPath(Node(start, None))
    file = open("puzzles.txt", "r")
    for line in file:
        print(line.strip())
        tic = time()
        print("PATH LENGTH: " + getLength(Node(line.strip(), None)))
        toc = time()
        print("EXECUTION TIME: %5.2f seconds" % (toc - tic))
        print()


if __name__ == "__main__":
    main()