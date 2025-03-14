import logging
import typer

# Logging configuration
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

app = typer.Typer()

@app.command()
def square(number: int):
    """The function calculates the square of a number and displays the result."""
    result = number ** 2
    logger.info(f"Calculating the square of {number}: {result}")
    print(result)

if __name__ == "__main__":
    app()



