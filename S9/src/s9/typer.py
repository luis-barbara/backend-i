import discord
import typer
from bot import run_bot
import os

token = os.getenv('DOCKER_TOKEN', None)
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

app = typer.Typer()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@app.command()
def start():
    """
    Start the Discord bot using the provided token.
    """
    run_bot(token)



@app.command()
def welcome(username: str):
    """
    Sends a welcome message to a specific Discord channel.
    """
    async def send_welcome():
        await client.wait_until_ready()  # Espera até que o bot esteja pronto
        channel = client.get_channel(CHANNEL_ID)
        if channel:
            await channel.send(f"Welcome to the server, {username}!")
        else:
            print("Erro: ID do canal inválido ou o bot não tem acesso.")

    client.loop.create_task(send_welcome())


if __name__ == "__main__":
    app()