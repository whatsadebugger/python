def keywordargsprint(**args_list):
    print(args_list["one"])
    print(args_list["two"])

def kwargsargs(*args, **kwargs):
    print(type(args))
    print(args)

    print(type(kwargs))
    print(kwargs)

# args is a tuple while, kwargs is a dict

keywordargsprint(one="one", two="two")
print()

kwargsargs(1, 2, 3, 4, one="one", two="two")
print()

# how to expand the tuple and dict into the method call

args = (1,2)
kwargs = {"one": 1, "two": 2}
kwargsargs(*args, **kwargs)