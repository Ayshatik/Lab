name, count = input('What is your name: '), int(input('Enter a number: '))
if count < 10:
    for i in range(count):
        print(name)
else:
    for i in range(3):
        print('Too high')
