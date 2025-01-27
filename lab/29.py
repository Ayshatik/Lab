import math

cylinder_radius = int(input('Введите радиус цилиндра: '))
cylinder_height = int(input('Введите высоту цилиндра: '))
cylinder_square = math.pi * cylinder_radius**2 * cylinder_height
print(f'{cylinder_square:.3f}')