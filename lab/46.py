compnum = 50
num = int(input('Enter a number: '))
i = 0
while num != compnum:
    i += 1
    if num < compnum:
        print(f'{num} is smaller than compnum')
    elif num > compnum:
        print(f'{num} is bigger than compnum')
    num = int(input('Enter a number: '))


if num == compnum:
    print(f'Well done, you took {i + 1} attempts')
