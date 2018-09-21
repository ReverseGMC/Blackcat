import discord

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('%hello'):
        msg = 'Greetings {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('%videogames'):
        await client.send_message(message.channel, "https://www.mcleodgaming.com/games/ssf2")
        
@client.event       
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('NDQ5MzA2OTU5ODYzMDg3MTA0.DoU4Qw.oq7ljmrz17k9n0yimUy8wGAZB4o')




