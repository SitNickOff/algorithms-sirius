# Tuples - Кортежи

e1 = tuple()
e2 = ()
print(e1)
print(e2)

t0 = ()
t1 = (1,)
t2 = (2, 3)
t3 = (4, 5, 6)
print(t0)
print(t1)
print(t2)
print(t3)

p1 = 1,
p2 = 1, 2
p3 = 1, 2, 3
print(p1)
print(p2)
print(p3)

x, y, z = 44, 66, 88
print(x)
print(y)
print(z)

x, y, z = t3
print(x)
print(y)
print(z)

var1 = 14
var2 = 3

var1, var2 = var2, var1  # меняем значения переменных между собой
print(var1)
print(var2)

# Операции над кортежами
# Кортежи неизменяемые тип коллекций

t4 = (t1 + t2 + t3) * 3  # Кортежи можно складывать и мультиплицировать
print(t4)

print(t4[0])
print(t4[2])
print(t4[4])
print(t4[::-1])  # В кортежах можно использовать срезы
print(t4[0:5])
print(t4[-4:-2])

print(len(t4))  # Количество элементов в кортеже
print(t4.count(3))  # Количество повторений опреденного элемента в кортеже
print(t4.index(3))  # Индекс первого значения в кортеже

del t4  # Уничтожаем кортеж

moves = {
    (1, 0): 'up',
    (0, 1): 'Right',
    (-1, 0): 'Down',
    (0, -1): 'Left'
}

print(moves[(1, 0)])
