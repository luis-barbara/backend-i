from typer import Typer

app = Typer()


@app.command()
def square(number: int):
    print(f'{number**2}')

@app.command()
def addition(number: int):
        print(f'{number+2}')

@app.command()
def subtraction(number: int):
        print(f'{number-2}')

if __name__ == "__main__":
    app()