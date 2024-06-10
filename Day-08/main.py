while True:
    user_action = input("Type show, add,edit, complete, exit :")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input('Enter a todos :') + "\n"
            with open("todos.txt", 'r') as file:
                todos = file.readlines()
            todos.append(todo)
            with open("todos.txt", 'w') as file:
                file.writelines(todos)

        case 'show':
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            # for removing the extra space
            new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(new_todos):
                item = item.strip('\n')
                item = item.title()
                print(f'{index + 1}-{item}')

        case 'edit':
            number = int(input("Number of the todo to edit ?: "))

            with open("todos.txt", 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter new tods .")
            print("here is todo existing", todos)

            todos[number - 1] = new_todo + '\n'

            print('Here is how it will be', todos)

        case 'complete':
            number = int(input("Number of the todo to completed :"))

            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')

            todos.pop(index)

            with open("todos.txt", 'w') as file:
                file.writelines(todos)

            message = f"To do {todo_to_remove} is was remove form the list !"
            print(message)

        case 'exit':
            break
        case _:
            print("Hey, Your entered an unknown command")

print("Bye!!")
