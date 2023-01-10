def fac(n):
    """Takes the factorial of the integer. The user is 
    assumed to have made the correct type of input (int)"""
    if n == 0 :
        return 1
    return n*fac(n-1)

assert fac(6) == 720
assert fac(5) == 120
assert fac(0) == 1
print(fac(17))