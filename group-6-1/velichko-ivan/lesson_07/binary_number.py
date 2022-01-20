def bin_to_ten(n):
    if n == 0:
        return n
    last_digit = n % 2
    return str(bin_to_ten(n // 2)) + str(last_digit)


def test(result, expected):
    if result != expected:
        print(f'Ошибка: {result} != {expected}')
    else:
        print('!Nice!')


test(bin_to_ten(128), "010000000")
test(bin_to_ten(54), "0110110")