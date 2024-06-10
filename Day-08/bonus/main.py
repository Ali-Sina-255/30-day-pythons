date = input("Enter today's date :")
mood = input("How do you rate your mode today from 1 to tan ? :")
thoughts = input("let your thoughts flow: \n")

with open(f'../journal/{date}.txt', 'w') as file:
    file.write(mood, 2 * '\n')
    file.write(thoughts)
