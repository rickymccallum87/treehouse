todo_list = []

while True:
    item = input('> ')
    if item == 'd':
        break
    else:
        todo_list.append(item)

print(todo_list)
