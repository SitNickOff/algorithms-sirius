# def is_prime(num):
#     pass

# def test(result, awaitin_result):
#     if result == awaitin_result:
#         print('ok')
#     else:
#         print('Ошибка', result, '!=', awaitin_result)


# test(is_prime(5), True)
# test(is_prime(4), False)

def F(n):
    print(n)
    if n < 5:
        F(n + 1)
        F(n + 3)


F(2)
