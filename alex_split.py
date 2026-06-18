####Леша и разбиение массива####

n = int(input())
a = list(map(int, input().split()))

total = sum(a)

if total != 0:
    print("YES")
    print(1)
    print(1, n)
    exit()

s = 0
for i in range(n):
    s += a[i]
    if s != 0:
        print("YES")
        print(2)
        print(1, i + 1)
        print(i + 2, n)
        exit()

print("NO")
