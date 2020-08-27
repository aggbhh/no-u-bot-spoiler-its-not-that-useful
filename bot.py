#bot.py
import os
import random
import discord
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('bot-token-here')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
@client.event
async def on_message(message):
    if '!no u' in message.content.lower():
        await message.channel.send('no u')
        print("sent no u")
    elif '!help' in message.content.lower():
        await message.channel.send('the prefix is !. Commands: no u, random number')
    elif '!random number' in message.content.lower():
        random_num = random.randint(1,100000000)
        strrandnum=str(random_num)
        await message.channel.send('your random number is: '+ strrandnum +" ")
        print("sent your random number is: "+ strrandnum +" ")
    

client.run("bot-token-here")
