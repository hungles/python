import platform

x = platform.system()
y = platform.architecture()
print(x)
print(y)

all_methods = dir(platform)
print(all_methods)
