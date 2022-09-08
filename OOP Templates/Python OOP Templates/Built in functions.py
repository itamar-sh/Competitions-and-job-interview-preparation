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

# object() - The object() function returns a featureless object which is a base for all classes.
o = object()
print(type(o), dir(o))

# iter(object) - The  method returns an iterator for the given argument.
# The object has to have __iter__ implemented.
# list of vowels
vowels_iter = iter(["a", "e", "i", "o", "u"])  # example 1
print(next(vowels_iter))  # "a
print(next(vowels_iter))  # "e
class PrintNumber:  # example 2
    def __init__(self, max):
        self.max = max
    def __iter__(self):  # can return himself because __next__ is implemented
        self.num = 0
        return self
    def __next__(self):
        if self.num >= self.max:
            raise StopIteration
        self.num += 1
        return self.num
print(next(iter(PrintNumber(3))))  # 1

# next(iterator, default)
# default (optional) - this value is returned if the iterator is exhausted (there is no next item)
iterator_marks = iter([65, 71, 68, 74, 61])
print(next(iterator_marks))  # 65
# print(next([65, 71, 68, 74, 61])) - won't work

# repr(obj) - take obj and use the __repr__ of this object.
print(repr('foo'))  # 'foo'

# The type() function has two different forms:
# type(object) - return type of the object
lst, dct,foo = {}, [], lambda a: a+1
print(type(lst), type(dct), type(foo))  # <class 'dict'> <class 'list'> <class 'function'>
class Foo:
    a = 0
foo = Foo()
print(foo, Foo)  # <__main__.Foo object at 0x0000024FEC7BC820> <class '__main__.Foo'>
# type(name, bases, dict) -
# name - a class name; becomes the __name__ attribute.
# bases - a tuple that itemizes the base class; becomes the __bases__ attribute.
# dict - a dictionary which is the namespace containing definitions for the class body; becomes the __dict__ attribute.
new_type = type('X', (object,), dict(a='Foo', b=12))
print(type(new_type))  # <class 'type'>
print(vars(new_type))  # {'a': 'Foo', 'b': 12, '__module__': '__main__', '__dict__': <attribute '__dict__' of
                       # 'X' objects>, '__weakref__': <attribute '__weakref__' of 'X' objects>, '__doc__': None}

# super() - The super() builtin returns a proxy object (temporary object of the superclass) that allows us to access
# methods of the base class.

# uses of super: 1) Allows us to avoid using the base class name explicitly.
#                2) Working with Multiple Inheritance
class Animal:
    def __init__(self, animal_type):
        print('Animal Type:', animal_type)

class Mammal(Animal):
    def __init__(self):
        # call superclass
        super().__init__('Mammal')   # equal to: Animal.__init__(self, 'Mammal')
        print('Mammals give birth directly')
dog = Mammal()  # Animal Type: Mammal
#                 Mammals give birth directly

# __mro__ - Method Resolution Order (MRO) is the order in which methods should be inherited in the presence of multiple
# inheritance. You can view the MRO by using the __mro__ attribute.
print(Mammal.__mro__)  # (<class '__main__.Mammal'>, <class '__main__.Animal'>, <class 'object'>)





