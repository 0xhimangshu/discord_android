# discord_android

## Description
A Python package that allows Discord bots to appear with mobile status by bypassing the Gateway Identify process.

## Features
- Shows mobile status for your Discord bot
- Simple integration with discord.py
- No additional configuration needed

## Installation
```bash
pip install discord_android
```

## Usage
```python
import discord_android
import discord
from discord.ext import commands

# Initialize mobile status
discord_android.init()

bot = commands.Bot(
    intents = discord.Intents.all(),
    command_prefix="!"
)

@bot.event
async def on_ready():
    print(f"logged in as {bot.user}")

bot.run("YOUR_BOT_TOKEN")
```

## Note
This package modifies the Discord gateway identification process to simulate a mobile client. Use responsibly and in accordance with Discord's Terms of Service.
