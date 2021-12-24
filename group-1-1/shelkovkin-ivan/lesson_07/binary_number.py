def binary_number(n):
    if n < 0:
        return "-" + binary_number(-n)

    if n == 0 or n == 1:
        return str(n)

    last_digit = n % 2
    return binary_number(n // 2) + str(last_digit)

print(binary_number(251))