
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
"""
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
        

with open('users.txt', 'r') as f:
    lines = f.read().split('\n')
    user = lines[1].split(';')
    print(user[0])
    print(user[1])

import json

with open('userData.json', 'r') as f:
    data = json.load(f)
    print(type(data))
    print(json.dumps(data['amaya'], sort_keys=True, indent= 4))
    f.close()"""

for x in range(2, 0, -1):
    print(x)
else:
    print('no left attempts')