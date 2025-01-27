num = int(input('Enter a integer in range from 10 to 20: '))
while num < 10 or num > 20:
    if num < 10:
        print('Too low')
        num = int(input('Enter a integer in range from 10 to 20: '))
    elif num > 20:
        print('Too high')
        num = int(input('Enter a integer in range from 10 to 20: '))
else:
    print('Thank U')


