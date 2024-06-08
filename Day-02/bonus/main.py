password = input('Enter your password :')
user_password = 'alisina123'
times = 1
while times <= 2:
    if password != user_password:
        print('Password is incorrect')
    else:
        print("password is correct")

    times += 1