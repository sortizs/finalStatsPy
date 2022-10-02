
""" with open('users.txt', 'r') as file:
    content = file.read().split('\n')
    for contentLine in content:
        list.append(contentLine.split(';'))
        print(type(contentLine))

    print(type(content))
    print(list)
    for item in list:
        print(type(item))
    
    print(type(list)) """

from typing import List
import re

lines: List[str] = []
names: List[str] = []
with open('users.txt', 'r') as file:
    lines = file.read().split('\n')
    # print(lines)
    for line in lines:
        for line in line.split(';'):
            names.append(str(line).split(','))
    del names[1::2]
    for name in names:
        print(name)