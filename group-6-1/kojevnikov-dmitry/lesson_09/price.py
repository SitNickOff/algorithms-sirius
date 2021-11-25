# class Node():
#     def __init__(self, value=None, next=None):
#         self.value = value
#         self.next = next
    

# class HashTable():
#     def __init__(self, size=33):
#         self.values = [None] * size
#         self.size = size
           
#     def bucket(self, key):
#         return hash(key) % self.size
    
#     def put(self, key, value):
#         index = self.bucket(key)
#         if self.values[index] == None:
#             node_value = [key, value]
#         else:
#             while
#         self.values[index] = Node(node_value)
        

#     def get(self, key):
#         index = self.bucket(key)
        
#         return self.values[index].value[1]
    
    

# def hash(str, q = 5, r = 33):
#     # j = 1
#     # hash = 0
#     # for i in str:
#     #     hash += ord(i) * q **(len(str)-j)
#     #     j +=1
#     # return hash % r
#     return ord(str[0])


# def test():
#     price = HashTable()
#     price.put('bananas', 75)
#     print(price.values)
#     print(price.get('bananas'))
#     price.put('orange', 80)
#     price.put('obricos', 95)
#     print(price.get('orange'))
#     print(price.get('obricos'))
    
# test()    
