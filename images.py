import urllib.request
from os import system

system("pip install py-cord")
import discord
from asyncio import sleep
from discord.ext import commands
from discord import option
from PIL import Image, ImageDraw, ImageFont
from sanic import Sanic
from sanic.response import file, text,json,redirect
from os import path
from os import listdir
from os import environ as ENV

app = Sanic("images")
url = f"https://{ENV['REPL_ID']}.id.repl.co"
bot = commands.Bot(
  description="klldFN Images",
  command_prefix=[
    "!",
  ],
)

@app.route("/")
async def index(request):
  return redirect("")







@app.route("/images/<id>/icon.png")
async def images(request, id):
  try:
    id = id.upper()
    if path.exists(f"images/{id}"):
      return await file(f"images/{id}.png")
    else:
      image_url = f"https://fortnite-api.com/images/cosmetics/br/{id}/icon.png"
      with urllib.request.urlopen(image_url) as url:
          image_data = url.read()
      with open("temp.png", "wb") as f:
          f.write(image_data)
      image = Image.open("temp.png")
      draw = ImageDraw.Draw(image)
      font = ImageFont.truetype("Provicali.otf", 62)
      text_width, text_height = draw.textsize("KllDFN", font=font)
      x = (image.width - text_width) // 2
      y = (image.height - text_height) // 2
      try:
        draw.text((x, y), "KllDFN", font=font, fill=(256, 64))
      except:
        draw.text((x, y), "KllDFN", font=font, fill=(0, 0, 0, 64))
      image.save(f"images/{id}.png")
      return await file(f"images/{id}.png")
  except Exception as e:
    return text(str(e))

async def statusLoop():
  while True:
    images = listdir("images")
    game = discord.Activity(
      type=discord.ActivityType.watching, 
      name=f"{len(images)} Images"
    )
    await bot.change_presence(
      status=discord.Status.dnd, 
      activity=game
    )
    await sleep(300)

    
@app.route("/images/<id>/featured.png")
async def images(request, id):
  try:
    id = id.upper()
    if path.exists(f"images/{id}"):
      return await file(f"images/{id}.png")
    else:
      image_url = f"https://fortnite-api.com/images/cosmetics/br/{id}/featured.png"
      with urllib.request.urlopen(image_url) as url:
          image_data = url.read()
      with open("temp.png", "wb") as f:
          f.write(image_data)
      image = Image.open("temp.png")
      draw = ImageDraw.Draw(image)
      font = ImageFont.truetype("Provicali.otf", 62)
      text_width, text_height = draw.textsize("klld", font=font)
      x = (image.width - text_width) // 2
      y = (image.height - text_height) // 2
      try:
        draw.text((x, y), "klld", font=font, fill=(256, 64))
      except:
        draw.text((x, y), "klld", font=font, fill=(0, 0, 0, 64))
      image.save(f"images/{id}.png")
      return await file(f"images/{id}.png")
  except Exception as e:
    return text(str(e))
async def statusLoop():
  while True:
    images = listdir("images")
    game = discord.Activity(
      type=discord.ActivityType.watching, 
      name=f"{len(images)} Images"
    )
    await bot.change_presence(
      status=discord.Status.dnd, 
      activity=game
    )
    await sleep(300)
  
@app.route("/images/<id>/showcase.png")
async def images(request, id):
  try:
    id = id.upper()
    if path.exists(f"images/{id}"):
      return await file(f"images/{id}.png")
    else:
      image_url = f"https://fortnite-api.com/images/playlists/{id}/showcase.png"
      with urllib.request.urlopen(image_url) as url:
          image_data = url.read()
      with open("temp.png", "wb") as f:
          f.write(image_data)
      image = Image.open("temp.png")
      draw = ImageDraw.Draw(image)
      font = ImageFont.truetype("Provicali.otf", 62)
      text_width, text_height = draw.textsize("klld", font=font)
      x = (image.width - text_width) // 2
      y = (image.height - text_height) // 2
      try:
        draw.text((x, y), "klld", font=font, fill=(256, 64))
      except:
        draw.text((x, y), "klld", font=font, fill=(0, 0, 0, 64))
      image.save(f"images/{id}.png")
      return await file(f"images/{id}.png")
  except Exception as e:
     return text(str(e))
async def statusLoop():
  while True:
    images = listdir("images")
    game = discord.Activity(
      type=discord.ActivityType.watching, 
      name=f"{len(images)} Images"
    )
    await bot.change_presence(
      status=discord.Status.dnd, 
      activity=game
    )
    await sleep(300)    

@bot.event
async def on_ready():
  print("Launching Server")
  await app.create_server(
    host="0.0.0.0",
    port=443,
    access_log=False,
    return_asyncio_server=True
  )
  bot.loop.create_task(statusLoop())
  return

@bot.slash_command(name="generate")
@option(
    "id",
    description="An ID For a Valid Fortnite Cosmetic",
    required=True
)
async def gen(ctx: discord.ApplicationContext, id:str):
  embed=discord.Embed(title=f"{id}", url=f"{url}/images/{id}/icon.png", description=f"{id} Image Generated")
  embed.set_author(name="Image Generated", url=f"{url}/images/{id}/icon.png", icon_url=f"{url}/images/{id}/icon.png")
  embed.set_thumbnail(url=f"{url}/images/{id}/icon.png")
  embed.set_image(url=f"{url}/images/{id}/icon.png")
  await ctx.respond(embed=embed)
  
  @bot.slash_command(name="playlists")
@option(
    "id",
    description="An ID For a Valid Fortnite Cosmetic",
    required=True
)
async def gen(ctx: discord.ApplicationContext, id:str):
  embed=discord.Embed(title=f"{id}", url=f"{url}/images/playlists/{id}/showcase.png", description=f"{id} Image Generated")
  embed.set_author(name="Image Generated", url=f"{url}/images/playlists/{id}/showcase.png", icon_url=f"{url}/images/playlists/{id}/showcase.png")
  embed.set_thumbnail(url=f"{url}/images/playlists/{id}/showcase.png")
  embed.set_image(url=f"{url}/images/playlists/{id}/showcase.png")
  await ctx.respond(embed=embed)


bot.run(ENV['token'])
