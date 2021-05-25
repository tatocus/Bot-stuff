import os
import discord
from pathlib import Path
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
load_dotenv(verbose=True)
env_path = Path("./") / ".env"
load_dotenv(dotenv_path=env_path)

client = commands.Bot(command_prefix="!")


@client.event
async def on_ready():
    print("Bot logged in!")


@client.command(name="ping")
async def ping(ctx):
    await ctx.send("Pong")

client.run(os.getenv("TOKEN"))
