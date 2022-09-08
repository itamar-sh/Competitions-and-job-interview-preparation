from abc import ABC, abstractmethod

# inherent from ABC + making at least one method with @abstractmethod will enforce the constraints for abstract clas/
class Shape(ABC):  # ABC is short for AbstractClass -
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def calc_area(self):  # must be override by derived class
        pass

try:
    Shape()  # Shape is Abstract Class so no object can be directly initialized.
except:
    print("TypeError: Can't instantiate abstract class Shape with abstract method calc_area")

class Circle(Shape):
    pass

try:
    c = Circle()  # calc_area was not override.
except:
    print("TypeError: Can't instantiate abstract class Circle with abstract method calc_area")

class Rectabgle(Shape):
    def calc_area(self):  # No need for some @override
        return 10

print(Rectabgle().calc_area())  # 10
