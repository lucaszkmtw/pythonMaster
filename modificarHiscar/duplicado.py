from archivo import fileOpen

def findDuplicate(lineas):
    l1 = []
    l2 = []
    for i in lineas:
        if i not in l1:
            l1.append(i)
        else:
            l2.append(i)
            print(i)
    
    return l2


lista = fileOpen()
print(lista)
print(findDuplicate(lista))