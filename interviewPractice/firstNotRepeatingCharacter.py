def firstNotRepeatingCharacter(s):
    b=set()
    a=set()
    for i in s:
        if i in b:
            a.add(i)
        else:
            b.add(i)
            print b
    for i in s:
        if (i in a)==False:
            return i
    return '_'