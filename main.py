def boos(m, number):
    if int(number) % 6 == 0:
        return 0

    other = [i for i, ben in enumerate(number) if int(ben) % 2 == 0]
    if not other:
        return -1

    summ = sum(int(d) for d in number)
    if summ % 3 != 0:
        return -1

    minmov = float('inf')
    for i in other:
        if i == m - 1:
            continue
        mov = abs(i - (m - 1))
        if i == 0 and number[1] == '0':
            continue
        minmov = min(minmov, mov)

    return minmov if minmov != float('inf') else -1


a = int(input('Введите первое число: '))
b = input('Введите второе число: ')

print(boos(a, b))
