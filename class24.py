# Regular expressions (RegEx)
import re

text = "Khulna Metro GHA 12 - 1234"
pattern = "[A-Z][a-z]+ [A-Z][a-z]+ [A-Z]+ [0-9]+ [-] [0-9]+"
sp = re.findall(pattern,text)
print(sp)
# text = "Hello I am from bangladesh"

# pattern = '\+8801\d{9}'
# pattern = '[a-z]+[.]*[_]*[0-9|a-z]*@[a-z]+.[a-z]+' #email
# pattern = '\w+'
# sp = re.findall(pattern,text)
# print(sp)
# sp = text.split("1")
# print(sp)

data = "Khulna Metro GHA 12-1234"
# pattern1='[A-Z][a-z]+ [A-Z][a-z]+ [A-Z]+ \d{2}[-]\d{4}'
# pattern2 = "[A-Z][A-Z | a-z]+ [A-Z][A-Z | a-z]+ [0-9][0-9][-][0-9][0-9][0-9][0-9]"
# sp = re.findall(pattern2,data)
# print(sp)
