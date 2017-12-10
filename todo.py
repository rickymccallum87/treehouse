todo_list = []

def show_help():
    print('(H)elp, (L)ist, (Q)uit')

def show_list():
    print(todo_list)

def add_item(item):
    todo_list.append(item)

def main():
    show_help()
    while True:
        item = input('> ')
        if item == 'h':
            show_help()
        elif item == 'l':
            show_list()
        elif item == 'q':
            break
        else:
            add_item(item)

main()
show_list()
