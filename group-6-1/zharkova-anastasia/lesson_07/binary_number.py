def binary_string(n):
    if n < 0:
        return "-" + binary_string(-n)

    if n == 0 or n == 1:
        return str(n)

    last_digit = n % 2
    return binary_string(n // 2) + str(last_digit)

print(binary_string(251))