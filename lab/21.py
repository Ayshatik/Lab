poem = input('Write the first string of poem: ')
print(len(poem))
# преобразуем строку в список
poem_list = poem.split()
# выводим начальную и конечную позицию
print(poem_list[0], poem_list[-1])

#print(poem_list[1:-1])
