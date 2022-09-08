# has attr(obj, str) - return True if there is instance attribute with this name for the object.
class AdvancedClass:
    def make_some_instance_attributes(self, val1: str, val2: int):
        self.val1 = val1
        self.val2 = val2

    def use_some_instance_attributes(self):
        if hasattr(self, "val1"):  # !!!
            print(self.val1)
        else:
            print(None)

o = AdvancedClass()
o.use_some_instance_attributes()  # None
o.make_some_instance_attributes("val1", 5)
o.use_some_instance_attributes()  # val1

# @classmethod - this is the way to make class methods (static methods) in python
class ClassWithStaticMethods:
    class_attr = ["a","b"]
    @classmethod
    def some_class_level_method(cls):
        cls.class_attr.append(chr(ord(cls.class_attr[-1])+1))  # add the next char in abcde order

print(ClassWithStaticMethods.class_attr)  # ["a","b"]
ClassWithStaticMethods.some_class_level_method()
print(ClassWithStaticMethods.class_attr)  # ["a","b","c"]

# @staticmethod - this is not the regular static method as we know. it's only function inside the scope of the class
# But actually it's should not touch any of it's attributes.
# One use for this is singleton
class Singleton:
    __our_lst = None  # private

    @staticmethod
    def get_out_lst():
        if Singleton.__our_lst:
            return Singleton.__our_lst
        else:
            Singleton.__our_lst = []
            return Singleton.__our_lst

# if we try to init by ourself it's would raise an error:
try:
    print(Singleton.__our_lst)  # raise error
except:
    print("error occured")
# but this will work
print(Singleton.get_out_lst())  # []
# of course, there isn't really private in python so:
Singleton._Singleton__our_lst.append(1)  # will work



