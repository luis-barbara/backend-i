# This example requires the 'message_content' intent.

import discord
from dotenv import load_dotenv
import os

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

@client.event
async def welcome(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('hi'):
        await message.channel.send('Welcome, how can I help you?')

    if message.content.startswith('ola'):
        await message.channel.send('Ola, como estas hoje?')
        

client.run(os.getenv('DOCKER_TOKEN', None))
