import nextcord
from nextcord.ext import commands
bot = commands.Bot(command_prefix="blin", description="Blin ass machine", intents=nextcord.Intents.all())

@bot.command()
async def howbigpp(ctx):
    await ctx.send("Beeg enough")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id}), ready to blin")

token = open("token").read()
bot.run(token)


