## My solution
def get_sum(a,b):
    #good luck!
    if a == b:
        return a
    elif a <= b:
        small = a
        large = b
    else:
        small = b
        large = a
    i = 0
    sum = 0
    while((small+i)<large):
        sum += (small+i)
        i += 1
    sum += large
    return sum

## Best...
def get_sum(a,b):
    return sum(xrange(min(a,b), max(a,b)+1))

def get_sum(a, b):
    return (a + b) * (abs(a - b) + 1) // 2

## corner case:
get_sum(1,1) = 1