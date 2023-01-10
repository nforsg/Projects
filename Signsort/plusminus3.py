def signsort(array):
    '''The algorithm traverses simultaneaously from each side, switching places of the elements if 
    the order (signs) are "wrong".
    Time complexity is linear'''
    i = 0
    j = len(array)-1
    while i<j:

        '''Loop-invariant: array[0],..., array[i] < 0
            array[j], ..., array[len(array)-1] >= 0'''
        
        if array[i] >= 0 and array[j] < 0:
            array[i] , array[j] = array[j], array[i]
            j = j-1
            i = i+1
        elif array[i]>=0 and array[j] >= 0:
            j = j - 1
        elif array[i] <0 and array[j] < 0:
            i = i+1
        else:
            i = i+1
            j= j-1
    return array


'''Testing the emepty list'''
a = []
assert signsort(a) == []

'''Testing some lists containing ints. The for-loops states the conditions that must be satisfied 
for the hard-coded test-cases.'''

b = [-1, 2,-3, -5, 5, -5]
for i in range(0,3):
    assert signsort(b)[i] < 0
    assert not signsort(b)[i] >= 0
for i in range(4, len(b)):
    assert signsort(b)[i] >= 0
    assert not signsort(b)[i] < 0 

c = [1,-2,100,-1]
for i in range (2,3):
    assert signsort(c)[i] > 0
    assert not signsort(c)[i] < 0
for i in range(0,1):
    assert signsort(c)[i] < 0 
    assert not signsort(c)[i] >= 0

'''Only negative integers in array'''
d = [-1,-1,-100,-999, -500]
for i in range(0,len(d)):
    assert signsort(d)[i] < 0


'''Only positive integers'''
e = [1, 2, 3, 5, 10, 11, 9]
for i in range(0, len(e)):
    assert signsort(e)[i] >= 0

'''Testing for floats'''
f = [2.9, -2.4, 2.8, -2.5, 5, -500.5]
for i in range(0, 2):
        assert signsort(f)[i] < 0 
        assert not signsort(f)[i] >= 0
for i in range(3, len(f)):
    assert signsort(f)[i] >= 0
    assert not signsort(f)[i] <0

'''all passed'''