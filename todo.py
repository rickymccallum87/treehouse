def show_help():
    print('(H)elp, (L)ist, (S)ave, (Q)uit')

def show_list(todo_list):
    for item in todo_list:
        print(item, end='')

def add_item(todo_list, item):
    todo_list.append(item + '\n')

def load_file():
    with open('todo.txt') as todo_file:
        todo_list = list(todo_file)
    return todo_list

def save_file(todo_list):
    with open('todo.txt', 'w') as todo_file:
        for item in todo_list:
            todo_file.write(item)
    return

def main():
    todo_list = load_file()
    show_list(todo_list)
    show_help()
    while True:
        item = input('> ')
        if item == 'h':
            show_help()
        elif item == 'l':
            show_list(todo_list)
        elif item == 's':
            save_file(todo_list)
        elif item == 'q':
            show_list(todo_list)
            break
        else:
            add_item(todo_list, item)

main()
