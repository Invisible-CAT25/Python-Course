import re

s = "python is a programming language"
pattern = "[a-z]"

# x = re.match(pattern,s)
# x = re.fullmatch(pattern,s)
# x = re.search(pattern,s)
# x = re.findall(pattern,s)
# x = re.sub(pattern,"X",s,2)
# x = re.subn(pattern,"X",s,2)
# x = re.split(pattern,s)
# print(x)

x = re.findall(pattern,s)
print(x)