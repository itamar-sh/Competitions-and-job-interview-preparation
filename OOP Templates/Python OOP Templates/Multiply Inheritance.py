class A:
    def __init__(self) -> None:
        super().__init__()
        self.name = "A"

class B:
    def __init__(self) -> None:
        super().__init__()
        self.name = "B"

class C(A,B):
    def print_name(self):
        print(self.name)

c = C()
print(c.name)  # "A"
# because A before B in (A,B) so the __mro__ will take A before B:
print(C.__mro__)  # (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
