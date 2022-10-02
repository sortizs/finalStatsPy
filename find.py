list = []
with open('users.txt', 'r') as file:
    content = file.read().split('\n')
    for contentLine in content:
        list.append(contentLine.split(';'))
        print(type(contentLine))

    print(type(content))
    print(list)
    for item in list:
        print(type(item))
    
    print(type(list))
    