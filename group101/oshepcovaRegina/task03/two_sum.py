def two_sum(array, num):
    for i in array:
        if (num - i) in array:
            return [i, num - i]
    return None

print(two_sum([1,2,3,5,7,9], 9))