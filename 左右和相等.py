# My solution
def find_even_index(arr):
    #your code here
    length = len(arr)
    if length == 0:
        return 0
    for i in range(length):
        if i == 0:
            if sum(arr[1:length]) == 0:
                return 0
        else:
            # print sum(arr[0:i]), sum(arr[i+1:length])
            if sum(arr[0:i]) == sum(arr[i+1:length]):
                return i
    return -1

    ################ sum(arr[0:i]) means add from [0,i)!!!!

## Best
def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1

def find_even_index(lst):
    left_sum = 0
    right_sum = sum(lst)
    for i, a in enumerate(lst):
        right_sum -= a
        if left_sum == right_sum:
            return i
        left_sum += a
    return -1