print('1) Square ', '2) Triangle ', sep='\n')
num = int(input('Enter a number: '))
if num == 1:
    square_length = int(input('Enter the length of square: '))
    print(square_length**2)
elif num ==2:
    triangle_length = int(input('Enter the length of triangle: '))
    triangle_height = int(input('Enter the height of triangle: '))
    print(triangle_length * triangle_height /2)
else:
    print('ERROR!')