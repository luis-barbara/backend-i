import typer

app = typer.Typer()

@app.command()
def hello(name: str):
    """
    Greet the user with their name.
    """
    typer.echo(f"Hello {name}")

if __name__ == "__main__":
    app()
    