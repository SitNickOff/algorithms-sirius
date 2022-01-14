# Гуляя по одному из островов Алгосского архипелага, Гоша набрёл на пещеру, в которой лежат кучи золотого песка. К счастью, у Гоши есть с собой рюкзак грузоподъёмностью до M килограмм, поэтому он может унести с собой какое-то ограниченное количество золота.

# Всего золотых куч n штук, и все они разные. В куче под номером i содержится mi килограммов золотого песка, а стоимость одного килограмма — ci алгосских франков.

# Помогите Гоше наполнить рюкзак так, чтобы общая стоимость золотого песка в пересчёте на алгосские франки была максимальной.

# Формат ввода
# В первой строке задано целое число M — грузоподъёмность рюкзака Гоши (0 ≤ M ≤ 108).

# Во второй строке дано количество куч с золотым песком — целое число n (1 ≤ n ≤ 105).

# В каждой из следующих n строк описаны кучи: i-ая куча задаётся двумя целыми числами ci и mi, записанными через пробел (1 ≤ ci ≤ 107, 1 ≤ mi ≤ 108).

# Формат вывода
# Выведите единственное число —– максимальную сумму (в алгосских франках), которую Гоша сможет вынести из пещеры в своём рюкзаке.         

def solution(m, arr):
    arr.sort(reverse=True)
    print(arr)
    weight = 0
    amount = 0
    for i in arr:
        if m - weight >= i[1] :
            amount += i[0] * i[1]
            weight += i[1]
        else:
            return amount + i[0] * (m - weight)            
    
    return amount

def test(result, expected):
    if expected != result:
        print(f"Error: {expected} != {result}")
    else:
        print(f"OK! {result}")
        
test(solution(10, [[8, 1], [2, 10], [4, 5]]), 36)
test(solution(10000, [[4, 20]]), 80)