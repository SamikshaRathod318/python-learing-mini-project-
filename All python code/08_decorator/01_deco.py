import time 

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__}: {end_time - start_time} time")
        return result
    return wrapper

@timer
def example_function(n):
    time.sleep(n)
example_function(2)

  