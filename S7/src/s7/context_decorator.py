from contextlib import contextmanager
import logging

logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

@contextmanager
def open_file(filename, mode):
    print(f"Opening file {filename}")
    try:
        f = open(filename, mode)
        yield f
    except FileNotFoundError:
        #raise FileNotFoundError(f'File {filename} not found')
        logging.error(f'File {filename} not found')
    finally:
        print(f"Closing file {filename}")
        f.close()


# Usage example:
if __name__ == "__main__":
        with open_file("example.txt", "a") as f:
            f.write("\nAppending with context manager using @contextmanager.")


    
