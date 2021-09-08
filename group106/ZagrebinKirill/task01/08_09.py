def amount(_list):  # Реализовал функцию суммирования тк не совсем понял задание :D
    result = 0
    for i in _list:
        result += i
    return result


a = [1, 10, 20, 41, 22, 13]

print(amount(a))
print(sum(a))  # просто ленивый вариант через встроеную функцию :)))))
