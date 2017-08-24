## My solution
def filter_list(l):
  new_list = []
  for item in l:
      if type(item) != str:
          new_list.append(item)
  return new_list
          

## Best
def filter_list(l):
  'return a new list with the strings filtered out'
  return [i for i in l if not isinstance(i, str)]