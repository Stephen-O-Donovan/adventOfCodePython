

with open("input.txt") as f:
    for line in f:
        sequence = line

def findStart(code: str)-> int:
    currentSq = []
    for (i,v) in enumerate(code):
        if(i<3):
            continue
        for j in range(-3,1):
            e = code[(j+i)]
            if(e not in currentSq):
                currentSq.append(e)
        if(len(currentSq)==4):
            return i+1
        else:
            currentSq = []


# assert findStart('bvwbjplbgvbhsrlpgdmjqwftvncz') == 5
# assert findStart('nppdvjthqldpwncqszvftbrmjlhg') == 6
# assert findStart('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 10
# assert findStart('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 11
# print(findStart(sequence))

def findMsg(code: str)-> int:
    # n=14
    # return [i for i in range(n, len(code)) if len(set(code[i-n:i])) == n][0]
    currentSq = []
    for (i,v) in enumerate(code):
        if(i<13):
            continue
        for j in range(-13,1):
            e = code[(j+i)]
            if(e in currentSq):
                currentSq = []
                break
            else:
                currentSq.append(e)
        if(currentSq!=[]):
            return i+1
            

assert findMsg('mjqjpqmgbljsphdztnvjfqwrcgsmlb') == 19
assert findMsg('bvwbjplbgvbhsrlpgdmjqwftvncz') == 23
assert findMsg('nppdvjthqldpwncqszvftbrmjlhg') == 23
assert findMsg('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 29
assert findMsg('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 26
print(findMsg(sequence))