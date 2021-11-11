def gen_binary(n,ref=''):
    if n == 0:
        print(ref)
    else:
        gen_binary(n - 1, ref + '1')
        gen_binary(n - 1, ref + '0')

gen_binary(3)