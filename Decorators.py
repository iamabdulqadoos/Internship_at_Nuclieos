import time

def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()

        print("Execution Time:", end - start)

    return wrapper

@timer
def task():
    time.sleep(4)
    print("Task Completed")

task()