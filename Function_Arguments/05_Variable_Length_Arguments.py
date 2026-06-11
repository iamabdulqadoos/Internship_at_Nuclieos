# Sometimes we don’t know in advance how many values a function will receive.
# For that, Python gives us Variable Length Arguments.

def Numbers(*args):
    print("The Numbers are:", args)

Numbers(1,2,3,4,5,6,7,8,9,10)
Numbers(101,674,322,22,4,5,7,9)