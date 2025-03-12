import typer

def cenas(name: str, formal:bool = False):
    print(f'{name}')

if __name__ == "__main__":
    typer.run(cenas)