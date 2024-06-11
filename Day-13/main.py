def get_todo(filepath):
    with open(filepath, 'r') as local_file:
        local_todos = local_file.readlines()
    return local_todos


def write_tods(filepath, todo_arg):
    with open(filepath, 'w') as local_file:
        local_file.writelines(todo_arg)


while True:
    user_action = input("Type show, add,edit, complete, exit :")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]
        todos = get_todo("todos.txt")

        todos.append(todo + '\n')

        write_tods('todos.txt', todos)

    elif user_action.startswith('show'):
        todos = get_todo("todos.txt")
        for index, item in enumerate(todos):
            item = item.strip('\n')
            item = item.title()
            print(f'{index + 1}-{item}')

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            todos = get_todo("todos.txt")
            new_todo = input("Enter new tods. ")
            print("here is todo existing", todos)

            todos[number - 1] = new_todo + '\n'

            print('Here is how it will be', todos)
        except ValueError:
            print("Your command is not Valid. ")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = get_todo("todos.txt")
            index = number - 1
            todo_to_remove = todos[index].strip('\n')

            todos.pop(index)

            write_tods('todos.txt', todos)

            message = f"To do {todo_to_remove} is was remove form the list !"
            print(message)

        except IndexError:

            print("There is no Number with that index .")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Hey, This command is not Valid")

print("Bye!!")
