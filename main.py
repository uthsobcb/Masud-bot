import discord
import requests
from datetime import date, datetime
from discord.ext import commands
from discord.ext.commands import Bot
from decouple import config

TOKEN = config('TOKEN')
#Bot = discord.Client(intents = discord.Intents.all())

Bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())


@Bot.event
async def on_ready():
    print(f"Logged on {Bot.user}")


@Bot.command(name="spy")
async def spy_(ctx):
    if (not ctx.message.mentions):
        userID = ctx.message.content.split('.spy ')[1]
        user = await Bot.fetch_user(userID)

        embed = discord.Embed(colour=user.colour, timestamp=user.created_at)
        embed.set_author(name=f'("User Info - {user}")')
        embed.set_thumbnail(url=user.avatar)
        embed.add_field(name='ID:', value=user.id, inline=False)
        embed.add_field(name='Name:', value=user.display_name, inline=False)
        embed.add_field(name='Account Created at:',value=user.created_at, inline=False)
        await ctx.send(embed=embed)
    else:
        for user in ctx.message.mentions:
            embed = discord.Embed(colour=user.colour, timestamp=user.created_at)

            embed.set_author(name=f'("User Info - {user}")')
            embed.set_thumbnail(url=user.avatar)
            embed.add_field(name='ID:', value=user.id, inline=False)
            embed.add_field(name='Name:', value=user.display_name, inline=False)
            embed.add_field(name='Account Created at:',value=user.created_at, inline=False)
            embed.add_field(name='Joined at:',value=user.joined_at, inline=False)
            await ctx.send(embed=embed)
Bot.run(TOKEN)
