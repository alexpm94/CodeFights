"""Ticket numbers usually consist of an even number of digits. 
A ticket number is considered lucky if the sum of the first 
half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.

Example

    For n = 1230, the output should be
    isLucky(n) = true;
    For n = 239017, the output should be
    isLucky(n) = false"""

def isLucky(n):
	nList=list(str(n))
	nL=[int(i) for i in nList]
	half=len(nList)//2
	return sum(nL[:half])==sum(nL[half:])

print(isLucky(1001))