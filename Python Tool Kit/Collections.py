import collections

# namedtuple - when we want to make a tuple that is more readable and accesable but not too much like a class
Point = collections.namedtuple("Point", ["x", "y"])
p1 = Point(10,20)
print(p1)  # Point(x=10, y=20)
p2 = Point(30,40)
print(p2)  # Point(x=30, y=40)
p1 = p1._replace(x=0)
print(p1.x)  # 0
print(p1._fields)  # ('x', 'y')
print(p1._asdict())  # {'x': 0, 'y': 20}
print(Point._make([5,5]))  # Point(x=5, y=5)

# defaultdict - have init value if key is not in dict
from collections import defaultdict
our_dict = defaultdict(int)
our_dict["new_key"] += 1  # init to 0 and then += 1
print(our_dict["new_key"])  # 1

our_dict = defaultdict(list)  # set our similar
our_dict["new_key"].append("first val")  # init to [] and then appends "first val"
print(our_dict["new_key"])  # ['first val']

our_dict = defaultdict(str)
our_dict["new_key"] += "a"  # init to "" and then appends "a"
print(our_dict["new_key"])  # a

our_dict = defaultdict(lambda: 100)  # start at 100
our_dict["new_key"] += 10  # init to "" and then appends "a"
print(our_dict["new_key"])  # 110



