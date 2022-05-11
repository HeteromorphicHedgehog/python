'''
myfile = open('fruits.txt')
content = myfile.read()
myfile.close()
'''

with open('files\\fruits.txt', 'r') as myfile:
    content = myfile.read()

print(content)