from typing import Any


class Book:
    def __init__(self, name, price = 0) -> None:
        super().__init__()
        self.name: str = name
        self.price = price

    # call when use print() or str()
    def __str__(self) -> str:
        return f"The name is: {self.name}"

    # call when use repr()
    def __repr__(self) -> str:
        return f"name=\"{self.name}\""

    # call when use ==
    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Book):
            raise ValueError("Can't compare two Object that are not Book type")
        else:
            return self.name == o.name

    # call when < is performed
    def __lt__(self, other):
        if not isinstance(other, Book):
            raise ValueError("Can't compare two Object that are not Book type")
        else:
            return self.price < other.price
    # another names: gt: >, le: =<, ge: >=, ne: !=

# repr, str
b = Book("War And Peace")
print(b)  # The name is: War And Peace
print(str(b))  # The name is: War And Peace
print(repr(b))  # name="War And Peace"

# eq
b1 = Book("War And Peace")
b2 = Book("War And Peace")
b3 = Book("Between Two cities")
print(b1 == b2)  # True
print(b3 == b2)  # False

# lt
p1 = Book("C", 1)
p2 = Book("B", 3)
p3 = Book("A", 2)
print(p1 < p3 < p2)  # True
sorted_p = [p1,p2, p3]
sorted_p.sort()  # we only need < or > for sorting, <= or >= is not enough.
print(sorted_p)  # [name="C", name="A", name="B"]

# getattribute, setattr, getattr

class Computer:
    accessed_of_objects_attributes = 0
    def __init__(self, model, price = 0.0) -> None:
        super().__init__()
        self.model: str = model
        self.price = price

    # call when use print() or str()
    def __str__(self) -> str:
        return f"The model is: {self.model}"

    # call when we try to use self.model or self.price
    def __getattribute__(self, name: str):
        Computer.accessed_of_objects_attributes += 1
        if name == "price":
            return super().__getattribute__("price")
        elif name == "model":
            return super().__getattribute__("model")  # we cant use self.name because it's call this function
        else:
            return super().__getattribute__(name)  # jump to __getattr__

    # call when we try to set self.model or self.price
    def __setattr__(self, name: str, value: Any) -> None:
        if name == "price":
            if type(value) is not float:
                raise ValueError("price should be float")
            else:
                return super().__setattr__("price", value)
        elif name == "model":
            return super().__setattr__("model", value)
        else:
            return super().__setattr__(name, value)
    # call only of one of three options:
    # 1) the attribute isn't exist.
    # 2) __getattribute__ isn't exist.
    # 3) __getattribute__ throws exception
    def __getattr__(self, item: str):
        # return item + "is not here"
        super().__setattr__(item, 0)  # return None but ini a new attribute
        return super().__getattribute__(item)

try:
    c = Computer("lenovo", 40)
except:
    print("raise ValueError(\"price should be float\")")

c2 = Computer("lenovo", 40.0)
print(Computer.accessed_of_objects_attributes)  # 0
print(c2.model, c2.price)  # lenovo 40.0
print(Computer.accessed_of_objects_attributes)  # 2

print(c2.new_item)  # 0

# call
class Animal:
    def __call__(self, *args, **kwargs) -> 'Animal':
        print("Object Animal is Called and now we return a baby")
        return Animal()
a = Animal()
print(a)    # <__main__.Animal object at 0x000001A6EF56C7F0>
print(a())  # Object Animal is Called and now we return a baby
            # <__main__.Animal object at 0x000001A6EF56C640>
            # We even can see they put the objects next to each other.




