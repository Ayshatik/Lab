first_num = int(input('Enter the 1st number: '))
second_num = int(input('Enter the 2nd number: '))
summ = first_num + second_num
print(summ)
ans = input('Do U wanna add another number? (y/n) ')
while ans =='y':
    num = int(input('Enter a number: '))
    summ += num
    print(summ)
    ans = input('Do U wanna add another number? (y/n) ')
else:
    print(summ)

