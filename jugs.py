def nod(i, n):
    while i != 0:
        n, i = i, n % i
    return n


def f(m:int, b:int, mMx, bMx, nd):
    print(m, b)

    if b == 0:
        b = bMx
    elif m == mMx:
        m = 0
    elif b > mMx:
        b = b - (mMx - m)
        m = mMx
    else:
        m = b
        b = 0
    if b == nd:
        print(f"{m} {b}\nВ большем кувшине налито {b} галлонов воды")
        return

    return f(m, b, mMx, bMx, nd)


m, b, mMx, bMx, nd = map(int, input('Введите данные: ').split())
if (nd % nod(mMx, bMx)) == 0:
    f(m, b, mMx, bMx, nd)
else:
    print("Задача не имеет решений")
