# The problem of local variables not available, due to the use of global keywords can be overcome
# by using the Python built-in function called globals(). The globals() is a built-in function 
# that returns a table of current global variables in the form of a dictionary. 
b=10
def app():
    a=20
    globals()['b']=20
    print(a+b)

app() # This will print 40 because a is a local variable and b is a global variable and we can access them in the function.