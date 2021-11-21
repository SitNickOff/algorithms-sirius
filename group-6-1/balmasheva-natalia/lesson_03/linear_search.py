def linear_search(numbers, x):
    for index in range(len(numbers)):   #так как это линейный поиск, будем перебирать все числа в списке
        if numbers[index] == x:
            return index       #если нашлось число возвращаем индекс найденного числа
    return -1                   #если ничего не нашлось, возвращаем -1

list_num= list(map(int, input("запишите числа, среди которых мы будем искать").split())) #задаем массив
num = int(input("Введите число индекс, которого вы ищите: ")) #число которое, мы будем искать
poznany = linear_search(list_num,num)
if poznany == -1:
    print("Всё работает, такого числа нет,", poznany)
elif poznany != -1:
    print("Всё работает, такое число есть. Число", num ,"под индексом", poznany)
else:
    print("НИЧЕГО не работает. ---ОШИБКА---")