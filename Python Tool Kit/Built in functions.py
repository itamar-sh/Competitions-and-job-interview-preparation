# abs() - get a int or float and return the abs value


print(abs(-124))  # 124
print(abs(-67.5))  # 67.5

# any() - gets iterable and return True if at least one element is not False, aka not False/0, Empty iterable also False
print("any()")
print(any("120"))  # True
print(any("000"))  # True - "0" is not 0 but 48
print(any(""))  # False
print(any([]))  # False
print(any([""]))  # False
print(any([0,0,0]))  # False
print(any([0,1,0]))  # True
print(any([False, False]))  # False
print(any([True, False]))  # True

# all like any -only if everything is True or not 0. - But empty now is True
print("all()")
print(all("120"))  # True
print(all("000"))  # True - "0" is not 0 but 48
print(all(""))  # True
print(all([]))  # True
print(all([""]))  # False
print(all([0,0,0]))  # False
print(all([0,1,0]))  # False
print(all([False, False]))  # False
print(all([True, False]))  # False
print(all([True, True]))  # True

# bin() - gets int return its binary representation as string start with 0b
print("bin()")
print(bin(0))  # "0b0"
print(bin(1))  # "0b1"
print(bin(2))  # "0b10"
print(bin(15))  # "0b111"
print(bin(-2))  # "-0b10"
print(bin(-15))  # "-0b111"
print(bin(2147483647))  # "0b1111111111111111111111111111111"
print(bin(-2147483648))  # "-0b10000000000000000000000000000000"
print(bin(9223372036854775807))  # "0b111111111111111111111111111111111111111111111111111111111111111"
import sys
print(bin(sys.maxsize))          # "0b111111111111111111111111111111111111111111111111111111111111111"

# bool() - return True or False base on one argument
print("bool()")
print(bool(1))  # True
print(bool(254))  # True
print(bool(25.14))  # True
print(bool(-25.14))  # True
print(bool("python"))  # True
print(bool("0"))  # True
print(bool(True))  # True
print(bool(0))  # False
print(bool(""))  # False
print(bool([]))  # False
print(bool(None))  # False
print(bool(False))  # False

# enumerate() - return generator of tuples: each tuple like that: (i, value)
text = "abc"
print(list(enumerate(text)))  # [(0, 'a'), (1, 'b'), (2, 'c')]
lst = ["a","b",4]
print(list(enumerate(lst)))  # [(0, 'a'), (1, 'b'), (2, 4)]

# callable() - return True if arg is callable
print(callable(lambda a: a+1))  # True
print(callable("aa"))  # False



