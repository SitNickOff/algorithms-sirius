# Циклы

employees = [
    {'name': 'Jhon', 'salary': 25000},
    {'name': 'Peter', 'salary': 25000},
    {'name': 'Ben', 'salary': 25000},
    {'name': 'Bob', 'salary': 25000},
    {'name': 'Kevin', 'salary': 25000},
    {'name': 'Mike', 'salary': 25000}
]


'''
while condition_is_true:
    pass

for iterator in some_range:
    pass
'''

index = 0
while index < len(employees):
    if employees[index]['name'] == 'Mike':
        employees[index]['salary'] = 35000
    index += 1

print(employees)

'''
r - range[START <included> : STOP <not included> : STEP <default value: 1>]
'''

for index in range(len(employees)):
    if employees[index]['name'] == 'Mike':
        employees[index]['salary'] = 45000

print(employees)


for worker in employees:
    if worker['name'] == 'Mike':
        worker['salary'] = 55000

print(employees)

employees = [
    {'name': 'Jhon', 'salary': 25000},
    {'name': 'Peter', 'salary': 25000},
    {'name': 'Ben', 'salary': 25000},
    {'name': 'Bob', 'salary': 25000},
    {'name': 'Kevin', 'salary': 25000},
    # {'name': 'Mike', 'salary': 25000},
    {'name': 'Jhon', 'salary': 25000},
    {'name': 'Peter', 'salary': 25000},
    {'name': 'Ben', 'salary': 25000},
    {'name': 'Bob', 'salary': 25000},
    {'name': 'Kevin', 'salary': 25000},
    # {'name': 'Mike', 'salary': 25000}
]

for worker in employees:
    if (worker['name'] == 'Mike' and worker['salary'] >= 55000):
        continue  # ниже ничего выполняться не будет
    
    if worker['name'] == 'Mike':  # Повышаем заработную плату первому Mike
        worker['salary'] = 55000
        break  # Выходим из цикла
    
else:  # Если не нашли ни одного Mike
    print('There is no Mike')

print(employees)