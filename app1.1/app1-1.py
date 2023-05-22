todos = []
def get_todos():
    with open('todos_o.txt', 'r') as file:
        todos_local = file.readlines()
    return todos_local
def write_todos(todos_arg):
    with open('todos_o.txt', 'w') as file:
        file.writelines(todos_arg)
while True:
    action = input("type add, edit, show, remove or exit: ")
    if action == 'add':
        todo = input("enter a todo: ")
        todos = get_todos()
        todos.append(todo + '\n')
        write_todos(todos)
    elif action == 'edit':
        number = int(input("input number: "))
        number = number - 1
        todos = get_todos()
        new_todo = input("Enter a new todo: ")
        todos[number] = new_todo
        write_todos(todos)
    elif action == 'show':
        todos = get_todos()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif action == 'remove':
        todos = get_todos()
        delete = int(input("Enter the number of todo to remove: "))
        delete = delete - 1
        del todos[delete]
        write_todos(todos)
    elif action == 'exit':
        break
    else:
        print("Invalid code")
print("bye")
