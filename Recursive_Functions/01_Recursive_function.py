# A recursive function is a function that calls itself to solve a problem. It is a powerful tool for solving problems that can be broken down into smaller, similar subproblems. The key to writing a recursive function is to define a base case that stops the recursion and a recursive case that breaks the problem into smaller subproblems.
# Here is an example of a recursive function that calculates the factorial of a number:
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(6)) # This will print 720 because 6! = 6 * 5 * 4 * 3 * 2 * 1 = 720
