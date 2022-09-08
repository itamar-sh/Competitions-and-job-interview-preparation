from typing import List


class Parent:
    static_member1: int
    static_member2: str
    static_member3: List

    def __init__(self):
        self.member1: int
        self.member2: str
        self.member3: List

    def method1(self):
        pass

    def method2(self):
        pass

class Child(Parent):
    __private_member: int
    def __init__(self):
        super().__init__()

    @staticmethod
    def static_method1(arg1, arg2):
        Child.static_member1 = 1
        Child.static_member2 = "2"
        Child.static_member3 = []
        Child.__private_member = -1

c = Child()
Child.static_member1 = "ab"
print(c.static_member1)  # "ab"
print(Child.static_member1)  # "ab"
c.member1 = 5
print(c.member1)  # "5
c.method1()
Child.static_method1(1, 2)
print(Child.static_member3)  # []
