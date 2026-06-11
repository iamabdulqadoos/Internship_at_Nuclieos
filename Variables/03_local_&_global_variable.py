# There might be some scenarios, where the global variable names and local variable names are the same.
# In such cases, within the function, by default, the local variables are only
# referred and the global variables are ignored.

a=10
b=20
def app():
    a=30
    b=40
    print(a+b)

def app2():
    print(a+b)

app() # This will print 70 because a and b are local variables and we can access them in the function.
app2() # This will print 30 because a and b are global variables and we can access them in the function.