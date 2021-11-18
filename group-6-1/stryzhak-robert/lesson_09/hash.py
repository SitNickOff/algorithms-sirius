class Map():
    def __init__(self):
        self.pairs = []
        
    def set(self, key, value):
        self.pairs.append([key, value])
    
    def get(self, key):
        for item in self.pairs:
            if item[0] == key:
                return item[1]
        return -1

    
def test():
    cities1 = Map()
    cities1.set('city1', 'Moscow')    
    cities1.set('city2', 'Tula')    
    cities1.set('city3', 'LA')
    

    print(cities1.pairs)
    assert cities1.get('city1') == 'Moscow'
    assert cities1.get('city3') == 'LA'
    
    print(cities1.get('city1'))    
    print(cities1.get('city2'))

    
test()