import logging
import sys
from datetime import datetime
import time

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(sys.stdout))




class FileOpener:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
        self.start_time= time.perf_counter()
        self.finish_time= time.perf_counter()



    def __enter__(self):
        self.start_time = time.perf_counter()
        logger.info(f"start at {datetime.now()}")
        print(f"Opening file {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing file {self.filename}")
        if self.file:
            self.file.close()
        end_time = time.perf_counter()
        execution_time = end_time - self.start_time
        logger.info(f"finish at {datetime.now()}")
        logger.info(f"Execution time: {execution_time:} seconds")
        # Do not suppress exceptions
        return False


    
# Usage example:
if __name__ == "__main__":
    with FileOpener("example.txt", "w") as f:
        f.write("Hello, Context Managers!")


 

