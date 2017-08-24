## My solution:
def square_sum(numbers):
    #your code here
    sum = 0
    for i in numbers:
        sum += i**2
    return sum


## Best
def square_sum(numbers):
    return sum(x ** 2 for x in numbers)