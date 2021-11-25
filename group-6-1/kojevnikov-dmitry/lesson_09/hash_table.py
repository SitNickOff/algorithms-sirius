arr = [None] * 3
arr[0] = 25
arr[1] = 'qwerty'
arr[3] = 36

print(arr)

assoc = {}
assoc['123'] = 25
assoc[123] = 'qwerty'

print(assoc)

students = [
    {
      'name': 'Joghn',
        'last_name': 'Ivanov',
        'age': 73
    },
    {
        'name': 'Bill',
        'last_name': 'Petrov',
        'age': 13,
        'adress': {
            'city': "LA",
            'street': 'Kablukova',
            'home': 23
        }
    }
]

print(students)