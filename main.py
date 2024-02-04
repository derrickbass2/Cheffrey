import discord
from discord.ext import commands

INTENTS = discord.Intents.default()
INTENTS.typing = False
INTENTS.presences = False

TOKEN = 'MTExMzc1NTUyODUyNzYwOTg1Ng.G24dhq.eUXGwZtgCOc3cLG6EF5vwd9sN5aDmfrCsCMIVg'

bot = commands.Bot(command_prefix='!', intents=INTENTS)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@bot.command()
async def hello(ctx):
    await ctx.send('Hello, I am Cheffrey! How can I assist you today?')

if __name__ == "__main__":
    bot.run(TOKEN)







