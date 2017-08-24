## My solution
def find_outlier(integers):
    odd_list = []
    even_list = []
    for item in integers:
        if item % 2 == 0:
            even_list.append(item)
        else:
            odd_list.append(item)
    if len(odd_list) > len(even_list):
        return even_list[0]
    else:
        return odd_list[0]

## Best
def find_outlier(integers):
    parity = [n % 2 for n in integers]
    return integers[parity.index(1)] if sum(parity) == 1 else integers[parity.index(0)]

def find_outlier(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]

######### Don't understand.....
def find_outlier(integers):
    assert len(integers) >= 3

    bit = integers[0] & 1

    if integers[1] & 1 != bit:
        return integers[integers[2] & 1 == bit]

    for n in integers:
        if n & 1 != bit:
            return n

    assert False