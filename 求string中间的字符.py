## My solution
def get_middle(s):
    #your code here
    length = len(s)
    if length%2 == 1:
        return s[(length+1)/2 - 1]
    else:
        return s[length/2 - 1]+s[length/2]

## Best
def get_middle(s):
   return s[(len(s)-1)/2:len(s)/2+1]

def get_middle(s):
    i = (len(s) - 1) // 2
    return s[i:-i] or s