def as_binary_string(n):
    
    if n == 0:
        return n
    last_digit = n % 2
    return str(as_binary_string(n//2)) + str(last_digit)

print(as_binary_string(4))