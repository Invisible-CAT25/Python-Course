import re

data = "python is a programming language barrier carrier Apple16@#$%&"
pattern = r"."

x = re.findall(pattern,data)
print(x)