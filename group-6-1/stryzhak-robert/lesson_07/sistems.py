def as_binary(n):
    if n < 0:
        return '-' + as_binary(-n)
    if n < 1:
        return str(n%2)
    b = n // 2
    return str(as_binary(b)) + str(n%2)

print(as_binary(-255))