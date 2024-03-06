"""
loop: while [] output => [5,4,3,2,1,0]
"""

def fn_hack_7():
    result = []
    contador = 0
    while contador < 6:
        result.append(contador)
        contador += 1
    result.reverse()
    return result
