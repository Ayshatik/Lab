guest_name = None
ans = input('Do U wanna invite anybody? (y/n) ')
counter = 0
while ans == 'y':
    guest_name = input('Enter name of your guest: ')
    print(f'{guest_name} has been invited')
    counter += 1
    ans = input('Do U wanna invite anybody else? (y/n) ')
print(counter)
