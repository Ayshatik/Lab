ans = input('In which direction should I keep the report?'
            'Choose FORWARD or REVERSE: (f/r) ')
if ans == 'f':
    num = int(input('Enter a number: '))
    for i in range(1, num + 1):
        print(i)
elif ans == 'r':
    num = int(input('Enter a number smaller than 20: '))
    for i in reversed(range(num, 21)):
        print(i)
else:
    print('I don’t understand')


