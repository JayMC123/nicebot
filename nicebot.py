import discord
from discord.ext import commands
import random

description = ''''This A Nice Bot Has More Commands Comming Devs Are Working On Me.
There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='^', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')  

@bot.command()
async def add(left : int, right : int):
    await bot.say(left + right)

@bot.command()
async def roll(dice : str):
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await bot.say('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await bot.say(result)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(*choices : str):
    await bot.say(random.choice(choices))

@bot.command()
async def repeat(times : int, content='repeating...'):
    for i in range(times):
        await bot.say(content)

@bot.command()
async def joined(member : discord.Member):
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))

@bot.group(pass_context=True)
async def cool(ctx):
 
    if ctx.invoked_subcommand is None:
        await bot.say('No, {0.subcommand_passed} is not cool'.format(ctx))

@cool.command(name='bot')
async def _bot():
    await bot.say('Yes, the bot is cool.')
    
@bot.command()
async def say (*args):
	output = ' '
	for word in args:
		output += word
		output += ' '
		await bot.say(output)
						
@bot.command()
async def cookie():
	await bot.say('Fine Here A Cookie :cookie:')
				
@bot.command(pass_context=True)
async def joined_at(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.message.author

    await bot.say('{0} joined at {0.joined_at}')
    
@bot.command()
async def ping():
	await bot.say('Pong! :white_check_mark: ```Nice Bot```')
	
@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member = None):
    try:
        if ctx.message.author.server_permissions.kick_members:
            if user is None:
                embed = discord.Embed(description=":x: **You forgot a user!**", color=(random.randint(0, 0xffffff)))
                await bot.say(embed=embed)
                return
            await bot.kick(user)
            embed = discord.Embed(description=f":white_check_mark: Sucessfuly kicked **{user}**!", color=(random.randint(0, 0xffffff)))
            await bot.say(embed=embed)
        else:
            embed = discord.Embed(description=":x: **You are missing KICK_MEMBERS permission.**", color=(random.randint(0, 0xffffff)))
            await client.say(embed=embed)
    except discord.Forbidden:
        embed = discord.Embed(description=":x: **I am missing permissions to use this command!**", color=(random.randint(0, 0xffffff)))
        
        await bot.say(embed=embed)
@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)
    
@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here's what I could find.", color=0x00ff00)
    embed.set_author(name="Desscription")
    embed.add_field(name=" Server ", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)
    
@bot.command(pass_context=True)
async def clear(ctx, amount=100):
	channel = ctx.message.channel
	messages = [ ]
	async for message in client.logs_from(channel, limit=int(amount) +1):
		message.append(message)
	await client.delete_messages(messages)
	await bot.say('Messages deleted')
	
@bot.command(pass_context=True)
async def suggest(ctx, *, msg: str):
    user_formatted = ctx.message.author.name + "#" + ctx.message.author.discriminator
    channel = discord.utils.get(ctx.message.server.channels, name="suggestions")
    embed = discord.Embed(title="New Suggestion", description=msg, color=0x149900)
    embed.set_author(name=user_formatted, icon_url=ctx.message.author.avatar_url)
    embed_message = await bot.send_message(channel, embed=embed)
    await bot.add_reaction(embed_message, '👍')
    await bot.add_reaction(embed_message, '👎')
    embed_2 = discord.Embed(title="Success", description="Your suggestion has been sent.", color=0x149900)
    await bot.send_message(ctx.message.channel, embed=embed_2)
    await bot.delete_message(ctx.message)
			
bot.run('NTE2MDcwMjkyNjI4NDM5MDYw.DtzAow.sPZxPQJcjJ8E4OMkDlfJSNySjXo')
