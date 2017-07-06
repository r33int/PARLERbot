import discord
import random
client = discord.Client()
name = "Luclu7","leonekmi","Theo","LnBot","Lozzydud","Nyo","Donald Trump","ta maman","MOI"
ip = "127.0.0.1","8.8.8.8","196.168.1.1","255.255.255.0","$ipv6"
@client.event

async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content == 'cc':
        msg = discord.Embed(title='sésé', colour=0x53CD80)
        await client.add_reaction(message, '?')
        await client.send_message(message.channel, embed=msg)
    if message.content == 'pdva':
        msg = discord.Embed(title='#PDVA2022', description='Votez pour nous !', url='https://twitter.com/PDVA_officiel', colour=0x93BD43)
        await client.add_reaction(message, '?')
        msg.set_author(name='@PDVA_officiel', icon_url="https://pbs.twimg.com/profile_images/851500993086967816/1m-V3R9Y.jpg")
        await client.send_message(message.channel, embed=msg)
    if message.content == 'PDVA':
        msg = discord.Embed(title='#PDVA2022', description='Votez pour nous !', url='https://twitter.com/PDVA_officiel', colour=0x93BD43)
        await client.add_reaction(message, '?')
        msg.set_author(name='@PDVA_officiel', icon_url="https://pbs.twimg.com/profile_images/851500993086967816/1m-V3R9Y.jpg")
        await client.send_message(message.channel, embed=msg)
    if message.content == "ckoil'ip":
        i = random.choice(ip)
        print (i)
        msg = discord.Embed(title="Ckoil'ip", description=i + ' !',  colour=0x0078ff)
        await client.add_reaction(message, '?')
        await client.send_message(message.channel, embed=msg)
    if message.content == "avant 2017":
        msg = discord.Embed(title="ON EST DÉJÀ EN 2017", description='Imbécile',  colour=0xff0000)
        await client.add_reaction(message, '?')
        await client.send_message(message.channel, embed=msg)
    if message.content == "C ki la taup":
        n = random.choice(name)
        print (n)
        msg = discord.Embed(title="C ki la taup", description="C'EST "+ n +" LA TAUPE", colour=0x1571B0)
        await client.add_reaction(message, '??')
        await client.send_message(message.channel, embed=msg)
    if message.content == "#KebabEuropeen":
        msg = discord.Embed(title="@benoithamon", description="J'ai craqué. #faim #ZéroRégime", url='https://twitter.com/benoithamon/status/880510699855892480', colour=0x192249)
        msg.set_image(url="https://pbs.twimg.com/media/DDgz0HeXsAAn6C9.jpg")
        msg.set_author(name='Benoît Hamon',icon_url='https://i.imgur.com/AX2yZom.png')
        await client.add_reaction(message, '?')
        await client.send_message(message.channel, embed=msg)
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

#Put your token here
client.run('TOKEN')
