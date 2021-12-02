import discord
from discord.ext import commands
from config import token, prefix

bot = commands.Bot(command_prefix = prefix)
member_count = 0

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

# @bot.command(name='poll')
# @commands.has_role('dshodl')
# async def create_channel(ctx, channel_name='real-python'):
#     print(ctx.message.id)
#     guild = ctx.guild
#     existing_channel = discord.utils.get(guild.channels, name=channel_name)
#     if not existing_channel:
#         print(f'Creating a new channel: {channel_name}')
#         await guild.create_text_channel(channel_name)
#     else:
#         print("Channel exists")

# @bot.event
# async def on_command_error(ctx, error):
#     if isinstance(error, commands.errors.CheckFailure):
#         await ctx.send('You do not have the correct role for this command.')
#         print(ctx)
#     else:
#         await ctx.send('Error')

@bot.command(name='poll')
@commands.has_role('dshodl') # Name of token holders role
async def on_message(ctx, *, message='offer'):
    #if the spotify command is triggered
        #fetch from the API
        channel = bot.get_channel(910898541742915634) #private channel id 
        global poll_message
        poll_message = message
        offer_message = await channel.send(message)
        await offer_message.add_reaction("👍")
        await offer_message.add_reaction("👎")
        global member_count
        member_count = ctx.guild.member_count


@bot.event
async def on_reaction_add(reaction, user):
    print(member_count)
    if user != bot.user:
        if str(reaction.emoji) == "👍":
            likes = reaction.message.reactions[0].count
            if member_count/2 <= likes:
                channel = bot.get_channel(910861765368233996) #open channel id
                await channel.send(poll_message)
        if str(reaction.emoji) == "👎":
            dislikes = reaction.message.reactions[1].count
            print(dislikes)

bot.run(token)