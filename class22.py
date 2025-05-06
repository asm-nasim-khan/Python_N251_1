# file = open('sample.txt','a')
# for i in range(10):
#     file.write(f'''Eshikhon {i}\n''')

# file.close()


# file = open('sample.txt','w+')
# for i in range(10):
#     file.write(f'''Eshikhon {i}\n''')
# file.seek(0)
# data = file.read()
# print(data)
# # for i in range(10):
# #     file.write(f'''Eshikhon {i}\n''')

# file.close()



file = open('sample.txt','a+')
# file.seek(0)
# data = file.read()
# print(data)
for i in range(10):
    file.write(f'''\nEshikhon {i}''')
file.seek(0)
data = file.read()
print(data)

file.close()