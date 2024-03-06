"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    contador = 1
    while contador < 6:
        result.insert(contador,'@')
        contador += 2
    return result  

