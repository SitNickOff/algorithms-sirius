def hash(string):
    dlin = len(string)
    string_new = string[0:dlin-1]
    if dlin == 1:
        return ord(string[0])*(dlin-1)
    return (hash(string_new)*(dlin-1) + 