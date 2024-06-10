# using dict
password = input("Enter new password :")
result = {}

if len(password) >= 9:
    result['length'] = True
else:
    result['length'] = False

digit = False

for i in password:
    if i.isdigit():
        digit = True

result['digit'] = digit

uppercase = False

for i in password:
    if i.isupper():
        uppercase = True

result['upper-cate'] = uppercase
print(result)
if all(result.values()):
    print("password is strong ")
else:
    print("password is weak ")

