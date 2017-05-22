# python-streams
A module that wraps Python 3 iterators in delicious Java 8 stream syntax.

### Example:
```python
import itertools
from fractions import Fraction
import operator

L = [1,2,3,5,4]

print(Stream(L).filter(lambda ele: ele > 3) # Using only values greater than 3
               .map(lambda ele: ele * 2) # Double each value
               .sorted() # Sort the resulting list
               .reduce(operator.mul, seed=1)) # Return the product of the elements
	
# Start with an infinite stream [0,1,2, ...]
print(Stream().map(Fraction) # Turn everything into a fraction
              .map(lambda ele: ele / 3) # Divide everything by 3
              .map(str) # Turn everything into strings
              .limit(5) # Only use the first 5 elements
              .list()) # Return stream as list

print(Stream.iterate(-5, lambda prev: prev + 2) # Starting at -5, increment by 2
            .limit(10) # Take the first  10 values
            .list()) # Return stream as list
 ```
