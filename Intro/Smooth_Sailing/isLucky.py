def isLucky(n):
	nList=list(str(n))
	nL=[int(i) for i in nList]
	half=len(nList)//2
	Half1=sum(nL[:half])
	Half2=sum(nL[half:])
	return Half1==Half2

print(isLucky(1001))