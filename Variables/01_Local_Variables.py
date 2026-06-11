# The variables which are declared inside of the function are called local variables.
# Their scope is limited to the function i.e we can access local variables within the function only.

def app():
    a=10
    b=20
    print(a+b)

app()
def app2():
    print(a)

app2() # This will give an error because a is a local variable and we cannot access it outside of the function.