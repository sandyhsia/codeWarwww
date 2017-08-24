## My solution
def countBits(n):
    # print(n)
    count = 0
    for i in range(32):
        count += (n%2)
        n = int(n/2)
    return count

## Best
def countBits(n):
    return bin(n).count("1")