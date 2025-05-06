# JSON modules 
import json

mydict = {
    "name": "John", 
    "age": 30,
    'city': "New York",
    "is_student": False,
    "courses": ["Math", "Science"],
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "state": "NY"
    }
}

# json_string = json.dumps(mydict)
# # print(type(mydict))
# print(json_string)

# new_dict = json.loads(json_string)
# print(new_dict)
# print(type(new_dict))


#ternary operator
# a = 100
# b = 100
# max_value =  a if a > b and a!=b else b

# if a>b and a!=b:
#     if a > b:
#         max_value = a
#     else:
#         max_value = b
#     max_value = a
# else:
#     max_value = b
    
# print(max_value)

#iterators
# lst = [1,2,3,4,5,6,7,8,9,10]
# myiter = iter(lst)
# # print(next(myiter))
# print(next(myiter))
# print(next(myiter))

#generators
# def counter(n):
#     i = 0
#     while i <= n:
#         yield i
#         i += 1

# mygen = counter(10)

# for num in mygen:
#     print(num,end="  ")


from openpyxl import Workbook, load_workbook
myfile = load_workbook("MYFILE.xlsx")
sheet = myfile.active
print(sheet.title)
print(sheet['A1'].value,sheet['B1'].value, sheet['C1'].value)
print(sheet['A2'].value,sheet['B2'].value, sheet['C2'].value)
print(sheet['A3'].value,sheet['B3'].value, sheet['C3'].value)
print(sheet['A4'].value,sheet['B4'].value, sheet['C4'].value)   
