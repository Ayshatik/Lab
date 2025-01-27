first_num = input('Введите первое число: ')
second_num = input('Введите второе число: ')
if int(first_num) > int(second_num):
    print(second_num, first_num, sep=', ')
else:
    print(first_num, second_num, sep=', ')
