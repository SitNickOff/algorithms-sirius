# Sets - сеты

s1 = set()  # Единственный способ определения Сета
s2 = {}
print(type(s1))
print(type(s2))

s1 = set(['False', 2.73, 4, (12, 22), True])
# Значения отражаются в другом порядке, потому как это неупорядоченный тип
print(s1)
print(len(s1))

s1.add(25)
s1.add(4)  # Ничего не изменилось так как сети уже имеет в наборе 4
print(s1)
print(len(s1))  # Мы добавили два числа а количество увеличилось на одноо

s2 = set([2, 4, 5, 7, 8, 9])
print(s1.union(s2))
print(s2.union(s1))

user_subs = [2, 3, 4, 5, 8, 10, 11, 12, 13, 14, 16, 18, 19, 20]
user_likes = [1, 3, 6, 7, 8, 9, 12, 15, 16, 17, 20, 21, 22]
set_user_subs = set(user_subs)
set_uesr_like = set(user_likes)

# Пересечение пользователей
vip_users = set_user_subs.intersection(set_uesr_like)
# Пользователи, которые есть в одном списке, но нет в другом
note_users = set_user_subs.symmetric_difference(set_uesr_like)

print(vip_users, 'vip_users')
print(note_users, 'note_users')

print(s1)
s1.remove(25)  # удалит только если есть в сете, иначе ошибка
s1.discard(255)  # удалит если есть в сете, иначе ничего не произойдет
s1.pop()  # не понятно зачем нужно
print(s1)

s1.clear()  # очещает все элементы, но сам сет сохраняется как объект
print(s1)
del s1  # безвозвратного удалеят и значения и сам сет
