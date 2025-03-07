import time


def uptime():
    start = time.time()
    time.sleep(3)
    finish = time.time()
    print(f"Tempo de execução: {finish - start:.4f} segundos")


if __name__ == '__main__':
    uptime()

