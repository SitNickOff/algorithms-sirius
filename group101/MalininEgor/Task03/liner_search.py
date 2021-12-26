def linear_search(numbers, x): 
    return -1 
 
n = int(input()) 
num = [] 
for i in range(n): 
    num.append(int(input())) 
 
x = int (input()) 
 
result = linear_search(num, x) 
 
print(result)