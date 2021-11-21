def two_sum_primary(numbers, sum):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == sum:
                return[i, j]
    return []

def two_sum_optimized(numbers, sum):
    some_nums=dict()
    for i in range(len(numbers)):
        num = sum - numbers[i]
        if numbers[i] in some_nums:
            return [some_nums[numbers[i]], i]
        else:
            some_nums[num] = i