def prime(number):
    if number == 1:
       return False

    acc = 0
    for i in range(2, number):
        if (number % i) == 0:
            acc += 1
    if acc == 0:
            return True
    return False

def test(number, result):
    if prime(number) != result:
        print('A mistake! We expect: "', result, '" - Return "', prime(number))
    else:
            print('All acording to plan!')

test(7, True)
test(4, True)
test(13, True)