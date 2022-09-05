# isinstance(object, classinfo) - return True if object is from type classinfo even is from inherited class.
from typing import List

print(isinstance([1,2,3], list))  # True
# print(isinstance([1,2,3], List[int]))  # not working
print(isinstance([1,2,3], (int, list)))  # classsinfo can be tuple of classes name # True
class Foo:
    a = 5
fooInstance = Foo()
print(isinstance(fooInstance, Foo))  # True
print(isinstance(fooInstance, (list, tuple)))  # False
print(isinstance(fooInstance, (list, tuple, Foo)))  # True

# issubclass()

# object()

# next()

# repr()

# __import__()

# type()

# super()
