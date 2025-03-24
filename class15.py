# Write a Python program that has a string and counts the frequency of each character using a dictionary. The program should then print the dictionary, where the keys are characters and the values are their respective frequencies.  

# Output: {'b': 1, 'a': 3, 'n': 2}
myDict = {}
word = "cclass"

# for ith in word:
#     if ith in myDict.keys():
#         myDict[ith] =  myDict[ith] + 1
#     else:
#         myDict[ith] = 1

# print(myDict)

# Write a program that  checks whether an element exists in a tuple using loop.

tpl = (4,8,6,0,3)

# print(55 in tpl)

# found = False
# for num in tpl:
#     if num == 55:
#         found = True

# if found == True:
#     print("Element Found in the Tuple.")
# else:
#     print("Not Found.")



# tpl = (4,7,9,6)
# element = 7
# for i in tpl:
#   if i == element:
#     print(("tple in 7 is ") ,"="  "true")
#   else:
#     print("Not Found.")



# a=3
# tpl=(1,2,3,4)

# if a in tpl:
#     print("exist")
# else:
#     print("does not exist")



# lst = [1, 2, 3, 7, 8, 9]
# total_sum = 0
# for num in lst:
#     total_sum += num
# print("Sum:", total_sum)
    
    
# total_sum = 0
# for i in range(len(lst)):
#    total_sum = total_sum + lst[i]
# print (total_sum)



# lst = [2,4,4,5,6,7,"apple"]
# for i in range(len(lst)):
#     if isinstance(lst[i],int):
#         if i%2==0:
#             print(i,"even")
#         else:
#             print(i,"odd")
#     elif isinstance(lst[i],str):
#         print(i,"_string")


# for item in lst:
#     if type(item) == "str":
#         print("Found")


# lst = [20,4,4,5,6,7,-1]
# myMax = lst[0]
# myMin = lst[0]
# for num in lst:
#     if num > myMax:
#         myMax = num
#     if num < myMin:
#         myMin = num
# print(myMax,myMin)
myDict = {
    1: 0,
    2: 0, 
    3: 0, 
    4: 0, 
    5: 0, 
    6: 0, 
    7: 0, 
    8: 0, 
    9: 0
    }
lst = [[1,2,3],[4,5,6]]
isDone = False
for i in range(9):
    if isDone == True:
        print(f'''|| 1:{myDict[1]} || 2:{myDict[2]}  || 3:{myDict[3]}  ||''')
        print("=====================")
        print(f'''|| 4:{myDict[4]} || 5:{myDict[5]}  || 6:{myDict[6]}  ||''')
        print("=====================")
        print(f'''|| 7:{myDict[7]} || 8:{myDict[8]}  || 9:{myDict[9]}  ||''')
        print("=====================")
        print("We Got a winner.")
        break

    print(f'''|| 1:{myDict[1]} || 2:{myDict[2]}  || 3:{myDict[3]}  ||''')
    print("=====================")
    print(f'''|| 4:{myDict[4]} || 5:{myDict[5]}  || 6:{myDict[6]}  ||''')
    print("=====================")
    print(f'''|| 7:{myDict[7]} || 8:{myDict[8]}  || 9:{myDict[9]}  ||''')
    print("=====================")

    cell_no = int(input("Enter cell value: "))
    mark = input("Enter your sign: ")
    myDict[cell_no] = mark

    # print(f'''|| 1:{myDict[1]} || 2:{myDict[2]}  || 3:{myDict[3]}  ||''')
    # print("=====================")
    # print(f'''|| 4:{myDict[4]} || 5:{myDict[5]}  || 6:{myDict[6]}  ||''')
    # print("=====================")
    # print(f'''|| 7:{myDict[7]} || 8:{myDict[8]}  || 9:{myDict[9]}  ||''')
    # print("=====================")

    for items in lst:
        temp = myDict[items[0]]
        count = 0
        for cell in items:
            if myDict[cell] == temp and myDict[cell] != 0 :
                count = count + 1
        if count>2:
            isDone = True
            break



