
class FileTree:
    def __init__(self) -> None:
        self.name = '/'
        self.levelNum = 1
        self.nodes = [Node(self.levelNum, self.name, self.name)]

    def addNode(self, nodeName, parentName):
        self.nodes.append(Node(self.levelNum, nodeName, parentName))
        self.getNode(parentName).addChildDir(nodeName)

    def listAllNodes(self):
        return self.nodes

    def getNode(self, nodeName):
        for n in self.listAllNodes():
            if n.getNodeName() == nodeName:
                return n
        return None


class Node:
    def __init__(self, level, name, parent) -> None:
        self.name = name
        self.parent = parent
        self.files = {}
        self.childDir = {}
        self.level = level

    def addFile(self, fileName, size):
        self.files[fileName] = size

    def addChildDir(self, dirName):
        self.childDir[dirName] = self.level

    def setParent(self, parentName):
        self.parent[parentName] = self.level

    def getNodeName(self):
        return self.name

    def getNodeParent(self):
        return self.parent

    def getNodeChildDir(self):
        return self.childDir

    def getNodeFiles(self):
        return self.files

    def getNodeLevel(self):
        return self.level



class Cursor:
    def __init__(self, tree) -> None:
        self.parentDir = '/'
        self.currentDir = '/'
        self.tree = tree

    def returnToRoot(self):
        self.parentDir = '/'
        self.currentDir = '/'
        self.tree.levelNum = 1

    def ascentTree(self):
        parent = self.tree.getNode(self.currentDir).getNodeParent()
        self.tree.levelNum -=1 if self.tree.levelNum > 1 else 1
        self.currentDir = parent
        if self.tree.levelNum > 1:
            self.parentDir = self.tree.getNode(self.currentDir).getNodeParent()  
        else: 
            self.parentDir = '/'

    def descentTree(self, childDir):
        parent = self.tree.getNode(self.currentDir).getNodeName()
        self.parentDir = parent
        self.currentDir = childDir
        self.tree.levelNum += 1

    def createDir(self, dirName):
        self.tree.addNode(dirName, self.currentDir)

    def createFile(self, fileName, fileSize):
        self.tree.getNode(self.currentDir).addFile(fileName, int(fileSize))

    def getCurrentLevel(self):
        return self.tree.levelNum

    def getLevelDirs(self, level):
        dirs = [d for d in self.tree.nodes if  d.getNodeLevel() == level]
        return dirs

    def getAllNodes(self):
        return self.tree.listAllNodes()

    def getAllFilesInCurrentDir(self):
        return self.tree.getNode(self.currentDir).getNodeFiles()
    
    def calculateDirSize(self):
        return sum(self.tree.getNode(self.currentDir).getNodeFiles().values())

    def traverseNode(self, size, level):
        nodeList = self.getLevelDirs(level)
        for n in nodeList:
            if n.getNodeChildDir() == {}:
                size += sum(n.getNodeFiles().values())
            else:
                return  self.traverseNode(size, level+1)
        return size


f1 = FileTree()
c = Cursor(f1)

with open("input.txt") as f:
    for line in f:
        # print(line)
        if(line[0] == '$'):
            cmdLst = line.strip('\n').split(' ')
            if(cmdLst[1]=='cd'):
                if(cmdLst[2]=='/'):
                    c.returnToRoot()
                elif(cmdLst[2]=='..'):
                    c.ascentTree()
                else:
                    c.descentTree(cmdLst[2])
            else:
                continue
        else:
            createLst = line.strip('\n').split(' ')
            if(createLst[0]=='dir'):
                c.createDir(createLst[1])
            else:
                c.createFile(createLst[1], createLst[0])

c.returnToRoot()


print(c.tree.levelNum)
print(c.traverseNode(0, c.tree.levelNum))
for d in c.getLevelDirs(c.tree.levelNum):
    print(d.getNodeName())
c.descentTree('jpfrhmw')
print(c.tree.levelNum)
print(c.traverseNode(0, c.tree.levelNum))
