# This time, write a procedure, called biggest, which returns the key corresponding to the entry with the largest 
# number of values associated with it. If there is more than one such entry, return any one of the matching keys.

# animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

#animals['d'] = ['donkey']
#animals['d'].append('dog')
#animals['d'].append('dingo')

# biggest(animals)
# 'd'

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    if aDict=={}:
        return None
    else:
        return max(aDict, key=lambda x:len(aDict[x]))
        

# or

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    result = None
    biggestValue = 0
    for key in aDict.keys():
        if len(aDict[key]) >= biggestValue:
            result = key
            biggestValue = len(aDict[key])
    return result
