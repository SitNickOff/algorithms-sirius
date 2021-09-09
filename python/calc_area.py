from math import pi

def circle_area(radius):
    if type(radius) not in [int, float]:
        raise TypeError("Radius must be non-negative real number only")
    if radius < 0:
        raise ValueError("Radius can't be negative")
    return pi*radius**2

print(circle_area(25))

# r_list = [2, 0, -3, 2 + 3j, True, [2], 'seven']
# message = 'Площадь окружности с радиусом {radius} --> {area}'

# for r in r_list:
#     s = circle_area(r)
#     print(message.format(radius=r, area=s))
