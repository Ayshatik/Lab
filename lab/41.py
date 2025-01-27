guests_quantity = int(input('How many people do U wanna invite'
                            ' to your party? '))
if guests_quantity < 10:
    for i in range(guests_quantity):
        guest_name = input('What\'s name? ')
        print(guest_name, 'has been invited')
else:
    print('Too many people')