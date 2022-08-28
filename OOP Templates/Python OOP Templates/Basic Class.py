from typing import List


class Dog:
    # class attribute
    attr1 = "mammal"

    # Instance attribute
    def __init__(self, name):
        self.name = name
        self.__private_attr = "cannot be used outside class or in derived class"
        self._protected_attr = "can be used only in instance of the Dog class not derived class"


    # Methods
    def speak(self):
        print("My name is {}".format(self.name))



# Driver code
# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

# Accessing class attributes
print("Rodger is a {}".format(Rodger.__class__.attr1))  # Rodger is a mammal
print("Tommy is also a {}".format(Tommy.__class__.attr1))  # Tommy is also a mammal

# Accessing instance attributes
print("My name is {}".format(Rodger.name))  # My name is Rodger
print("My name is {}".format(Tommy.name))   # My name is Tommy

# Accessing class methods
Rodger.speak()  # My name is Rodger
Tommy.speak()   # My name is Tommy


## Inheritance
# parent class
class Person:

    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self._name = name
        self.idnumber = idnumber

    def display(self):
        print(self._name)
        print(self.idnumber)

    def details(self):
        print("My name is {}".format(self._name))
        print("IdNumber: {}".format(self.idnumber))


# child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)

    def details(self):
        print("Post: {}".format(self.post))
        print(self._name)


# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")

# calling a function of the class Person using
# its instance
a.display()     # My name is Rahul
                # IdNumber: 886012
a.details()     # Post: Intern
b = Person("aa", 2)
print(b._name)
print(a._name)





