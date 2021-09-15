# Операторы сравнения

a = 7
b = 3

c1 = a == b
c2 = a != b
c3 = a > b
c4 = a < b
print(c1, c2, c3, c4)

'''
if true_expression:
    # do something
else:
    # do something else
'''

if c3: 
    print('a больше чем b')
else: 
    print('a НЕ больше чем b')
print('конец программы')

a = int(input('Введите a: '))
b = int(input('Введите b: '))

if a > b:
    print('a больше чем b')
elif a < b:
    print('a меньше чем b')
else:
    print('значения равны')

if (a > b) or (a == b):
    print('a не меньше чем b')
if (a < b) or (a == b):
    print('a не больше чем b')

if (a > b) and (b > 0):
    print('a больше чем b и положительное')
if (a < b) or (a > 0):
    print('b больше чем а и положительное')


