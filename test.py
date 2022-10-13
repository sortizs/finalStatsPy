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
    f.close()

for x in range(2, 0, -1):
    print(x)
else:
    print('no left attempts')
    

username = 'carlosgomez'
with open(f'mensajes/{username}.txt', 'r') as f:
    content = f.read().split('\n')
    print(content)
    f.close()

from datetime import datetime

date = datetime.now()

print(datetime.now().strftime('%d/%m/%y %H:%M:%S'))"""
"""
import json

nombre = input('Nombre: ')
apellido = input('Apellido: ')
edad = int(input('Edad: '))
profile = {'nombre': nombre, 'apellido': apellido, 'edad': edad}

print(json.dumps(profile, indent=4))

with open('./data/userData.json', 'r+') as f:
    data = json.load(f)
    data['sebas'] = profile
    print(data)
    f.seek(0)
    json.dump(data, f, indent=4)
    f.truncate()
    f.close()"""

import re

gustos = re.sub(r'^\s+|\s+$', '', input('Gustos: ').split(','))
# likes = []
# for gusto in gustos:
#    likes.append()
print(gustos)