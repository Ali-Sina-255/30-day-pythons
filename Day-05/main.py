while True:
    user_action = input("Type show, add,edit, complete, exit :")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input('Enter a todos :') + "\n"
            file = open('todos.txt', 'r')

            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('todos.txt', 'w')
            file.writelines(todos)
        case 'show':
            for index, item in enumerate(todos):
                item = item.title()
                print(f'{index + 1} - {item}')
        case 'edit':
            number = int(input("Number of the todo to edit ?: "))
            new_todo = input("Enter new tods .")
            todos[number - 1] = new_todo
            print(todos)
        case 'complete':
            number = int(input("Enter the number you want to delete :"))
            todos.pop(number - 1)
        case 'exit':
            break
        case _:
            print("Hey, Your entered an unknown command")

print("Bye!!")
