# import re

# email_pattern = r'[a-z]+[.]*[_]*[0-9|a-z]*@[a-z]+.[a-z]+'
# text = "Here are some emails: test@example.com, hello@world.org, invalid-email@, another@valid.co, user@domain.com"

# # print(re.findall(email_pattern, text))
# email = lambda x: re.findall(email_pattern, x)


# emails = email(text)
# print(emails)


from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment
myfile = load_workbook("MYFILE.xlsx")
sheet = myfile.active
sheet['A5'] = "Hello World"
sheet['B5'] = 52
sheet['B5'].alignment = Alignment(horizontal='center', vertical='center')
sheet['C5'] = "Gulshan"

sheet['A6'] = "Abdul"
sheet['B6'] = 55
sheet['B6'].alignment = Alignment(horizontal='center', vertical='center')
sheet['C6'] = "Malibagh"
myfile.save("MYFILE.xlsx")
myfile.close()