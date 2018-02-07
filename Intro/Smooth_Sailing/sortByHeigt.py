'''Some people are standing in a row in a park. 
There are trees between them which cannot be moved. 
Your task is to rearrange the people by their heights 
in a non-descending order without moving the trees.

Example

For a = [-1, 150, 190, 170, -1, -1, 160, 180] 
the output should be:
sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].'''


def sortByHeight(a):
	x=sorted(a)
	indexTree=[]
	for i in range(len(a)):
		if a[i]==-1:
			indexTree.append(i)
	for i in range(len(x)):
		if x[i]!=-1:
			x=x[i:]
			break
	if -1 in x:
		x=[]
	for i in indexTree:
		x.insert(i,-1)
	return x



a = [-1,-1,-1]
print(sortByHeight(a))