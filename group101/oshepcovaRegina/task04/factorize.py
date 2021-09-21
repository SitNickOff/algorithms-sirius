def factorizate(num):
    result = list()
    div = 2
    while div * div <= num:
        if num % div == 0:
            result.append(div)
            num //= div
        else:
            div += 1
    if num > 1:
        result.append(num)
    return result


print(factorizate(8))
