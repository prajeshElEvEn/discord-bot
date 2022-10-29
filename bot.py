import discord
import responses
import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


async def sendMessage(message, userMessage, isPrivate):
    try:
        response = responses.handleResponse(userMessage)
        await message.author.send(response) if isPrivate else await message.channel.send(response)
    except Exception as e:
        print(f"[!] `Oops! error occurred. {e}`")


def runBot():
    TOKEN = os.getenv('TOKEN')
    client = discord.Client(intents=discord.Intents.all())

    @client.event
    async def onReady():
        print(f'[+] {client.user} is now running!')

    client.run(TOKEN)
