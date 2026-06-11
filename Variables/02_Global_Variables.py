# The variables which are declared outside of the function are called global variables.
# Global variables can be accessed in all functions of that module.
a=10
b=20
def app():
    print(a+b)

def app2():
    print(a)

app() # This will print 30 because a and b are global variables and we can access them in the function.
app2() # This will print 10 because a is a global variable and we can access it in the function.