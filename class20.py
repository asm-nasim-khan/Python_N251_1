import math as m

# print(math.sqrt(21**2))
# print(math.isqrt(21))

# print(25**0.5)
# print(math.pow(3,2))
# print(math.factorial(-1))

# print(m.ceil(4.01))
# print(m.floor(4.6))

# from datetime import datetime,date
# print(datetime.now().astimezone().tzinfo)
# print(datetime.now().month) 
# print(datetime.now().day)

# print(datetime.now().strftime("%I:%M:%S"))
# print(datetime.now().strftime("%B"))
# print(datetime.now().strftime("%b"))

# print(datetime.now().strftime("%A"))
# print(datetime.now().strftime("%a"))

# import class17 as mymodule
# mymodule.Greetings()

# import random
# print(random.randint(1,10))

file = open('sample.txt','r').readlines()
# file = open('sample.txt','r').read()
# file = open('sample.txt','r')
# print(file.readline())
# print(file.readline())
print(file)
for line in file:
    print(line)




