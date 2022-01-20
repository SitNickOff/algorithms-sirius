def build_matryoshka(size, n):
    if n >= 1:
        print(f"Создаём низ матрёшки размера {size}.")
        build_matryoshka(size - 1, n - 1)
        print(f"Создаём верх матрешки размера {size}.")
    else:
        return


build_matryoshka(7, 7)