# discord_android

## bypass gatway identify


<p>The Gateway's IDENTIFY packet contains a properties field, containing $os, $browser and $device fields.
    Discord uses that information to know when your phone client and only your phone client has connected to Discord,
    from there they send the extended presence object.
    The exact field that is checked is the $browser field. If it's set to Discord Android on desktop,
    the mobile indicator is is triggered by the desktop client. If it's set to Discord Client on mobile,
    the mobile indicator is not triggered by the mobile client.
    The specific values for the $os, $browser, and $device fields are can change from time to time.<p>

<h4 style="text-align:center;">install this package </h4>

```
 pip install discord_android
 pip install git+github.com/himangshu147-git/discord_android
```

```py
import discord_android
import discord
from discord.ext import commands

discord_android

bot = commands.Bot(
    intents = discord.Intents.all(),
    command_prefix=">"
)
@bot.event
async def on_ready():
    print(f"logged in as {bot.user}")

bot.run("token")
```
