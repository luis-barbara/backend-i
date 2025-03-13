import typer
from bot import run_bot
import os

token = os.getenv('DOCKER_TOKEN', None)
app = typer.Typer()

@app.command()
def start():
    """
    Start the Discord bot using the provided token.
    """
    run_bot(token)


@app.command()
def welcome(username: str):
    """
    Gera uma mensagem de boas-vindas personalizada para um usuário.
    """
    message = welcome(username)
    print(message) 
   

if __name__ == "__main__":
    app()