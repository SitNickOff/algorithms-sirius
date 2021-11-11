def gen_binary(n,ref=''):
    if n == 0:
        print(ref)
    else:
        gen_binary(n - 1, ref + 'a')
        gen_binary(n - 1, ref + 'b')

gen_binary(3)