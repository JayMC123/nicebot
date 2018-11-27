import discord
import random
import time
import asyncio
from discord.ext import commands

TOKEN = 'NTE2MDcyNTY3MDk0NjQwNjQw.DtuWhw.Lky00QEk2A_VxGFkx354I2k8J14'
client = commands.Bot(command_prefix = '/')
client.remove_command('help')

@client.event
async def on_ready():
    serverCount = len(client.servers)
    await client.change_presence(game=discord.Game(name='{} servers | /help'.format(serverCount), type = 2, status=discord.Status.dnd))
    print('Hello')
                                                                   
@client.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(colour=discord.Colour.blue())
    embed.set_author(name="{}'s info".format(ctx.message.server.name))
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Server Owner", value=(ctx.message.server.owner))
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.add_field(name="Channels", value=len(ctx.message.server.channels))
    embed.add_field(name="Region", value=ctx.message.server.region, inline=True)
    embed.add_field(name="Server Created", value=ctx.message.server.created_at, inline=True)
    embed.add_field(name="Verification Level", value=ctx.message.server.verification_level, inline=True)
    embed.add_field(name="Is Server Large", value=ctx.message.server.large, inline=True)
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await client.say(embed=embed)
    
@client.command(pass_context=True)
async def flipcoin(ctx):
      await client.say(random.choice(['heads!', 'Tails!']))
	
@client.command(pass_context=True)
async def purge(ctx, amount=100):
	channel = ctx.message.channel
	messages = []
	async for message in client.logs_from(channel, limit=int(amount) +1):
		message.append(message)
	await client.delete_messages(messages)
	await client.say('Messages deleted.')

@client.command(pass_context=True)
async def help(ctx):
	author = ctx.message.author
	
	embed = discord.Embed(
	           colour = discord.Colour.blue()
	)
	
	embed.set_author(name='                                      Commands')
	embed.add_field(name='help', value='Shows this message', inline=True)
	embed.add_field(name='clear', value='Clears chat', inline=True)
	embed.add_field(name='kick', value='Kicks member', inline=True)
	embed.add_field(name='ban', value='Bans a user', inline=True)
	embed.add_field(name='flipcoin', value='flips a coin', inline=True)
	embed.add_field(name='serverinfo', value='shows server info', inline=True)
	embed.add_field(name='ping', value='shows (ms)', inline=True)
	embed.add_field(name='say', value='says anything you want', inline=True)
	
	await client.send_message(author, embed=embed)
	await client.say('Check your inventory.')
	
@client.command(pass_context=True)
async def kick(ctx, user: discord.Member = None):
    try:
        if ctx.message.author.server_permissions.kick_members:
            if user is None:
                embed = discord.Embed(description=":no_entry_sign: **You forgot a user!**", color=(random.randint(0, 0xffffff)))
                await client.say(embed=embed)
                return
            await client.kick(user)
            embed = discord.Embed(description=f":white_check_mark:  Sucessfuly kicked **{user}**!", color=(random.randint(0, 0xffffff)))
            await client.say(embed=embed)
        else:
            embed = discord.Embed(description=":error: **You are missing KICK_MEMBERS permission.**", color=(random.randint(0, 0xffffff)))
            await client.say(embed=embed)
    except discord.Forbidden:
        embed = discord.Embed(description=":error: **I am missing permissions to use this command!**", color=(random.randint(0, 0xffffff)))
        await client.say(embed=embed)    
        
@client.command(pass_context=True)
async def ban(ctx, user: discord.Member = None):
    try:
        if ctx.message.author.server_permissions.ban_members:
            if user is None:
                embed = discord.Embed(description=":no_entry_sign: **You forgot a user!**", color=(random.randint(0, 0xffffff)))
                await client.say(embed=embed)
                return
            await client.ban(user)
            embed = discord.Embed(description=f":check: Sucessfuly banned **{user}**!", color=(random.randint(0, 0xffffff)))
            await client.say(embed=embed)
        else:
            embed = discord.Embed(description=":error: **You are missing BAN_MEMBERS permission.**", color=(random.randint(0, 0xffffff)))
            await client.say(embed=embed)
    except discord.Forbidden:
        embed = discord.Embed(description=":error: **I am missing permissions to use this command!**", color=(random.randint(0, 0xffffff)))
        await client.say(embed=embed)    
        
@client.command(pass_context=True)
async def ping(ctx):
    t = await client.say('Pong!')
    ms = (t.timestamp-ctx.message.timestamp).total_seconds() * 1000
    await client.edit_message(t, new_content='Pong! Took: {}ms'.format(int(ms)))
    
@client.command(pass_context=True)
@commands.has_permissions(administrator=True, manage_messages=True)
async def clear(ctx, amount=100):
    """Clear the specified number of messages, default 100 messages."""
    channel = ctx.message.channel
    messages = []
    amount = int(amount) + 1
    async for message in cleintt.logs_from(channel, limit=amount):
        messages.append(message)
    await bot.delete_messages(messages)
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await client.send_message(ctx.message.channel, "You do not have permission to use that command.".format(ctx.message.author.mention))
        
@client.command(pass_context=True)
async def say(ctx,*msg):
	user_msg=ctx.message
	await client.say('{}'.format(' '.join(msg)))
	await asyncio.sleep()
	await client.delete_message(user_msg)
	
client.run(TOKEN)
