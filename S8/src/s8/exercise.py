from typer import Typer
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
logger.addHandler(console_handler)


app = Typer()

class InvalidNumberError(Exception):
    pass

@app.command()
def square(number: int):
    if number > 10:
        logger.error(f'number {number} must be <= 10')
        raise InvalidNumberError(f"number {number} must be <= 10")
    else:
        print(f'{number**2}')
    

if __name__ == "__main__":
    app()

