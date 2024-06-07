user_prompt ='Enter a To do :'
todo_1 = input(user_prompt)
todo_2 = input(user_prompt)
todo_3 = input(user_prompt)

todo_list = [todo_1, todo_2, todo_3]
print(todo_list)

# text = input("Enter the Title :")
#
# print('Your title length is ',len(text))


def title_length(text):
    result = len(text)
    return result


text = input("Enter Your Text :")
length = title_length(text)
print(length)