"""
Created on Tue Feb  6 22:30:20 2018

@author: alexpm94
Given two strings, find the number of common 
characters between them.

Example

For s1 = "aabcc" and s2 = "adcaa", the output should be
commonCharacterCount(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".
"""

s1 = "cb"
s2 = "aab"

def commonCharacterCount(s1, s2):
    ss1=sorted(s1)
    ss2=sorted(s2)
    c=0
    for char in ss1:
        print (char,s2)
        if len(ss2)==0:
            break
        if char>ss2[0]:
            try:
                if char==ss2[1]:
                    c+=1
            except IndexError:
                pass
            ss2=ss2[1:]           
        elif char==ss2[0]:
            c+=1
            ss2=ss2[1:]
    return c

def common2(ss1,ss2):
    s1=sorted(ss1)
    s2=sorted(ss2)
    count = 0
    while len(s1)>0 and len(s2)>0:
        if s1[0] == s2[0]:
            count += 1
            s1 = s1[1:]
            s2 = s2[1:]
        elif s1[0] < s2[0]:
            s1 = s1[1:]
        else:
            s2 = s2[1:]
    return count

#print(common2(s1,s2))       
print(commonCharacterCount(s1, s2))