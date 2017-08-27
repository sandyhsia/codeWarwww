## My
def compare(a, b):
    if a == None and b == None:
        return True
    elif (a == None and b != None) or (a != None and b == None):
        return False
    else:
        if a.val != b.val:
            return False
        else:
            return (compare(a.left, b.left) and compare(a.right, b.right))

## Best
def compare(a, b):
    return a.val == b.val and compare(a.left, b.left) and compare(a.right, b.right) if a and b else a == b