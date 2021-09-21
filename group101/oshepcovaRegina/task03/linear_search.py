def linear_search(array, number):
    for i in range(0, len(array)-1):
        if array[i] == number:
            return i

print(linear_search([1,2,3,6,7,8,9,0,10], 3))