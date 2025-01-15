n = 200
l = [True for _ in range(n + 1)]
l_num = [i for i in range(n+1)]
for num in l_num:
    if num == 0 or num == 1:
        l[num] = False
    else: 
        if l[num]:
            for i in range(num * 2, n +1, num):
                l[i] = False

print([n for n in l_num if l[n]] )