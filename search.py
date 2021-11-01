def search(list,target):

    first = 0
    last = len(list) - 1 
    while first  <= last:
        midpoint = (first + last) // 2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else: 
            last = midpoint - 1
    return None





    
def verifico(index):
    if index is not None:
        print('target:', index)

    else:
        print('no se encontro el punto')


number= [1,2,3,4,5,6,7,8,9,10]

result = search(number, 12)
print(result)
verifico(result)


result = search(number, 6)
print(result)
verifico(result)
