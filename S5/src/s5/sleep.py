import time
from log import audit

@audit
def wait():
    time.sleep(1)

if __name__ == "__main__":
    wait()
    