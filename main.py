import nextcord,random
from nextcord.ext import commands
bot = commands.Bot(command_prefix="blin ", description="Blin ass machine", intents=nextcord.Intents.all())

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id}), ready to blin")
 
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "macky" in message.content or "ryan" in message.content:
        if random.random() > 0.7:
            await message.channel.send("is chad") 
            return
    if "keshav" in message.content:
        if random.random() > 0.7:
            await message.channel.send("JT")
            return 

@bot.command()
async def howtransami(ctx):
  transperc = random.randint(1,100)
  await ctx.send("You are " + str(transperc) + '% trans :transgender_flag: ')  

token = open("token").read()
bot.run(token)
