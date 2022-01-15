def linear_search(numbers, x):
    for i in range(len(numbers)):
        if numbers[i] == x:
            return i
    else:
        return -1

def test(res, aw_res):
    if res == aw_res:
        print('ok')
    else:
        print('not ok')

a = [1, 3, 4, 5, 7, 8, 10]
print('введите элемент для поиска в списке')
n = int(input())
print(linear_search(a, n))

test(linear_search(a,1), 0)
test(linear_search(a,2), -1)
test(linear_search(a,5), 3)
test(linear_search(a,15), -1)
