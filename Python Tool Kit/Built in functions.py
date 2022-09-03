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

# map() - gets two arguments - one if function name and the other is iterable. Return iterator.
print(list(map(lambda a: a+1, [1,2,3,4])))  # [2,3,4,5]
print(list(map(int, ["1","2","3","4"])))  # [1,2,3,4]
# map() - gets x+1 arguments when 1 is functions that gets x arguments and return a value.
print(list(map(lambda a, b: a+b, [2], [3])))  # [5]
print(list(map(lambda a, b: a+b, [2,3,4], [3,4,5])))  # [5,7,9]
print(list(map(lambda a, b: a+b, [2,3,4], [3,4])))  # [5,7] # iterate only the min(len(iter1, iter2)
map_lst = [1,2,3,4,5]
print(list(map(lambda a,b,c,d,e : a+b+c+d+e, map_lst, map_lst, map_lst, map_lst, map_lst)))  # [5, 10, 15, 20, 25]

# filter() - gets function and iterable and return iterable of values that return True after from the func.
letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']
def filter_vowels(letter):  # a function that returns True if letter is vowel
    vowels = ['a', 'e', 'i', 'o', 'u']
    return True if letter in vowels else False
print(tuple(filter(filter_vowels, letters)))  # ('a', 'e', 'i', 'o')
print(list(filter(lambda x: (x%2 == 0), [1, 2, 3, 4, 5, 6, 7])))  # [2, 4, 6]

# reversed() - gets one sequence_object, not dict or set but tuple or list or range. return reversed iterator.
seq_tuple = ('P', 'y', 't', 'h', 'o', 'n')
print(list(reversed(seq_tuple)))  # ['n', 'o', 'h', 't', 'y', 'P']
print(list(seq_tuple))  # Not in-place: ['P', 'y', 't', 'h', 'o', 'n']
class Vowels:
    vowels = ['a', 'e', 'i', 'o', 'u']
    def __reversed__(self):
        return reversed(self.vowels)
print(list(reversed(Vowels())))  # custom operator: ['u', 'o', 'i', 'e', 'a']

# range(start=0, stop, step=1) - very intuitive, we get an iterator
print(list(range(4, -1, -1) ))    # [4, 3, 2, 1, 0]

# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False), many objects, file can be  from: open("..", "w")
print('a =', 5, '= b', flush=True)  # a = 5 = b        # will immediately print

# pow(number, power, modulus [optional]), (number^power)%modulus
print(pow(7, 2, 5))  # 4       7^2%5=49%5=4      equal to: (7**2)%5
print(pow(-2, -2))   # 0.25   (-2)^(-2)=1/((-2)^2)=1/4     equal to (-2)**-2

# max(), min() - syntax 1: max(iterable, *iterables, key, default=ValueError)
#                          *iterables for more than one iter, key to comparison, default for case of empty iter.
#              - syntax 2: max(arg1, arg2,args*, key)
# #                          *args for more than two args, key to comparison.
print("The largest first value more than one iterables:", max([0,2,3,4],[1,-2],[-2,9,0]))    # [1,-2] because 1 > 0> -2
print("The longer from more than one iterables:", max([0,2,3,4],[1,-2],[-2,9,0], key=len))    # [0, 2, 3, 4]
print("The shortest from more than one iterables:", min([0,2,3,4],[1,-2],[-2,9,0], key=len))    # [1, -2]
square = {2: 4, -3: 9, -1: 1, -2: 4}  # dict
print("The largest key:", max(square))    # 2
print("The largest value:", max(square.values()))    # 9
print("The key with the largest value:", max(square, key=lambda k: square[k]))    # -3
print(max(("python", "lua", "ruby"), key=len))  # "python"
print(max("c", "b", "a", "Y", "Z", key=str.lower))  # "Z"
print("max from args: ", max(2,4,6,7,8,-2))  # 8

# vars() - gets one argument - and return dictionary of their properties. The object can be anything with __dict__ attr.
class Fruit:
    def __init__(self, apple=5, banana=10):
        self.apple = apple
        self.banana = banana
eat = Fruit()
# returns __dict__ of the eat object
print(vars(eat))  # {'apple': 5, 'banana': 10}
print(vars("Jones"))  # error
print(vars(list))  # {'__repr__': <slot wrapper '__repr__' of 'list' objects>, '__hash__': None, .....}











