def sudoku2(grid):
    a=[]
    b=[]
    c=[]
    
    def firstDuplicate(a):
        b= set()#Set no guarda duplicados
        for i in a:
            if i in b:
                return False
            else:
                b.add(i)
        return True

    for i in range(len(grid)):
        c.append([]) ##[None]*len(a) crea lista pero dependiente
    
    for i in range(len(grid)):
      for j in range(len(grid)):
            d=grid[i / 3 * 3 + j / 3][i % 3 * 3 + j % 3]
            if d!='.':
                c[i].append(d)
            if grid[i][j]!='.':
                a.append([grid[i][j],j])
                b.append([grid[i][j],i])
    for x in a:
            if a.count(x)>1:
                return False
    for x in b:
            if b.count(x)>1:
                return False
    for x in c:
        for y in x:
            if x.count(y)>1:
                return False
    return True


def sudoku2(board):
    big = set()
    for i in xrange(0,9):
        for j in xrange(0,9):
            if board[i][j]!='.':
                cur = board[i][j]
                if (i,cur) in big or (cur,j) in big or (i/3,j/3,cur) in big:
                    return False
                big.add((i,cur))
                big.add((cur,j))
                big.add((i/3,j/3,cur))
    return True