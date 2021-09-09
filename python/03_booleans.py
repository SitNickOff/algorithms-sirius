# Boolean - логические тип данных

a  = True
b = False

print(a, b)

b1 = bool(True)
b2 = bool(1)
b3 = bool(0)
b4 = bool(2.7)
b5 = bool(-297)
print(b1, b2, b3, b4, b5)

c1 = int(b1)
c2 = int(b3)
print(c1, c2)

d1 = b1 + b2 + b3 + b4 + b5
d2 = b1 * 10
print(d1, d2)

e1 = bool('True')
e2 = bool('False')
print(e1, e2)
e3 = bool('')
print(e1, e2, e3)

f1 = str(True)
f2 = str(False)
print(f1, f2)