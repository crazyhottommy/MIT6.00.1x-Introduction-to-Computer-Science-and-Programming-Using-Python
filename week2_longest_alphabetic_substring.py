# Assume s is a string of lower case characters.

# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
# For example, if s = 'azcbobobegghakl', then your program should print Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print 
# Longest substring in alphabetical order is: abc
# For problems such as these, do not include raw_input statements or define the variable s in any way. 
# Our automated testing will provide a value of s for you - so the code you submit in the following box 
# should assume s is already defined. If you are confused by this instruction, please review L4 Problems 10 and 11 
# before you begin this problem set.

alpha = 'abcdefghijklmnopqrstuvwxyz'

## track the length of the longest alphabetic order substring 
## starting from each letter in s
ind = []
for i in range(len(s)):
    length = 1
    while True:
        if i == len(s) - 1:
            break
        elif alpha.find(s[i]) <= alpha.find(s[i+1]):
            length += 1
            i += 1
        else:
            break
    ind.append(length)

t=[]
## t is an empty list, it will contain all the substrings in alphabetic order
for start, length in enumerate(ind):
    t.append(s[start:start + length])

print max(t, key = len)
