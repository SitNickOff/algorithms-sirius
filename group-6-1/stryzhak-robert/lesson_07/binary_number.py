def binary_convert(n):
    if n == 0:
        return n
    last_digit = n % 2
    return str(binary_convert(n // 2)) + str(last_digit)


def test(result, expected):
    if result != expected:
        print(f'Ошибка: {result} != {expected}')
    else:
        print('Norm!')


test(binary_convert(128), "010000000")
test(binary_convert(54), "0110110")