string = str(input())
while string[0] == ' ':
    string = string.lstrip(' ')
while string[-1] == ' ':
    string = string.rstrip(' ')

while string.find('  ') > 0:
    string = string.replace('  ', ' ')

print(string)