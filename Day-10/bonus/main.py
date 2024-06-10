# using pyton list
password = input("Enter new password :")
result = []

if len(password) >= 9:
    result.append(True)
else:
    result.append(False)

digit = False

for i in password:
    if i.isdigit():
        digit = True

result.append(digit)

uppercase = False

for i in password:
    if i.isupper():
        uppercase = True

result.append(uppercase)
if all(result):
    print("password is strong ")
else:
    print("password is weak ")
print(result)


def new_function(name, age):
    pass
