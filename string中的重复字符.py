## My solution
def is_isogram(string):
    #your code here
    if type(string) != str:
        raise TypeError('Argument should be a string')

    elif string == "":
      return True
    else:
        string = string.lower()
        repeat = 0
        for char in string:
            if string.count(char) > 1:
                repeat += 1
        if repeat > 0:
            return False
        else:
            return True

#Best Practice
def isogram(n):
    if not isinstance(n, str):
        return False
    elif len(n) < 1:
        return True
    n = n.lower()
    if len(n) == len(set(n)): ## we check if the length of the input is equal to the length of the set(n). 
        return True
    else:
        return False

# The function set() converts a collection or a sequence or an iterator object into a set. 
# For example: set('lists') returns {'s', 't', 'l', 'i'}, as you can see the letter 's' which appears twice in 'lists', does not appear in the set. 
# This is useful to check if the length of the set is equal to the length of the input, if there is a letter which appears twice in the input the condition is False.
