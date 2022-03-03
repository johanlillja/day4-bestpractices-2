"""
A collection of simple math operations for two numbers a,b

    Parameters
    ----------
    a : type
        float
    b : type
        float
    x : type
        float
        
    Returns
    -------
        float
        
    Warnings
    --------
    for simmple_div b = 0 is undefined
    
    
"""

def simple_add(a,b):
    return a+b

def simple_sub(a,b):
    return a-b

def simple_mult(a,b):
    return a*b

def simple_div(a,b):
    return a/b

def poly_first(x, a0, a1):
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    return poly_first(x, a0, a1) + a2*(x**2)

# Feel free to expand this list with more interesting mathematical operations...
# ....