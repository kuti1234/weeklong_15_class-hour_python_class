''' this module is for functions we write in class.
'''
from typing import Union

def get_cube_root(n: Union[int, float, complex]) -> Union[int, float, complex]:
    ''' Returns the cube root of an int, float, or imaginary number.
        >>>get_cube_root(27)
        3.0
    '''
    assert isinstance(n, (float, int, complex)), "the argument must be a number."
    return n ** (1/3)

def get_gc_content_per(nuclStr: str) -> float:
    ''' Returns the percentage of G+C in a nucleotide string as a float.
        >>>get_gc_content_per('gattacagattaca')
        28.57142857142857
    '''
    nuclStr = nuclStr.lower()
    assert isinstance(nuclStr, str), "input must be a clean nucleotide string."
    bad_values = {}
    for index, value in enumerate(nuclStr):
        if value not in 'acgt':
            bad_values[index] = value
    assert not bad_values, f"input string has non-nucleotides in it:\n{bad_values}"
    # the variable name we give to the argument is used in the function's block of code
    return 100*((nuclStr.count('g') + nuclStr.count('c'))/len(nuclStr))

def euclid_gcd(natA:int, natB:int) -> int:
    ''' Returns the greatest common divisor of two natural numbers.
        >>>euclid_gcd(53667, 25527)
        201
    '''
    assert isinstance(natA, int) and (natA > 0) and isinstance(natB, int) and (natB > 0), "the input must be two natural numbers greater than zero."

    # implementation of the algorithm
    while natB:
        natA, natB = natB, natA % natB
    return natA

def rev_compl(nuclStr:str) -> str:
    ''' Returns the reverse complement of a nucleotide string.
        >>>rev_compl('gattaca')
        'tgtaatc'
    '''
    # garbage filters go here. (hint: same garbage filters as we wrote for get_gc_content_per())

    # implementation of the algorithm
    pass.
