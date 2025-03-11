import time


class FileOpener:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.start_time = time.perf_counter()
        print(f"Opening file {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
       
        print(f"Closing file {self.filename}")
        if self.file:
            self.file.close()
        self.end_time = time.perf_counter()
        print(self.end_time-self.start_time)
        # Do not suppress exceptions
        return False


    
# Usage example:
if __name__ == "__main__":
    with FileOpener("example.txt", "w") as f:
        f.write("Hello, Context Managers!")


 

