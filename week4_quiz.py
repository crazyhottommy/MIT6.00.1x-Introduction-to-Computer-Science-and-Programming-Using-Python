
def primesList(N):
    '''
    N: an integer
    Returns a list of prime numbers smaller than N +1
    '''
    def is_prime(a):
        if a < 2:
            return False
        return all(a % i for i in xrange(2, a))

    prime_list=[]
    for num in range(2,N +1):
        if is_prime(num):
            prime_list.append(num)
    return prime_list

# Write a recursive Python function, given a non-negative integer N,
# to count and return the number of occurrences of the digit 7 in N.
# For example:
#  count7(717) -> 2
#  count7(1237123) -> 1
#  count7(8989) -> 0

# do not use loop!

def count7(N):
    if N < 10:
        if N %10 == 7:
            return 1
        else:
            return 0
    elif N % 10 == 7:
        return 1 + count7(N/10)
    else:
        return 0 + count7(N/10)


##Write a Python function that returns a list of keys in aDict that map to integer
# # values that are unique (i.e. values appear exactly once in aDict).
# # The list of keys you return should be sorted in increasing order.
# (If aDict does not contain any unique values, you should return an empty list.)

def uniqueValues(aDict):
    return [key for key in aDict.keys() if aDict.values().count(aDict[key]) == 1].sort()


def satisfiesF(L):
  """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements
    Returns the length of L after mutation
    """
    for s in L[:]:
        if not f(s):
            L.remove(s)
    return len(L)

def f(s):
    return 'a' in s

L =['a', 'b', 'a']

print satisfiesF(L)
print L
