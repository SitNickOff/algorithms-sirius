def generation(count, result='', left=0, right=0):
    if left == count and right == count:
        print(result)
    else:
        if left < count:
            generation(count, result + '(', left+1, right)
        if right < left:
            generation(count, result + ')', left, right+1)
