
#A=X=rock=1
#B=Y=Paper=2
#C=Z=Scissors
# score = 0
# with open("input.txt") as f:
#     for line in f:
#         round = line.split()
#         match round[1]:
#             case 'X':
#                 score+=1
#                 if(round[0]) == 'A':
#                     score+=3
#                 elif(round[0] == 'C'):
#                     score+=6
#             case 'Y':
#                 score+=2
#                 if(round[0]) == 'B':
#                     score+=3
#                 elif(round[0] == 'A'):
#                     score+=6
#             case 'Z':
#                 score+=3
#                 if(round[0]) == 'B':
#                     score+=6
#                 elif(round[0] == 'C'):
#                     score+=3
# print(score)

#A=rock=1
#B=Paper=2
#C=Scissors=3
#X=Lose
#Y=Draw
#Z=Win
score = 0
with open("input.txt") as f:
    for line in f:
        round = line.split()
        match round[1]:
            case 'X':
                if(round[0]) == 'A':
                    score+=3
                elif(round[0] == 'B'):
                    score+=1
                else:
                    score+=2
            case 'Y':
                if(round[0]) == 'A':
                    score+=4
                elif(round[0] == 'B'):
                    score+=5
                else:
                    score+=6
            case 'Z':
                if(round[0]) == 'A':
                    score+=8
                elif(round[0] == 'B'):
                    score+=9
                else:
                    score+=7
print(score)