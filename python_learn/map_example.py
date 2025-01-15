def name_changer(name):
    return 'Mr.' + name

names = ['Danya', 'Slava', 'Bob']
changed_names = list(map(name_changer, names))
print(changed_names)

numbers = '3 87 23 45 93 23'
prod = 1
for n in map(int, numbers.split()):
    prod *= n

print(prod)

numbers = list(map(int, numbers.split()))
sum_sqrt = 0
for n in map(lambda x: x ** 2, numbers):
    print(n)
    sum_sqrt += n

print(sum_sqrt)