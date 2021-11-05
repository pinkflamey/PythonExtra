import discord
import random

client = discord.Client()

@client.event
async def on_ready():
    # De bot kan op veel verschillende servers draaien. Met deze regel code pak je de eerste server die deze bot heeft. Als jouw bot maar 1 server heeft is het makkelijk.
    guild = client.guilds[0]
    # De naam van de server printen we gelijk uit.
    print(guild.name, "is the name of the server")

    # We printen de naam van de bot user uit.
    print(client.user, "has connected to the client")

    channel = guild.text_channels[0]
    print(channel.name, "is the name of the channel")
    # await channel.send("I'm online!")

@client.event
async def on_message(message):

    if message.author.bot == False:
        if str(message.content).lower() == "je moeder":
            m = random.randrange(1, 7)
            if m == 1:
                await message.channel.send("...is lelijk, @" + str(message.author))
            elif m == 2:
                await message.channel.send("...is een plopkoek, @" + str(message.author))
            elif m == 3:
                await message.channel.send("...is fucking lekker, @" + str(message.author))
            elif m == 4:
                await message.channel.send("...heb ik gisteravond genaaid, @" + str(message.author))
            elif m == 5:
                await message.channel.send("...is een 2/10, @" + str(message.author))
            elif m == 6:
                await message.channel.send("...is gewoon fucking triest, @" + str(message.author))



client.run("")