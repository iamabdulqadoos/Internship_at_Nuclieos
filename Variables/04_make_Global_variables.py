# If you wants to use the global variable inside a function, then need to use a
# global keyword before the variable in the beginning of the function body.
def app():
    global a
    global b
    a=30
    b=40
    print(a+b)

def app2():
    print(a-b)

app() # This will print 70 because a and b are global variables and we can access them in the function.
app2() # This will print -10 because a and b are global variables and we can
