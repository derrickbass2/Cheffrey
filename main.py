import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.typing = False  # Disable typing events for performance improvement
intents.presences = False  # Disable presence events for performance improvement

bot = commands.Bot(command_prefix='!', intents=intents)
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
@bot.command()
async def hello(ctx):
    await ctx.send('Hello, I am Cheffrey! How can I assist you today?')
import discord

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

intents = discord.Intents.default()

bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user.name}')

bot.run('MTExMzc1NTUyODUyNzYwOTg1Ng.G24dhq.eUXGwZtgCOc3cLG6EF5vwd9sN5aDmfrCsCMIVg')










