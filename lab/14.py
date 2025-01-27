rain = input('Is it rain? ')
if rain.lower() == 'yes':
    windy = input('Is it windy? ')
    if windy.lower() == 'yes':
        print('It\'s too windy for an umbrella')
    else:
        print('Take an umbrella')
else:
    print('Enjoy your day')

