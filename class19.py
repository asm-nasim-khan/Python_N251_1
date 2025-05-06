# def Greetings(n):
#     if n>=5:
#         return
#     print(n)
#     Greetings(n+1)
    

# Greetings(0)

# print("The end")


# n = "o"
# n = n+"1"
# print(n)

try:
    age = int(input("Enter you age: "))
    print(100/age)
except ValueError:
    print("Always Enter number for age")
except ZeroDivisionError:
    print("Can not divide by Zero")
    age = 1
    print(100/age)
except Exception as e:
    print("Found",e)

print("Good morning")