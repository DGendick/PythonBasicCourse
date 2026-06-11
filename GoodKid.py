##Хороший ребенок##

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0

    for i in range(n):
        b = a[:]      # копия массива
        b[i] += 1     # увеличиваем один элемент на 1

        prod = 1
        for x in b:
            prod *= x

        ans = max(ans, prod)

    print(ans)
