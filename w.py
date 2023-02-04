from jinja2 import Template
import traceback
from os import environ as ENV
from os import system
#from discord.utils import user_avatar

import sanic,datetime

system("pip install py-cord")
import discord
from discord.ext import commands
app = sanic.Sanic("loginbot")
bot = commands.AutoShardedBot(
  command_prefix="!",
  intents = discord.Intents(guilds=True)
)
keyword = ["__repl", "__"]
guild_id=1059724753012797510

@app.route("/status")


@app.route("/")
async def index(request):
 return sanic.response.redirect("")

@app.route("/1")
async def index(request):
  return await sanic.response.file("")

@bot.event
async def on_ready():
  await app.create_server(
    host='0.0.0.0',
    port=8080,
    return_asyncio_server=True,
    access_log=False
  )
  game = discord.Game(name="Opening The Gate!")
  await bot.change_presence(
    status=discord.Status.dnd, 
    activity=game
  )
  return


@bot.slash_command(name="verify")
async def verify(ctx):
  """Gives Access To kllDFN"""
  try:
    guild = bot.get_guild(1059724753012797510)
    role = guild.get_role(1059748388284944464)
    channel = bot.get_channel(1064470482520375407)
    member = guild.get_member(ctx.author.id)
    await member.add_roles(role)
    embed = discord.Embed(title="Welcome to kllDFN!", color=discord.Color.blue())
    embed.set_author(name=member.name)
    embed.set_footer(text=datetime.datetime.now().strftime("%m/%d/%Y %I:%M %p"))
    embed.description = "Thank you for joining our community!"
    await ctx.respond(embed=embed)
    await member.send(embed=embed)
    embed=discord.Embed(title="Welcome To kllDFN | The Final Version", description=f"<@{ctx.author.id}> Welcome To kllDFN", color=0x00ffe1)
    return await channel.send(embed=embed)
  except Exception as e:
    print(str(traceback.format_exc()))
    embed=discord.Embed(title="Error Detected", description=f"```py\n{traceback.format_exc()}\n{e}\n```")
    return await ctx.respond(embed=embed)


try:
  bot.run(ENV['TOKEN'])
except:
  system("kill 1")
