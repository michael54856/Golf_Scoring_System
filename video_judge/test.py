
def mininL(myList):
    minVal = myList[0]
    for i in myList:
        if i < minVal:
            minVal = i
    return minVal

def maxinL(myList):
    maxVal = myList[0]
    for i in myList:
        if i > maxVal:
            maxVal = i
    return maxVal

myList = [12,26,-6,48,-4,2,-2,32,5]

print(maxinL(myList),mininL(myList))