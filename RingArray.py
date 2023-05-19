# %%
import numpy as np
from itertools import cycle

'''
Numpy subclass information
https://numpy.org/doc/stable/user/basics.subclassing.html

'''

class RingArray(np.ndarray):
    """A modified numpy array type that functions like a queue. 
    RingArray has a set size specified during initialisation. 
    Add new data using the append() method, which will replace the 
    next value in a cyclical fashion. The array itself has all the 
    properties of a numpy array e.g. it can be sliced and accessed as 
    normal. Initially fills the array with np.nan values.
    
    Options
    --------
    shape : tuple
        A tuple of (height, width) for the maximum size of the array.

    Attributes
    ----------
    Inherited from nd.array. Initially fills array with np.nan values.
    
    Methods
    --------
    append(data)
        Add/replace data in the next element of the cycle.
        Data should be the length of the RingArray width.
    
    """    
    def __new__(subtype, shape):
        obj = super().__new__(subtype, shape)
        
        obj = np.vectorize(lambda x: np.nan)(obj)
        
        obj._pointer = cycle(np.arange(0, shape[0]))
        
        return obj
    
    # needed by numpy
    def __array_finalize__(self, obj):
         if obj is None: return
        
    # add data to the next element (looped)
    def append(self, data):
        """Adds or replaces data in the RingArray.
        The function writes to the next row in the Array.
        Once the last row is reached, the assignment row 
        loops back to the start.

        Parameters
        ----------
        data : array_like
            Data should be the length of the RingArray width.
        """        
        self[next(self._pointer)] = data
        

# %%
