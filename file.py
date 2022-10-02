from typing import List

def getNames() -> List[str]:
    names = []
    with open('users.txt', 'r') as file:
        lines = file.read().split('\n')
        for line in lines:
            for line in line.split(';'):
                names.append(line)
    return names