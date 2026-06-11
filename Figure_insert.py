####Вставь цифру####

t = int(input())

for j in range(t):
    n, d = map(int,input().split())

    ##print(n, d)
               
    f = input()
    d = str(d)
    ##print(f)
    
    f_result = []
    inserted = False

    for i in f:
        if not inserted and d > i:
            f_result.append(d)
            inserted = True
        f_result.append(i)

    if not inserted:
          f_result.append(d)


    print("".join(f_result))
