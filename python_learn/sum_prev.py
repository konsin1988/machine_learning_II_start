count = 0
prev_val_odd = 0
prev_val_even = 0

def cmp_prev(val):
    global prev_val_odd
    global prev_val_even
    global count
    answer = val > (prev_val_odd + prev_val_even)
    count += 1
    if count % 2:
        prev_val_odd = val
    else:
        prev_val_even = val
    
    return answer

print(cmp_prev(2))
print(cmp_prev(3))
print(cmp_prev(1))
print(cmp_prev(10))
print(cmp_prev(7))
print(cmp_prev(20))
