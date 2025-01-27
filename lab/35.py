name, n = input('Enter your name: '), int(input('Enter an integer: '))
for i in list(name):
    for j in range(n):
        if j == n - 1:
            print(i)
        else:
            print(i, end=' ')