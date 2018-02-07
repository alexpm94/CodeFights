def firstDuplicate(a):
    b= set()#Set no guarda duplicados
    for i in a:
        if i in b:
            return i
        else:
            b.add(i)
    return -1