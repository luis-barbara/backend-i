import functools


def caching_result(func):
    cached_results = {}  
    @functools.wraps(func)
    def wrapper(*args, **kwargs):  
        if args in cached_results:
            print(f"Fetching from cache: factorial({args[0]})")
            return cached_results[args]
        result = func(*args, **kwargs)
        cached_results[args]=result
        return result
    return wrapper


@caching_result      
def factorial(n):
    if n == 0 or n == 1:
        return 1  
    return n * factorial(n-1) 


if __name__ == "__main__":
    print(factorial(10))
    print(factorial(1))
    print(factorial(10))