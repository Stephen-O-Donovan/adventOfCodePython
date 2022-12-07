
priority = {}
for c in range(ord('a'),ord('z')+1):
    priority[chr(c)] = c-96
for c in range(ord('A'),ord('Z')+1):
    priority[chr(c)] = c-38


# priority_sum = 0
# with open("input.txt") as f:
#     for line in f:
#         print(line)
#         ln = len(line)
#         r1 = line[0:int(ln/2)]
#         r2 = line[int(ln/2):ln]
#         common = ''.join(set.intersection(set(r1), set(r2)))
#         priority_sum +=priority[common]

# print(priority_sum)

priority_sum = 0
with open("input.txt") as f:
    for num, line in enumerate(f, 1):
        if(num%3==1):
            r1=line
        elif(num%3==2):
            r2=line
        else:
            common = ''.join(set.intersection(set(r1), set(r2), set(line))).strip('\n')
            priority_sum +=priority[common]

print(priority_sum)