import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('ID')

client = discord.Client()
client = commands.Bot(command_prefix = '!')

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
  await member.kick(reason=reason)

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
  await member.ban(reason=reason)

@client.command()
async def unban(ctx, *, member):
  banned_users = await ctx.guild.bans()
  member_name, member_discriminator = member.split('#')
  for ban_entry in banned_users:
    user = ban_entry.user
  if(user.name, user.discriminator) == (member_name, member_discriminator):
    await ctx.guild.unban(user)
    await ctx.send(f'Unbanned {user.mention}')
    return

client.run(TOKEN)
