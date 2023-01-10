

def p(h, n, cache={}):
    '''We use the same recursive call as previous, with the adjustment that if
    our length oadasdasadasdadasdasdasdsaf cotton thread is already stored in the cache with a corresponding profit value,
    we can return that value instead of going through another recursive call. '''
    
    profit = 0

    if cache == {}:
        cache = {0:0} 

    if h == []:
        h = [0]

    assert h[0] == 0
    
    if n in cache.keys():
        return cache[n]
    if n== 0:
        return 0

    for i in range(1, min(n+1, len(h))):
        profit = max(profit, h[i] + p(h, n-i, cache))

    cache[n]=profit
    assert cache[0] == 0
    #print(cache)
    return profit
    
a = [0,2,5,6,9]
b = [] 
c = [0,4, 7]

'''Hard-coding some test-cases'''

assert p(b, 0) == 0
assert p(a, 5) == 12
assert p(a, 0) == 0
assert p(c, 10) == 40
correct_values = [0, 2, 5, 7, 10, 12, 15, 17, 20, 22, 25, 27, 30, 32, 35, 37, 40, 42, 45, 47]

for i in range(0, 20):
    assert p(a, i) == correct_values[i]

'''All passed'''