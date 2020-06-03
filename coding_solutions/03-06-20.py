def clear_rightmost_set_bit(n):
    return n & (n - 1)
n = int(input('Enter a number: '))
ans = clear_rightmost_set_bit(n)
print('n with its rightmost set bit cleared equals:', ans)    
