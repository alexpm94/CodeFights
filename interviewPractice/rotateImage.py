def rotateImage(a):
    b=[]
    for i in range(len(a)):
        b.append([]) ##[None]*len(a) crea lista pero dependiente
        
    for i in range(len(a)):
        for j in range(len(a)):
            b[j].append(a[abs(i-len(a)+1)][j])
    return b  

def rotateImage(a):
    return zip(*a[::-1])