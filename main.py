import nextcord,random
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="blin ", description="Blin ass machine", intents=intents)

print("Loading Variables.")
try:
    jt_quotes = open("Jt quotes").read().split("\n")
    token = open("token").read()
    print("Loaded Successfully.")
except Exception as e:
    print("An error Occured:",e)
    exit
    
@bot.command()
async def test(ctx):
    await ctx.send("test")

@bot.command()
async def howtransami(ctx):
  transperc = random.randint(1,100)
  await ctx.send("You are " + str(transperc) + '% trans :transgender_flag: ')  

@bot.command()
async def JTquotes(ctx):
    quote = random.choice(jt_quotes)
    await ctx.send(quote+"\n       -JT")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id}), ready to blin!")

@bot.listen('on_message')
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

bot.run(token)
