while True:
    user_action = input("Type show, add,edit, complete, exit :")
    user_action = user_action.strip()

    if 'add' in user_action:
        todo = user_action[4:]
        with open("files/todos.txt", 'r') as file:
            todos = file.readlines()

        todos.append(todo + '\n')

        with open("files/todos.txt", 'w') as file:
            file.writelines(todos)

    elif 'show' in user_action:

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            item = item.title()
            print(f'{index + 1}-{item}')

    elif 'edit' in user_action:
        number = int(user_action[5:])

        with open("files/todos.txt", 'r') as file:
            todos = file.readlines()

        new_todo = input("Enter new tods .")
        print("here is todo existing", todos)

        todos[number - 1] = new_todo + '\n'

        print('Here is how it will be', todos)

    elif 'complete' in user_action:
        number = int(user_action[9:])

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()
        index = number - 1
        todo_to_remove = todos[index].strip('\n')

        todos.pop(index)

        with open("files/todos.txt", 'w') as file:
            file.writelines(todos)

        message = f"To do {todo_to_remove} is was remove form the list !"
        print(message)

    elif 'exit' in user_action:
        break
    else:
        print("Hey, This command is not Valid")

print("Bye!!")

