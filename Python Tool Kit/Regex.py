import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)  # Returns a Match object if there is a match anywhere in the string
print(x)  # <re.Match object; span=(0, 17), match='The rain in Spain'>
print(x.string)  # The rain in Spain
print(x.span())  # (0, 17)
print(x.start())  # 0
print(x.end())  # 17
print(x.regs)  # ((0, 17),)
print(x.group())  # The rain in Spain
# search return None if no match has found
print()
