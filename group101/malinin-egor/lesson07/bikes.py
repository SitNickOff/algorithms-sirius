def bike(days,array,price, answer = [-1,-1]):
    price_2 =  2*price
    lenth = days - len(array)
    if lenth == 0:
        answer = [-1,-1]
    if days-len(array) == len(array) :
        return answer
    else:
        if array[lenth] - price_2 >= 0 and answer[1] == -1:
            answer[1] = lenth + 1  
            if -1 in answer:
                return bike(days + 1, array, price, answer)
            else:
                return answer
        elif array[lenth] - price >= 0 and answer[0] == -1:
            answer[0] = lenth + 1  
            if -1 in answer:
                return bike(days + 1, array, price, answer)
            else:
                return answer    
        else:
            return bike(days + 1, array, price, answer)



def test(result, expected):
    if result != expected:
        print(f'Ошибка: {result} != {expected}')
    else:
        print('Ok!')
