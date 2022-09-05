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

# issubclass(class, classinfo) - return True if class is from sub type of classinfo even is from inherited class.
class Polygon:
    def __init__(polygonType):
        print('Polygon is a ', polygonType)
class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__('triangle')
print(issubclass(Triangle, Polygon))  # True
print(issubclass(Triangle, list))  # False
print(issubclass(Triangle, (list, Polygon)))  # True - class info can be tuple.
print(issubclass(Polygon, (list, Polygon)))  # True - Polygon is sub class of himself.

# object()

# next()

# repr()

# __import__()

# type()

# super()
