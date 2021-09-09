# Int - integer - целые

cats = 4  # используем оператор присваивания
dogs = 2
delta_population = -200
k = int(16) # Создание с помощью конструктора


# Float - вещественные или дествительные (когда нужны дробные значения)

volume = 1.5
area = 42.8
salary = 2532.99
p = float(22)


# Complex - комплексные
a = 4 + 6j
b = 8 - 2.3j
c = complex(4, -2)

i_f = float(dogs)
f_i = int(area)  # отбрасывается вещественная часть
f_c = complex(salary)

print(i_f, f_i, f_c)

# комплексное перевести в Int или Float не получится
# c_f = float(b)
# print(c_f)


########################################
# Операции с числами
#########################################

s1 = a + b
s2 = volume - area
s3 = p * dogs # -> Float
s4 = salary / cats
s5 = volume ** 2

# Операции не применимы к комплексным числам
s6 = 19 // 2  # 9 - целочисленное деление
s6 = 19 % 2  # 1 - остаток на деление

s8 = 2 + 3 * 5  # 17

# int + float => float
# float + complex => complex

eq1 = 42.0 - 22 
eq2 = 42.2 - 22  # Ошибка округления в ядре Python
print('eq1 =', eq1)
print('eq2 =', eq2)
