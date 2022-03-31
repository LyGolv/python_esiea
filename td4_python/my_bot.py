import discord

default_intents = discord.Intents.default()
default_intents.members = True
client = discord.Client(intents=default_intents)

@client.event # decorateur, car fonction spéciale
async def on_ready():
    print("le bot est prèt")

@client.event 
async def on_message(message):
    if message.content.lower() == "ping":
        await message.channel.send("pong")
    
    if message.content.startswith("!del"): 
        number = int(message.content.split()[1])
        messages = await message.channel.history(limit=number-1).flatten()        
        for message in messages:
            await message.delete()
        
@client.event
async def on_member_join(member):
    # on récupère le channel sur lequel on veut envoyer le message
    general_channel: discord.TextChannel = client.get_channel(958704849304834111) 
    await general_channel.send(content=f"Bienvenue sur le serveur @{member.display_name} !")
    

# lancer l'éxécution du bot
client.run("OTU4NzAxMDk5NDkyMTgwMDQw.YkRJ-Q.BihBHq6NqJpiaOMvivbXsBxVJ9U")