# RingArray
An efficient circular buffer that subclasses NumPy ndarray.

A fixed-size array that can be appended to infinitely. The append function adds the data to the next element in sequence. Once the numpy array is full the append function will replace the items from the first item to the last. 

This is a more efficient solution to using np.roll, which translates the elements in the array so that new data is added to the top of the array. np.roll does not scale well with larger arrays. 

This was submitted as an answer on stackoverflow: https://stackoverflow.com/a/76084278/21712909
