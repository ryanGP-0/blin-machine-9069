import nextcord,random
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="b.", description="Blin ass machine", intents=intents)

print("Loading Variables.")
try:
    jt_quotes = open("resources/Jt quotes").read().split("\n")
    token = open("resources/token").read()
    print("Loaded Successfully.")
except Exception as e:
    print("An error Occured:",e)
    exit

@bot.command()
async def howtransami(ctx):
  transperc = random.randint(1,100)
  await ctx.send("You are " + str(transperc) + '% trans :transgender_flag:')  

@bot.command()
async def howgaeami(ctx):
  gaeperc = random.randint(1,100)
  await ctx.send("You are " + str(gaeperc) + '% gae :rainbow_flag:') 

@bot.command()
async def howthotami(ctx):
  thotperc = random.randint(1,100)
  await ctx.send("You are " + str(thotperc) + '% thot :peach:') 

@bot.command()
async def howsmortami(ctx):
  smort = random.randint(1,100)
  await ctx.send("You are " + str(smort) + '% smort :brain:') 
    
@bot.command()
async def amiblin(ctx):
    await ctx.send("you are already the biggest blin for using this bot :heart:")

@bot.command()
async def jtquotes(ctx):
    quote = random.choice(jt_quotes)
    await ctx.send("\""+quote+"\"\n\n -JT")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id}), ready to blin!")

@bot.listen('on_message')
async def on_message(message):
    if message.author == bot.user:
        return
    if "macky" == message.content or "ryan" in message.content:
        if random.random() > 0.7:
            await message.channel.send("is chad") 
            return
    if "keshav" == message.content:
        if random.random() > 0.7:
            await message.channel.send("JT")
            return
    if "nice joke" in message.content:
            await message.channel.send("https://media.discordapp.net/attachments/825055109502730332/1026062254908637245/nicejoke.png")
            return
     if "blin" in message.content:
        await message.channel.send("yes, yes, the blin religion must grow, it must spread")
        return

@bot.command()
async def nudes(ctx):
    await ctx.send(file=nextcord.File("resources/nudes.mp4"))

@bot.command()
async def toss(ctx):
    await ctx.send('flipping a coin :coin:')
    coin = random.randint(0,1)
    if coin == 0:
        await ctx.send("It landed on `heads`")
    if coin == 1:
        await ctx.send('It landed on `tails`')

@bot.command()
async def ppsize(ctx):
    rand1 = random.choice([True, False])
    rand2 = random.randint(1,10)
    if rand1 == True:
        rand2 = int(rand2/2)
        ppsize = "=" * rand2
    else:
        ppsize = "=" * rand2
    if rand2 <= 5:
        comment = "smol pp"
    elif rand2 > 5:
        comment = "beeg pp"
    await ctx.send('your pp size is ' + '`8'+ ppsize + 'D`' + f'\n{comment}')
    
@bot.command()
async def rr(ctx):
  await ctx.send('You have started Russian Roulette')
  bullets = random.randint(1,6)
  if bullets == 6 or bullets == 3:
    await ctx.send("Bang! You died, Try again")
  else:
    await ctx.send('You survived smol pp boi')

bot.run(token)
