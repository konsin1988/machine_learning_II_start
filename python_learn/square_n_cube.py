from math import sqrt, floor
n = 124213
l = [False for _ in range(n)]
i = 1
while i ** 2 <= n:
  l[i ** 2 - 1] = True
  i += 1
i = 1
while i ** 3 <= n:
  l[i ** 3 - 1] = True
  i += 1
print(sum(l))

print(floor(n**(1/2)) + floor(n ** (1.0/2.999999)) - round(n ** (1.0/6.0)))

