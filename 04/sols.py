
count=0
overlap=0
with open("input.txt") as f:
    for n, line in enumerate(f):
        l = line.strip().strip('\n').strip('').split(',')
        l1 = l[0].split('-')
        l2 = l[1].split('-')
        a = int(l1[0])
        b = int(l1[1])
        c = int(l2[0])
        d = int(l2[1])
        if( a <= c and b >= d ) or ( a >= c and b <= d ):
            count+=1
        if((c >= a and d <=b) or (d >= a and c <= b)):
            overlap+=1
print(count)
print(overlap)