class Map():
    def __init__(self):
        self.pairs = []

    def get(self, key):
        #  Your code
        #  “ヽ(´▽｀)ノ”
        pass

    def set(self, key, value):
        #  Your code
        #  “ヽ(´▽｀)ノ”
        pass

def test():
    map = Map()
    map.set('city1', 'Moscow')
    map.set('city2', 'Tula')
    map.set('city3', 'Sochi')

    assert map.get('city3') == 'Sochi'
    assert map.get('city1') == 'Moscow'

test()