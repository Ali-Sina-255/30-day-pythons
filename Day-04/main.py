todos = []
while True:
    user_action = input("Type show, add,edit exit :")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input('Enter a todos :')
            todos.append(todo)
        case 'show':
            for item in todos:
                item = item.title()
                print(item)
        case 'edit':
            number = int(input("Number of the todo to edit ?: "))
            new_todo = input("Enter new tods .")
            todos[number - 1] = new_todo
            print(todos)

        case 'exit':
            break
        case _ :
            print("Hey, Your entered an unknown command")

print("Bye!!")
