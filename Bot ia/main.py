import discord
import random
from discord.ext import commands
from flask import ctx


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot.command()
async def cargar(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            if attachment.content_type and attachment.content_type.startswith('image/'):
                await ctx.send(f"Aquí está tu imagen y la URL: {attachment.url}")
            else:
                await ctx.send("Eso no es una imagen.")
    else:        
        await ctx.send("No encuentro ningún archivo")
        
bot.run("MTQyMTIzNDI4OTY5NzA5OTc4Ng.Gpct6Y.00tylggpHLt9f6_yXN5zDOT6-pyQfQZl0e4Bxs")

    