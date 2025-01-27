name = input('What is your name? ')
if len(name) < 5:
    last_name = input('What is your last name? ')
    print(name.upper() + last_name.upper())
else:
    print(name.lower())