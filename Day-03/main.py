todos = []
while True:
    user_action = input("Type show, add, exit :")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input('Enter a todos :')
            todos.append(todo)
        case 'show':
            for item in todos:
                item = item.title()
                print(item)
        case 'exit':
            break
        case _:
            print("Hey, Your entered an unknown command")

print("Bye!!")
