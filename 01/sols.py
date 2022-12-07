data = {}
elf = 1
data[elf] = 0
with open("input.txt") as f:
    for line in f:
        if line == "\n":
            elf+=1
            data[elf] = 0
        else: 
            data[elf]+=int(line.strip('').strip('\n'))
max_elf = max(data, key=data.get)
print(max_elf)
print(data[max_elf])

sorted_elves_by_cals = sorted(data.items(), key=lambda x:x[1], reverse=True)
print(sorted_elves_by_cals[0][1]+sorted_elves_by_cals[1][1]+sorted_elves_by_cals[2][1])