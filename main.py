import os
import discord
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
load_dotenv(verbose=True)
env_path = Path("./") / ".env"
load_dotenv(dotenv_path=env_path)

client = discord.Client(command_prefix="!")

@client.event
async def on_ready():
    print("Bot logged in!")

client.run(os.getenv("TOKEN"))
