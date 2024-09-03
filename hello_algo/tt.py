lis_1 = [3, 1, 2, 0]
i = 0
def a(lis_1, i):
    i += 1
    if lis_1[i] != 0:
        a(lis_1, i)
        print(lis_1[i])


a(lis_1, 0)