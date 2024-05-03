
#Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n  scores. Store them in a list and find the score of the runner-up.

#Input Format

#The first line contains n . The second line contains an array A[]  of n integers each separated by a space._


if _name_ == '_main_':
    n = int(input())
    arr = map(int, input().split())
    lst=list(arr)
    scores=list()
    for score in lst:
        if score not in scores:
            scores.append(score)
        else:
                continue
    ordr=sorted(scores,reverse=True)
    print(ordr[1])     
           
#Input (stdin)
#5
#2 3 6 6 5
#Your Output (stdout)
#5
