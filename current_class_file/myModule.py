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
