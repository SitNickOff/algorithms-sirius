# Генератор скобок
# Все языки	Oracle Java 8	OpenJDK Java 11
# Ограничение времени	1 секунда	1.5 секунд	1.5 секунд
# Ограничение памяти	64Mb	64Mb	64Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# Рита по поручению Тимофея наводит порядок в правильных скобочных последовательностях (ПСП), состоящих только из круглых скобок (). Для этого ей надо сгенерировать все ПСП длины 2n в алфавитном порядке —– алфавит состоит из ( и ) и открывающая скобка идёт раньше закрывающей.

# Помогите Рите —– напишите программу, которая по заданному n выведет все ПСП в нужном порядке.

# Рассмотрим второй пример. Надо вывести ПСП из четырёх символов. Таких всего две:

# (())
# ()()
# (()) идёт раньше ()(), так как первый символ у них одинаковый, а на второй позиции у первой ПСП стоит (, который идёт раньше ).
# Формат ввода
# На вход функция принимает n — целое число от 0 до 10.

# Формат вывода
# Функция должна напечатать все возможные скобочные последовательности заданной длины в алфавитном (лексикографическом) порядке.

# 3
# ((()))
# (()())
# (())()
# ()(())
# ()()()

# 2
# (())
# ()()


def gen(n):
    slovo_from_skobka = []

    def biba(S=[], left=0, right=0):
        if len(S) == 2 * n:
            slovo_from_skobka.append("".join(S))
            return

        if left < n:
            S.append("(")
            biba(S, left + 1, right)
            S.pop()

        if right < left:
            S.append(")")
            biba(S, left, right + 1)
            S.pop()


    biba()
    return slovo_from_skobka

def test(result, expected):
    if result != expected:
        print(f'Oh shit Here we go again: {result} != {expected}')
    else:
        print('DAAAAMN U R a GOD')


test(gen(2), ["(())", "()()"])
test(gen(3), ["((()))", "(()())", "(())()", "()(())", "()()()"]) 