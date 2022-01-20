# Strings - строки

s1 = 'Python.'
s2 = "I'm a programmer"
s3 = 'I\'m a programmer' # экранируем спецсимвол
s4 = "C:\Windows\temp\network\new_file.txt"
s5 = r"C:\Windows\temp\network\new_file.txt"  # оператор r скажет интерпритатору игнорировать экранирование
s6 = '''I'm a big fan of movie "I'm a robot"!!!''' 
s7 = """I'm a big fan of movie "I'm a robot"!!!"""

# комментарий

'''
длинный комментарий
s1 = 'Python.'
s2 = "I'm a programmer"
s3 = 'I\'m a programmer' # экранируем спецсимвол
'''

print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print(s6)
print(s7)

print(s1 + ' ' + s2)   # конкантинация
print((s1 + ' ') * 10)

print(s2.split(' ')) # Список слов

a = 4.2
# print("В переменной хранится занчение: " + a)  - получим ошибку
print("В переменной хранится занчение: " + str(a))

s8 = '16+2j'
print(complex(s8))
print(type(complex(s8)))