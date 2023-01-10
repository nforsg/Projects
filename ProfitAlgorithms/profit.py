def p(h, n):
    '''This function will eventually call itself with other parameters eventually.
    We modify the profit with regard to the amount of cotton left after each expensive scarf.'''
    if h == []:
        h = [0]
    assert h[0] == 0
    if n == 0:
        return 0
    profit = 0
    for i in range(1, min(n+1, len(h))):
        profit = max(profit, h[i] + p(h, n-i))
    return profit

a = [0,2,5,6,9]
c = [0,4, 7]
print(p(c, 10))
b = []
p(b,0) == 0
assert p(a, 0) == 0
assert p(a, 5) == 12
b = []
assert p(b,0) == 0


'''for i in range(0, 20):
    print(p(a, i))'''
#print(p(a, 5))