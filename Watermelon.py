####Арбуз####

w = int(input())
if w <= 1:
    w = 1
elif w >= 100:
    w = 100

if w / 2 % 2 == 0:
    ans = bool(True)
else:
    i = 0
    w2 = 0
    for i in range(w):
        w = w - 1
        w2 = w2 + 1
        if (w % 2 == 0 and w2 % 2 == 0) and (w != 0 and w2 != 0):
            ans = bool(True)
            break
        else:
            ans = bool(False)



if ans == True:
    print('YES')
else:
    print('NO')
    
