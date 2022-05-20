from vector import Vector2
from constants import *

class MazeBase(object):
    def __init__(self):
        self.name = ""
        self.portalPairs = {}
        self.homeoffset = []
        self.homenodeconnectLeft = []
        self.homenodeconnectRight = []
        self.pacmanStart = []
        self.fruitStart = []
        self.ghostNodeDeny = {UP:None, DOWN:None, LEFT:None, RIGHT:None}

    def setup(self, nodegroup, pacman, ghostgroup):
        self.setPortals(nodegroup)
        self.denyAccess(nodegroup, pacman, ghostgroup)

    def denyAccess(self, nodegroup, pacman, ghostgroup):
        nodegroup.denyHomeAccess(pacman)
        nodegroup.denyHomeAccessList(ghostgroup)
        x, y = self.addoffset(2, 3)
        nodegroup.denyAccessList(x, y, LEFT, ghostgroup)
        nodegroup.denyAccessList(x, y, RIGHT, ghostgroup)

        for direction in list(self.ghostNodeDeny.keys()):
            if self.ghostNodeDeny[direction] is not None:
                for x, y in self.ghostNodeDeny[direction]:
                    nodegroup.denyAccessList(x, y, direction, ghostgroup)


    def getPacmanStartNode(self, nodegroup):
        pacstartkey = nodegroup.constructKey(*self.pacmanStart)
        return nodegroup.nodesLUT[pacstartkey]

    def getBlinkyStartNode(self, nodegroup):
        return self.getGhostStart(nodegroup, 2, 0)

    def getPinkyStartNode(self, nodegroup):
        return self.getGhostStart(nodegroup, 2, 3)

    def getInkyStartNode(self, nodegroup):
        return self.getGhostStart(nodegroup, 0, 3)

    def getClydeStartNode(self, nodegroup):
        return self.getGhostStart(nodegroup, 4, 3)

    def getGhostStart(self, nodegroup, x, y):
        key = nodegroup.constructKey(*self.addoffset(x, y))
        return nodegroup.nodesLUT[key]

    def getSpawnNode(self, nodegroup):
        spawnkey = nodegroup.constructKey(*self.addoffset(2, 3))
        return nodegroup.nodesLUT[spawnkey]

    def getFruitNode(self, nodegroup):
        key = nodegroup.constructKey(*self.fruitStart)
        return nodegroup.nodesLUT[key]

    def setPortals(self, nodegroup):
        for key in list(self.portalPairs.keys()):
            p1, p2 = self.portalPairs[key]
            nodegroup.setPortalPair(p1, p2)

    def connectHomeNodes(self, nodegroup):
        homekey = nodegroup.createHomeNodes(*self.homeoffset)
        nodegroup.connectHomeNodes(homekey, self.homenodeconnectLeft, LEFT)
        nodegroup.connectHomeNodes(homekey, self.homenodeconnectRight, RIGHT)

    def addoffset(self, x, y):
        return x+self.homeoffset[0], y+self.homeoffset[1]

class Maze1(MazeBase):
    def __init__(self):
        MazeBase.__init__(self)
        self.name = "maze1"
        self.portalPairs = {0:((0, 17), (27, 17))}
        self.homeoffset = (11.5, 14)
        self.homenodeconnectLeft = (12, 14)
        self.homenodeconnectRight = (15, 14)
        self.pacmanStart = (15, 26)
        self.fruitStart = (9, 20)
        self.ghostNodeDeny = {UP:((12, 14), (15, 14), (12, 26), (15, 26))}

class Maze2(MazeBase):
    def __init__(self):
        MazeBase.__init__(self)
        self.name = "maze2"
        self.portalPairs = {0:((0, 4), (27, 4)), 1:((0, 26), (27, 26))}
        self.homeoffset = (11.5, 14)
        self.homenodeconnectLeft = (9, 14)
        self.homenodeconnectRight = (18, 14)
        self.pacmanStart = (16, 26)
        self.fruitStart = (11, 20)
        self.ghostNodeDeny = {UP:((9, 14), (18, 14), (11, 23), (16, 23))}

class MazeController(object):
    def __init__(self):
        self.mazedict = {0:Maze1, 1:Maze2}

    def loadMaze(self, level):
        return self.mazedict[level%len(self.mazedict)]()