import re

commandList = []
stackDict = {}
for i in range(1,10):
    stackDict['S'+str(i)] = []
    
with open("input.txt") as f:
    for n, line in enumerate(f):
        if(n<8):
            for(i, v) in enumerate(line):
                if(i<=33 and v.isalpha()):
                    stackDict['S'+str(i//4 + 1)].insert(0, v)
        if(n>9):
            commandList.append(re.findall('\d+', line))


for c in commandList:
    for i in range(int(c[0])):
        e = stackDict['S'+str(c[1])].pop()
        stackDict['S'+str(c[2])].append(e)
print(stackDict)


# for c in commandList:
#     l1 = stackDict['S'+str(c[1])][:-int(c[0])]
#     l2 = stackDict['S'+str(c[1])][-int(c[0]):]
#     stackDict['S'+str(c[1])] = l1
#     for d in l2:
#         stackDict['S'+str(c[2])].append(d)
# print(stackDict)

final = ''
for p in stackDict.values():
    final+=p.pop()
print(final)
