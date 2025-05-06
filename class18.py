# from class17 import Greetings

# Greetings()


myList_1 = [0,0,0,0,0,0,0]
myList_2 = [0,0,0,0,0,1,0,0,0,]
def makeSquare(x):
    result = []
    for num in x:
        result.append(num*num)
    return result

x = [2,3,4,5]
# Squared_list  = makeSquare(x)

def isAllZero(lst):
    check = True
    for num in lst:
        if num != 0:
            check = False
            break
    return check


if isAllZero([0,0,1,0]):
    print("It has All zeros")
else:
    print("Non Zero")
