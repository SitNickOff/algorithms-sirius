print(ord('a'))
print(ord('A'))

string = 'rita'

hash = (ord('R') * 3**(4-1) + ord('I') * 3**(4-2) + ord('T') * 3 ** (4-3) + ord('A') * 3 ** (4-4)) % 7

print(f"h({string}): {hash}")

def test_hash(str, q, r):
    j = 1
    hash = 0
    for i in str:
        hash += ord(i) * q **(len(str)-j)
        j +=1
    return hash % r
hh = test_hash('RITA',3 , 7)
print(f'h({string}): {hh}')