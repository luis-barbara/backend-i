import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        finish = time.time()
        print(f"Tempo de execução: {finish - start:.2f} segundos")
        return result
    return wrapper

@measure_time
def calculator():
    time.sleep(3)


if __name__ == "__main__":
    calculator()
