
import os

os.system("pip install sanic==21.6.2")
os.system("pip install py-cord==2.0.0rc1")
os.system('clear')

import discord
import aiohttp  
import requests
from discord.ext import commands
import fortnitepy
from fortnitepy.ext import commands as co
import sanic
from fortnitepy.ext import commands as fortnite
import crayons
import uuid
import json
from functools import partial
import FortniteAPIAsync
import random
from discord.ui import Button, View, Modal, InputText
import asyncio
from PIL import Image, ImageDraw, ImageFont
import time
from datetime import datetime
import fortnitenews

FortniteAPIAsync = FortniteAPIAsync.APIClient()
bots = []
onlinebots = {}
uuids = {}
indexes = {}

"""defining stuff like a bozo"""



class data:
    def __init__(self):
        self.commands_today = 0
        self.day = datetime.now().timetuple().tm_yday
        self.uptime = 0





app = sanic.Sanic("klldFNLobbyBot")
intents = discord.Intents.all()
botdata = data()
discord_bot = discord.Bot(command_prefix="!")
set = discord_bot.create_group("set", "set stuff")
party = discord_bot.create_group("party", "party stuff")
outfit = discord_bot.create_group("outfit", "outfit stuff")
footertext = "Thanks for using klld LobbyBot | https://klld.42web.io/ â¤" 
color = 0x5865F2
startTime = time.time()
total_seconds = 0
minutes = 0
hours = 0

from jinja2 import Environment
from jinja2 import FileSystemLoader

def render_template(file, **kwargs) -> str:
  """Use jinja2 to render a template"""
  env = Environment(
    loader=FileSystemLoader(
      './templates', 
      encoding='utf8'
    )
  )
  template = env.get_template(file)
  return sanic.response.html(template.render(**kwargs))

@app.route('/cookies')
async def cookies(request):
  cookies = request.cookies
  print(str(request.cookies))

@app.route('/')
async def m(request):
  return sanic.response.redirect("https://www.klld.tk/")
  #return render_template(
    #file="dashboard.html",
    #user="PlaceHolder",
    #skin="Ikonik",
    #back="Galactic Disc",
    #axe="Raider's Revenge",
    #emote="Scenario",
    #banner="Brseason01",
    #level="150",
    #crown="123",
    #friends="25",
    #party="1 / 16",
  #)

async def get_name(id):
  async with aiohttp.ClientSession() as session:
    async with session.get(
      f"https://fortnite-api.com/v2/cosmetics/br/{id}"
    ) as r:
      response = await r.json()
  return response['data']['name']


@app.route('/set/')
async def setend(request):
  types = {
    "skin": "AthenaCharacter",
    "emote": "AthenaDance",
    "pickaxe": "AthenaPickaxe",
    "backpack": "AthenaBackpack"
  }
  type = request.args.get('type')
  name = request.args.get('name')
  id = request.args.get('id')
  client = uuids[id]
  async with aiohttp.ClientSession() as session:
    async with session.get(
      f"https://fortnite-api.com/v2/cosmetics/br/search/all?name={name}&backendtype={types.get(type)}"
    ) as r:
      data = await r.json()
  itemid = data['data'][0]['id']
  await client.party.me.set_outfit(asset=itemid)
  return sanic.response.text(itemid)
  


@app.route("/dashfiles")
async def render_dash(request):
  if request.args.get("path"):
    path = request.args.get("path")
    try:
      return await sanic.response.file(f"images/{path}")
    except FileNotFoundError:
      return sanic.response.json({"error": "File Not Found"})
  return sanic.response.redirect("/")

  

@app.route('/view/')
async def dash(request):
  id = request.args.get('id')
  try:
    client = uuids[id]
  except KeyError:
    return sanic.response.redirect("http://klld.42web.io/")
  if client:
    async with aiohttp.ClientSession() as session:
      async with session.get("https://fortnite-api.com/v1/banners") as r:
        banners = await r.json()
        banners = banners['data']
      for banner in banners:
        if banner['id'].lower() == client.party.me.banner[0].lower():
          b=banner.get("devName")
        else:
          continue
    meta = client.party.me.meta
    data = (meta.get_prop('Default:AthenaCosmeticLoadout_j'))['AthenaCosmeticLoadout']
    try:
      crown = data['cosmeticStats'][0]['statValue']
    except:
      crown = "0"
    return render_template(
      file="dashboard.html",
      user=client.user.display_name,
      skin=await get_name(client.party.me.outfit),
      back=await get_name(client.party.me.backpack),
      axe=await get_name(client.party.me.pickaxe),
      emote=client.party.me.emote,
      uuid = str(id),
      
      skin_id=client.party.me.outfit,
      back_id=client.party.me.backpack,
      axe_id=client.party.me.pickaxe,
      emote_id=client.party.me.emote,

      banner_id=client.party.me.banner[0],
      banner = b,
      level=f"{client.party.me.banner[2]}",
      crown=str(crown),
      friends=f"{len(client.friends)}",
      party=f"{client.party.member_count} / 16",
  )
  else:
    return sanic.response.text("You dont have a bot")

@app.exception(sanic.exceptions.NotFound)
async def ignore_404s(request, exception):
  return await sanic.response.file("templates/404.html", status=404)

@app.exception(sanic.exceptions.ServerError)
async def ignore_500s(request, exception):
  return render_template(
    file="500.html"
  )

@discord_bot.event
async def on_ready():
  await app.create_server(host="0.0.0.0",port=443,return_asyncio_server=True, access_log=False)
  print(f'Logged In As {discord_bot.user}')


cid = 'CID_028_Athena_Commando_F'
eid = 'EID_AfroHouse'
pickaxe_id = 'Pickaxe_LockJaw' 
status = 'Battle Royale Lobby - 1 / 16'
banner = "BRSeason01"
banner_color = "defaultcolor15"
platform = 'XSX'
acceptFriend = True
acceptInvite = True
joinMessage = 'test'

class BotChoiceDropdown(discord.ui.Select):
    def __init__(self, bot_: discord.Bot):
        self.bot = bot_
        options = [
            discord.SelectOption(
              label="Pre-Made Bot", 
              description="Start a klldFN-Made Bot", 
              emoji="<:boogie:965618391547260958>"),
            discord.SelectOption(
              label="Custom Bot", 
              description="Make a Bot with a custom name", 
              emoji="<:boogie:965618391547260958>"),
            discord.SelectOption(
              label="Saved Bot", 
              description="Use a previosly saved Bot", 
              emoji="<:boogie:965618391547260958>"),
        ]
        super().__init__(
            placeholder="What type of LobbyBot would you like to start?",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, interaction: discord.Interaction):
      label = self.values[0]
      if label == "Pre-Made Bot":
        embed=discord.Embed(title="Starting Your Bot <a:5564_Loading_Color:987094303027384370>", color=color)
        embed.set_footer(text=footertext)
        msg = await interaction.response.edit_message(
          embed=embed, 
          view = None
        )
        auths = await get_auths()
        print(auths)
        acc_id = auths[0]
        dev_id = auths[1]
        secret = auths[2]
        index = auths[3]
        global fortnite_client
        fortnite_client = new_client(
          user=interaction.user, 
          device_id=dev_id, 
          account_id=acc_id, 
          secret=secret
        )
        global task
        task = [
          discord_bot.loop.create_task(
            fortnite_client.start()
          ),
          discord_bot.loop.create_task(
            fortnite_client.wait_until_ready()
          )
        ]
        done, _ = await asyncio.wait(
          task, 
          return_when=asyncio.FIRST_COMPLETED
        )
        if task[1] not in done:
          await interaction.user.send('error starting bot')
        else:
          bots.append(fortnite_client)
          onlinebots.update({interaction.user.id:fortnite_client})
          uid = str(uuid.uuid4())
          uuids.update({interaction.user.id:uid})
          uuids.update({uid:fortnite_client})
          indexes.update({interaction.user.id:index})
          embed=discord.Embed(title=fortnite_client.user.display_name, color=color)
          embed.add_field(name=f"Battle Royale Lobby - {fortnite_client.party.member_count} / 16", value=f"â €", inline=False)
          embed.add_field(name=f"Join our discord server", value="[klld](https://discord.gg/)")
          embed.add_field(name="Friends:", value=f"{len(fortnite_client.friends)}")
          embed.add_field(name="LobbyBot Dashboard", value=f"[View LobbyBot Dashboard](38d30774-bd4f-4561-b27a-6a7fd744d355.id.repl.co/view?id={uid})")
          embed.set_thumbnail(url=f"https://1dbd854d-eda6-44b7-b0b1-aedad1b34a69.id.repl.co/images/CID_028_Athena_Commando_F/icon.png")
          embed.set_footer(text=footertext)
                
          await interaction.edit_original_message(embed=embed)
          await asyncio.sleep(1800) 
          await fortnite_client.close()
          
          for tasks in task:
            tasks.cancel()
          del onlinebots[interaction.user.id] 
          del uuids[uid]
          del uuids[interaction.user.id]
          del indexes[interaction.user.id]
          with open("auths.json") as f:
            old_auths=json.load(f)
          old_auths['auths'][index]['running'] = False
          with open(f'auths.json', 'w') as ffs:
            json.dump(old_auths, ffs, indent=2)
          embedstop = discord.Embed(title="Hosting Time Expired!", description = "To start a new bot type /start", color=color)
          embedstop.set_footer(text=footertext)
          await interaction.user.send(embed=embedstop)
                
          
          return
      if label == "Custom Bot":
        embed=discord.Embed(title="Create a Lobbybot", color=color)
        embed.add_field(name="step #1", value="Click the **Epic Games** And login with an **ALT**")
        embed.add_field(name="step #2", value="Head over to **Authorization Code** and copy the 32 digit code")
        embed.add_field(name="step #3", value="click the **Submit Code** button and paste the code, then click confirm")
        view = loginView()
        epic = discord.ui.Button(label='Epic Games', style=discord.ButtonStyle.gray, url='https://epicgames.com')
        auth = discord.ui.Button(label='Authorization Code', style=discord.ButtonStyle.gray, url='http://gg.gg/codeauth')
        view.add_item(epic)
        view.add_item(auth)
        embed.set_image(url="https://media.discordapp.net/attachments/836517393266245632/837230076118302730/image0.png")
        await interaction.response.edit_message(embed=embed, view=view)
        
      


class BotChoiceView(discord.ui.View):
    def __init__(self, bot_: discord.Bot):
        self.bot = bot_
        super().__init__()

        self.add_item(BotChoiceDropdown(self.bot))

@discord_bot.slash_command()
async def choose(ctx):
  client = onlinebots.get(ctx.author.id, None)
  if client:
    embed = already_bot()
    return await ctx.respond(embed=embed)
  embed=discord.Embed(title="Please select the type of Lobbybot you would like to start <a:5564_Loading_Color:987094303027384370>", color=color)
  embed.set_footer(text=footertext)
  return await ctx.respond(embed=embed, view = BotChoiceView(discord_bot))
  


def newbot(user):
  client = fortnitepy.Client(
    auth=fortnitepy.AdvancedAuth(),
    status=status,
    platform=fortnitepy.Platform('XSX'),
  )
  server = None
  print(f"[+] Client Being Started By: {user}")

  def store_device_auth_details(email, details):
    existing = get_device_auth_details()
    existing[email] = details

    with open('device_auths.json', 'w') as fp:
      json.dump(existing, fp)


  def get_device_auth_details():
    with open('device_auths.json') as f:
      return json.load(f)
     
     
    
  @client.event
  async def event_ready() -> None:
    global server
    await edit_and_keep_client_member()
    await set_crowns()
    print(crayons.green(f'[+] Client ready as {client.user.display_name} | {user.name}#{user.discriminator}.'))






  async def set_crowns():
    meta = client.party.me.meta
    data = (meta.get_prop('Default:AthenaCosmeticLoadout_j'))['AthenaCosmeticLoadout']
    try:
      data['cosmeticStats'][1]['statValue'] = 1942
    except KeyError:
      data['cosmeticStats'] = [
                      {
                          "statName": "TotalVictoryCrowns",
                          "statValue": 1942
                      },
                      {
                          "statName": "TotalRoyalRoyales",
                          "statValue": 1942
                      },
                      {
                          "statName": "HasCrown",
                          "statValue": 0
                      }
                  ]
      final = {'AthenaCosmeticLoadout': data}
      key = 'Default:AthenaCosmeticLoadout_j'
      prop = {key: meta.set_prop(key, final)}
      await client.party.me.patch(updated=prop)


  async def edit_and_keep_client_member():
    member = client.party.me
    try:
      await member.edit_and_keep(
      partial(member.set_outfit, asset='CID_619_Athena_Commando_F_TechLlama'),
      partial(member.set_banner, icon="brseason01", color="defaultcolor16", season_level=150),
      partial(member.set_backpack, asset='BID_138_Celestial'),
      partial(member.set_pickaxe, asset='Pickaxe_ID_376_FNCS'),
      )
    except:
      print(crayons.red('[KLLD] Error'))
      return

  @client.event
  async def event_friend_request(request):
    invite = request
    await create_image(type="friend", username=invite.display_name)
    view = View()
    accept = Button(label="Accept", style=discord.ButtonStyle.green, emoji="<a:b_yes:606562687446679553>")
    
    decline = Button(label="Decline", style=discord.ButtonStyle.red, emoji="<a:X_Box:871238400731140156>")

    async def accept_callback(interaction):
      await interaction.response.defer()
      await invite.accept()
      await create_image(type="frienda", username=invite.display_name)
      embed = discord.Embed(title=f"Friend Request from {invite.display_name} Accepted", color=color)
      embed.set_footer(text=footertext)
      embed.set_image(url="attachment://image.png")
      await msg.edit(file = discord.File(f"cache/{invite.display_name}.jpg", filename="image.png"), embed=embed, view=None)
      
    async def decline_callback(interaction):
      await interaction.response.defer()
      await invite.decline()
      await create_image(type="friendd", username=invite.display_name)
      embed = discord.Embed(title=f"Friend Request from {invite.display_name} Declined", color=color)
      embed.set_footer(text=footertext)
      embed.set_image(url="attachment://image.png")
      await msg.edit(file = discord.File(f"cache/{invite.display_name}.jpg", filename="image.png"), embed=embed, view=None)

    accept.callback = accept_callback
    decline.callback = decline_callback

    view.add_item(accept)
    view.add_item(decline)
    embed = discord.Embed(title=f"Friend Request from {invite.display_name}", color=color)
    embed.set_footer(text=footertext)
    embed.set_image(url="attachment://image.png")
    msg = await user.send(file = discord.File(f"cache/{invite.display_name}.jpg", filename="image.png"), embed=embed, view=view)
    
  @client.event
  async def event_party_invite(invite):
    await create_image(type="invite", username=invite.sender.display_name)
    view = View()
    accept = Button(label="Accept", style=discord.ButtonStyle.green, emoji="<a:b_yes:606562687446679553>")
    
    decline = Button(label="Decline", style=discord.ButtonStyle.red, emoji="<a:X_Box:871238400731140156>")

    async def accept_callback(interaction):
      await interaction.response.defer()
      await invite.accept()
      await create_image(type="invitea", username=invite.sender.display_name)
      embed = discord.Embed(title=f"Invite from {invite.sender.display_name} Accepted", color=color)
      embed.set_footer(text=footertext)
      embed.set_image(url="attachment://image.png")
      await msg.edit(file = discord.File(f"cache/{invite.sender.display_name}.jpg", filename="image.png"), embed=embed, view=None)
      
    async def decline_callback(interaction):
      await interaction.response.defer()
      await invite.decline()
      await create_image(type="invited", username=invite.sender.display_name)
      embed = discord.Embed(title=f"Invite from {invite.sender.display_name} Declined", color=color)
      embed.set_footer(text=footertext)
      embed.set_image(url="attachment://image.png")
      await msg.edit(file = discord.File(f"cache/{invite.sender.display_name}.jpg", filename="image.png"), embed=embed, view=None)

    accept.callback = accept_callback
    decline.callback = decline_callback

    view.add_item(accept)
    view.add_item(decline)
    embed = discord.Embed(title=f"Party invite from {invite.sender.display_name}", color=color)
    embed.set_footer(text=footertext)
    embed.set_image(url="attachment://image.png")
    msg = await user.send(file = discord.File(f"cache/{invite.sender.display_name}.jpg", filename="image.png"), embed=embed, view=view)
    #try:
      #await invite.accept()
    #except:
      #print(crayons.red("[NOTEASONFN] Error Joining A Invite"))



  @client.event
  async def event_party_member_join(member: fortnitepy.PartyMember) -> None:
    await set_crowns()
    await member.party.send(f"Hey {member.display_name}\nThanks for using KllDFN LobbyBot!\nDiscord: discord.gg/")
    await asyncio.sleep(1)
    await client.party.me.set_emote(asset='EID_KPopDance03')





def clear_auth_use():
  print("[+] Resetting...")
  with open("auths.json") as f:
    auths=json.load(f)
  for index, auth in enumerate(auths['auths']):
    if auth['running'] == True:
      auths['auths'][index]['running'] = False
        
      with open(f'auths.json', 'w') as ffs:
        json.dump(auths, ffs, indent=2)
  print("[+] Finished Resetting!")

clear_auth_use()

def new_client(user, device_id, account_id, secret):
    #client definition    
    client = fortnite.Bot(
			command_prefix="!",
      platform=fortnitepy.Platform('XSX'),
			auth = fortnitepy.DeviceAuth(
				device_id=device_id,
				account_id=account_id,
				secret=secret
			)
		)
    server = None
    print("Client Being Started")
    #prints when client is being started (you can change todo anything)

    def store_device_auth_details(email, details):
        existing = get_device_auth_details()
        existing[email] = details

        with open('device_auths.json', 'w') as fp:
            json.dump(existing, fp)


    def get_device_auth_details():
        with open('device_auths.json') as f:
            return json.load(f)
     
     
    
    @client.event
    async def event_ready() -> None:
        global server
        #global server is to start sanic server on ready
        await edit_and_keep_client_member()
        print(f'Client ready as {client.user.display_name}.')
        for friend in client.friends:
          await friend.remove()

    async def set_crowns():
      meta = client.party.me.meta
      data = (meta.get_prop('Default:AthenaCosmeticLoadout_j'))['AthenaCosmeticLoadout']
      try:
        data['cosmeticStats'][1]['statValue'] = 1942
      except KeyError:
        data['cosmeticStats'] = [
                        {
                            "statName": "TotalVictoryCrowns",
                            "statValue": 1942
                        },
                        {
                            "statName": "TotalRoyalRoyales",
                            "statValue": 1942
                        },
                        {
                            "statName": "HasCrown",
                            "statValue": 0
                        }
                    ]
        final = {'AthenaCosmeticLoadout': data}
        key = 'Default:AthenaCosmeticLoadout_j'
        prop = {key: meta.set_prop(key, final)}
        await client.party.me.patch(updated=prop)
  
  
    async def edit_and_keep_client_member():
      member = client.party.me
      try:
        await member.edit_and_keep(
        partial(member.set_outfit, asset='CID_028_Athena_Commando_F'),
        partial(member.set_banner, icon="brseason01", color="defaultcolor16", season_level=999),
        partial(member.set_backpack, asset='BID_138_Celestial'),
        partial(member.set_pickaxe, asset='Pickaxe_ID_376_FNCS'),
        )
      except:
        print(crayons.red('[KLLD] Error'))
        return
  
    @client.event
    async def event_friend_request(request):
      invite = request
      await create_image(type="friend", username=invite.display_name)
      view = View()
      accept = Button(label="Accept", style=discord.ButtonStyle.green, emoji="<a:b_yes:606562687446679553>")
      
      decline = Button(label="Decline", style=discord.ButtonStyle.red, emoji="<a:X_Box:871238400731140156>")
  
      async def accept_callback(interaction):
        await interaction.response.defer()
        await invite.accept()
        await create_image(type="frienda", username=invite.display_name)
        embed = discord.Embed(title=f"Friend Request from {invite.display_name} Accepted", color=color)
        embed.set_footer(text=footertext)
        embed.set_image(url="attachment://image.png")
        await msg.edit(file = discord.File(f"cache/{invite.display_name}.jpg", filename="image.png"), embed=embed, view=None)
        
      async def decline_callback(interaction):
        await interaction.response.defer()
        await invite.decline()
        await create_image(type="friendd", username=invite.display_name)
        embed = discord.Embed(title=f"Friend Request from {invite.display_name} Declined", color=color)
        embed.set_footer(text=footertext)
        embed.set_image(url="attachment://image.png")
        await msg.edit(file = discord.File(f"cache/{invite.display_name}.jpg", filename="image.png"), embed=embed, view=None)
  
      accept.callback = accept_callback
      decline.callback = decline_callback
  
      view.add_item(accept)
      view.add_item(decline)
      embed = discord.Embed(title=f"Friend Request from {invite.display_name}", color=color)
      embed.set_footer(text=footertext)
      embed.set_image(url="attachment://image.png")
      msg = await user.send(file = discord.File(f"cache/{invite.display_name}.jpg", filename="image.png"), embed=embed, view=view)
      
    @client.event
    async def event_party_invite(invite):
      await create_image(type="invite", username=invite.sender.display_name)
      view = View()
      accept = Button(label="Accept", style=discord.ButtonStyle.green, emoji="<a:b_yes:606562687446679553>")
      
      decline = Button(label="Decline", style=discord.ButtonStyle.red, emoji="<a:X_Box:871238400731140156>")
  
      async def accept_callback(interaction):
        await interaction.response.defer()
        await invite.accept()
        await create_image(type="invitea", username=invite.sender.display_name)
        embed = discord.Embed(title=f"Invite from {invite.sender.display_name} Accepted", color=color)
        embed.set_footer(text=footertext)
        embed.set_image(url="attachment://image.png")
        await msg.edit(file = discord.File(f"cache/{invite.sender.display_name}.jpg", filename="image.png"), embed=embed, view=None)
        
      async def decline_callback(interaction):
        await interaction.response.defer()
        await invite.decline()
        await create_image(type="invited", username=invite.sender.display_name)
        embed = discord.Embed(title=f"Invite from {invite.sender.display_name} Declined", color=color)
        embed.set_footer(text=footertext)
        embed.set_image(url="attachment://image.png")
        await msg.edit(file = discord.File(f"cache/{invite.sender.display_name}.jpg", filename="image.png"), embed=embed, view=None)
  
      accept.callback = accept_callback
      decline.callback = decline_callback
  
      view.add_item(accept)
      view.add_item(decline)
      embed = discord.Embed(title=f"Party invite from {invite.sender.display_name}", color=color)
      embed.set_footer(text=footertext)
      embed.set_image(url="attachment://image.png")
      msg = await user.send(file = discord.File(f"cache/{invite.sender.display_name}.jpg", filename="image.png"), embed=embed, view=view)
      #try:
        #await invite.accept()
      #except:
        #print(crayons.red("[KLLD] Error Joining A Invite"))
  
  
  
    @client.event
    async def event_party_member_join(member: fortnitepy.PartyMember) -> None:
      await set_crowns()
      await member.party.send(f"Hey {member.display_name}\nThanks for using BoogieFN LobbyBot!\nDiscord: discord.gg/fortnitedev")
      await asyncio.sleep(1)
      await client.party.me.set_emote(asset='EID_KPopDance03')

    

    return client

    
async def get_auths():
    with open("auths.json") as f:
      auths=json.load(f)
    for index, auth in enumerate(auths['auths']):
      if auth['running'] == False:
        auths['auths'][index]['running'] = True
        
        with open(f'auths.json', 'w') as ffs:
          json.dump(auths, ffs, indent=2)
        account_id = auth['accountid']
        device_id = auth['deviceId']
        secret = auth['secret']
        return account_id, device_id, secret, index
      

@discord_bot.slash_command()
async def start(ctx):
  client = onlinebots.get(ctx.author.id, None)
  if client:
    embed = already_bot()
    return await ctx.respond(embed=embed)
  embed=discord.Embed(title="Starting Your Bot <a:5564_Loading_Color:987094303027384370>", color=color)
  embed.set_footer(text=footertext)
  msg = await ctx.respond(embed=embed)
  auths = await get_auths()
  print(auths)
  acc_id = auths[0]
  dev_id = auths[1]
  secret = auths[2]
  index = auths[3]
  global fortnite_client
  fortnite_client = new_client(
    user=ctx.author, 
    device_id=dev_id, 
    account_id=acc_id, 
    secret=secret
  )
  global task
  task = [
    discord_bot.loop.create_task(
      fortnite_client.start()
    ),
    discord_bot.loop.create_task(
      fortnite_client.wait_until_ready()
    )
  ]
  done, _ = await asyncio.wait(
    task, 
    return_when=asyncio.FIRST_COMPLETED
  )
  if task[1] not in done:
    await ctx.send('error starting bot')
  else:
    bots.append(fortnite_client)
    onlinebots.update({ctx.author.id:fortnite_client})
    uid = str(uuid.uuid4())
    uuids.update({ctx.author.id:uid})
    uuids.update({uid:fortnite_client})
    indexes.update({ctx.author.id:index})
    embed=discord.Embed(title=fortnite_client.user.display_name, color=color)
    embed.add_field(name=f"Battle Royale Lobby - {fortnite_client.party.member_count} / 16", value=f"â €", inline=False)
    embed.add_field(name=f"Join our discord server", value="[BoogieFN](https://discord.gg/fortnitedev)")
    embed.add_field(name="Friends:", value=f"{len(fortnite_client.friends)}")
    embed.add_field(name="LobbyBot Dashboard", value=f"[View LobbyBot Dashboard](https://lobbybot.boogiefn.dev/view?id={uid})")
    embed.set_thumbnail(url=f"https://fortnite-api.com/images/cosmetics/br/{fortnite_client.party.me.outfit}/smallicon.png")
    embed.set_footer(text=footertext)
          
    await msg.edit_original_message(embed=embed)
    await asyncio.sleep(1800) 
    await fortnite_client.close()
    
    for tasks in task:
      tasks.cancel()
    del onlinebots[ctx.author.id] 
    del uuids[uid]
    del uuids[ctx.author.id]
    del indexes[ctx.author.id]
    with open("auths.json") as f:
      old_auths=json.load(f)
    old_auths['auths'][index]['running'] = False
    with open(f'auths.json', 'w') as ffs:
      json.dump(old_auths, ffs, indent=2)
    embedstop = discord.Embed(title="Hosting Time Expired!", description = "To start a new bot type /start", color=color)
    embedstop.set_footer(text=footertext)
    await ctx.author.send(embed=embedstop)
          
    
    return



class LoginModal(Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.add_item(InputText(label="Authorization Code", placeholder="Input Code Here"))

    async def callback(self, interaction: discord.Interaction):
      embed=discord.Embed(title="Starting Your Bot <a:5564_Loading_Color:987094303027384370>", color=color)
      embed.set_footer(text=footertext)
      await interaction.response.edit_message(embed=embed, view=None)
      
      PromoView = View()
      discordserv = discord.ui.Button(label='Support Server', style=discord.ButtonStyle.gray, url='https://discord.gg/fortnitedev')
      auth = discord.ui.Button(label='Invite Boogie LobbyBot', style=discord.ButtonStyle.gray, url='https://discord.com/api/oauth2/authorize?client_id=990041302701862963&permissions=534790011200&scope=bot%20applications.commands')
      PromoView.add_item(discordserv)
      PromoView.add_item(auth)
      try:
        global fortnite_bott
        print(interaction.user)
        fortnite_bott = newbot(user=interaction.user)
      
        async def runner():
          return str(self.children[0].value)
      
        fortnite_bott.auth.authorization_code = runner
      
        global task 
        task = [discord_bot.loop.create_task(fortnite_bott.start()), discord_bot.loop.create_task(fortnite_bott.wait_until_ready())]
                      
        done, _ = await asyncio.wait(task, return_when=asyncio.FIRST_COMPLETED)
        if task[1] not in done:
          await interaction.user.send('error starting bot') 
        else:
          bots.append(fortnite_bott)
          onlinebots.update({interaction.user.id:fortnite_bott})
          uid = str(uuid.uuid4())
          uuids.update({interaction.user.id:uid})
          uuids.update({uid:fortnite_bott})
          embed=discord.Embed(title=fortnite_bott.user.display_name, color=color)
          embed.add_field(name=f"Battle Royale Lobby - {fortnite_bott.party.member_count} / 16", value=f"â €", inline=False)
          embed.add_field(name=f"Join our discord server", value="[BoogieFN](https://discord.gg/fortnitedev)")
          embed.add_field(name="Friends:", value=f"{len(fortnite_bott.friends)}")
          embed.add_field(name="LobbyBot Dashboard", value=f"[View LobbyBot Dashboard](https://lobbybot.boogiefn.dev/view?id={uid})")
          embed.set_thumbnail(url=f"https://fortnite-api.com/images/cosmetics/br/{fortnite_bott.party.me.outfit}/smallicon.png")
          embed.set_footer(text=footertext)
          
          await interaction.edit_original_message(embed=embed, view=PromoView)
          await asyncio.sleep(3600) 
          await fortnite_bott.close()
    
          for tasks in task:
            tasks.cancel()
          del onlinebots[interaction.user.id] 
          del uuids[uid]
          del uuids[interaction.user.id]
          embedstop = discord.Embed(title="Hosting Time Expired!", description = "To start a new bot type /create", color=color)
          embedstop.set_footer(text=footertext)
          await interaction.user.send(embed=embedstop, view=PromoView)
    
          return
      except Exception as e:
        import traceback
        print(traceback.format_exc())
        embed = error_embed(traceback.format_exc())
        await interaction.user.send(embed=embed)

class loginView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

      
    @discord.ui.button(
        label="Submit Code",
        style=discord.ButtonStyle.green,
        emoji="ðŸ”’",
        custom_id="submit"
    )
    async def create(self, button: discord.ui.Button, interaction: discord.Interaction):
        client = onlinebots.get(interaction.user.id, None)
        if client: 
          return await interaction.response.send_message("You Have Already Have a Bot Started")
        modal = LoginModal(title="Connect Epic Games to BoogieFN")
        await interaction.response.send_modal(modal)


@discord_bot.slash_command()
async def create(ctx):
  client = onlinebots.get(ctx.author.id, None)
  if client:
    embed = already_bot()
    return await ctx.respond(embed=embed)
  else:
    embed=discord.Embed(title="Create a Lobbybot", color=color)
    embed.add_field(name="step #1", value="Click the **Epic Games** And login with an **ALT**")
    embed.add_field(name="step #2", value="Head over to **Authorization Code** and copy the 32 digit code")
    embed.add_field(name="step #3", value="click the **Submit Code** button and paste the code, then click confirm")
    view = loginView()
    epic = discord.ui.Button(label='Epic Games', style=discord.ButtonStyle.gray, url='https://epicgames.com')
    auth = discord.ui.Button(label='Authorization Code', style=discord.ButtonStyle.gray, url='https://www.epicgames.com/id/login?redirectUrl=https%3A%2F%2Fwww.epicgames.com%2Fid%2Fapi%2Fredirect%3FclientId%3D3446cd72694c4a4485d81b77adbb2141%26responseType%3Dcode')
    view.add_item(epic)
    view.add_item(auth)
    embed.set_image(url="https://media.discordapp.net/attachments/836517393266245632/837230076118302730/image0.png")
    await ctx.respond(embed=embed, view=view, ephemeral=True)


def not_found_embed():
  embed = discord.Embed(title="The item you were looking for was not found!", color=color)
  embed.set_footer(text=footertext)
  return embed

def no_bot():
  embed = discord.Embed(title="You need a **BOT** to run this command!", color=color)
  embed.set_footer(text=footertext)
  return embed

def already_bot():
  embed = discord.Embed(title="You already have a **bot** started!", color=color)
  embed.set_footer(text=footertext)
  return embed

import sys

def error_embed(e):
  exc_type, exc_obj, exc_tb = sys.exc_info()
  fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
  print(exc_type, fname, exc_tb.tb_lineno)
  embed=discord.Embed(title="Uh oh seems like an error occured ðŸ˜¥", description="Join Our [Support Server](https://discord.gg/fortnitedev) And Let Us Know!", color=0xFF0000)
  embed.add_field(name="Error:", value=f"```{e}```")
  return embed


async def create_image(type, *, username):
  if type == "invite":
    background = Image.open(f"images/partyinv.jpg")
    font = ImageFont.truetype("fortnite.otf", 35)
    draw = ImageDraw.Draw(background)
    text = username
    draw.text((487, 115),text, (0,0,0), font=font)
    background.save(f"cache/{username}.jpg")
    return True
  if type == "invitea":
    background = Image.open(f"images/partyinvaccepted.jpg")
    font = ImageFont.truetype("fortnite.otf", 35)
    draw = ImageDraw.Draw(background)
    text = username
    draw.text((487, 115),text, (0,0,0), font=font)
    background.save(f"cache/{username}.jpg")
    return True
  if type == "invited":
    background = Image.open(f"images/declineinv.jpg")
    font = ImageFont.truetype("fortnite.otf", 35)
    draw = ImageDraw.Draw(background)
    text = username
    draw.text((487, 115),text, (0,0,0), font=font)
    background.save(f"cache/{username}.jpg")
    return True
    
  if type == "friend":
    background = Image.open(f"images/friend.jpg")
    font = ImageFont.truetype("fortnite.otf", 35)
    draw = ImageDraw.Draw(background)
    text = username
    draw.text((530, 115),text, (0,0,0), font=font)
    background.save(f"cache/{username}.jpg")
    return True
  if type == "frienda":
    background = Image.open(f"images/friendaccept.jpg")
    font = ImageFont.truetype("fortnite.otf", 35)
    draw = ImageDraw.Draw(background)
    text = username
    draw.text((530, 115),text, (0,0,0), font=font)
    background.save(f"cache/{username}.jpg")
    return True
  if type == "friendd":
    background = Image.open(f"images/frienddecline.jpg")
    font = ImageFont.truetype("fortnite.otf", 35)
    draw = ImageDraw.Draw(background)
    text = username
    draw.text((530, 115),text, (0,0,0), font=font)
    background.save(f"cache/{username}.jpg")
    return True

@set.command(description="Set Equipped Outfit")
async def skin(ctx, *, name):
  await ctx.defer()
  try:
    client = onlinebots.get(ctx.author.id, None)
    if client:
      if "CID_" in name:
        await client.party.me.set_outfit(asset=name)
        embed = discord.Embed(title=f'Set Outfit To {name}', color=color)
        embed.set_thumbnail(url=f"https://fortnite-api.com/images/cosmetics/br/{name}/icon.png")
        embed.set_footer(text=footertext)
        await ctx.respond(embed=embed)
        return
      try:
        cosmetic = await FortniteAPIAsync.cosmetics.get_cosmetic(
          lang="en",
          searchLang="en",
          name=name,
          backendType="AthenaCharacter"
        )
      except:
        embed = not_found_embed()
        await ctx.respond(embed=embed)
        return
      await client.party.me.set_outfit(asset=cosmetic.id)
      embed = discord.Embed(title=f'Set Outfit To {cosmetic.name}', color=color)
      embed.set_thumbnail(url=f"https://fortnite-api.com/images/cosmetics/br/{cosmetic.id}/icon.png")
      embed.set_footer(text=footertext)
      await ctx.respond(embed=embed)
    else:
      embed = no_bot()
      await ctx.respond(embed=embed)
  except Exception as e:
    embed = error_embed(e)
    await ctx.respond(embed=embed)
  
@set.command(description="Set Equipped Emote")
async def emote(ctx, *, name):
  await ctx.defer()
  try:
    client = onlinebots.get(ctx.author.id, None)
    if client:
      if "EID_" in name:
        await client.party.me.set_emote(asset=name)
        embed = discord.Embed(title=f'Set Emote To {name}', color=color)
        embed.set_thumbnail(url=f"https://1dbd854d-eda6-44b7-b0b1-aedad1b34a69.id.repl.co/images/{name}/icon.png")
        embed.set_footer(text=footertext)
        await ctx.respond(embed=embed)
        return
      try:
        cosmetic = await FortniteAPIAsync.cosmetics.get_cosmetic(
          lang="en",
          searchLang="en",
          name=name,
          backendType="AthenaDance"
        )
      except:
        embed = not_found_embed()
        await ctx.respond(embed=embed)
        return
      await client.party.me.set_emote(asset=cosmetic.id)
      embed = discord.Embed(title=f'Set Emote To {cosmetic.name}', color=color)
      embed.set_thumbnail(url=f"https://1dbd854d-eda6-44b7-b0b1-aedad1b34a69.id.repl.co/images/{cosmetic.id}/icon.png")
      embed.set_footer(text=footertext)
      await ctx.respond(embed=embed)
    else:
      embed = no_bot()
      await ctx.respond(embed=embed)
  except Exception as e:
    embed = error_embed(e)
    await ctx.respond(embed=embed)

@set.command(description="Set Equipped BackPack")
async def backbling(ctx, *, name):
  await ctx.defer()
  try:
    client = onlinebots.get(ctx.author.id, None)
    if client:
      if "BID_" in name:
        await client.party.me.set_backpack(asset=name)
        embed = discord.Embed(title=f'Set BackBling To {name}', color=color)
        embed.set_thumbnail(url=f"https://1dbd854d-eda6-44b7-b0b1-aedad1b34a69.id.repl.co/images/{name}/icon.png")
        embed.set_footer(text=footertext)
        await ctx.respond(embed=embed)
        return
      try:
        cosmetic = await FortniteAPIAsync.cosmetics.get_cosmetic(
          lang="en",
          searchLang="en",
          name=name,
          backendType="AthenaBackpack"
        )
      except:
        embed = not_found_embed()
        await ctx.respond(embed=embed)
        return
      await client.party.me.set_backpack(asset=cosmetic.id)
      embed = discord.Embed(title=f'Set BackBling To {cosmetic.name}', color=color)
      embed.set_thumbnail(url=f"https://1dbd854d-eda6-44b7-b0b1-aedad1b34a69.id.repl.co/images/{cosmetic.id}/icon.png")
      embed.set_footer(text=footertext)
      await ctx.respond(embed=embed)
    else:
      embed = no_bot()
      await ctx.respond(embed=embed)
  except Exception as e:
    embed = error_embed(e)
    await ctx.respond(embed=embed)

@set.command(description="Set Equipped pickaxe")
async def pickaxe(ctx, *, name):
  await ctx.defer()
  try:
    client = onlinebots.get(ctx.author.id, None)
    if client:
      if "Pickaxe_" in name:
        await client.party.me.set_pickaxe(asset=name)
        embed = discord.Embed(title=f'Set Pickaxe To {name}', color=color)
        embed.set_thumbnail(url=f"https://1dbd854d-eda6-44b7-b0b1-aedad1b34a69.id.repl.co/images/{name}/icon.png")
        embed.set_footer(text=footertext)
        await ctx.respond(embed=embed)
        return
      try:
        cosmetic = await FortniteAPIAsync.cosmetics.get_cosmetic(
          lang="en",
          searchLang="en",
          name=name,
          backendType="AthenaPickaxe"
        )
      except:
        embed = not_found_embed()
        await ctx.respond(embed=embed)
        return
      await client.party.me.set_pickaxe(asset=cosmetic.id)
      embed = discord.Embed(title=f'Set Pickaxe To {cosmetic.name}', color=color)
      embed.set_thumbnail(url=f"https://1dbd854d-eda6-44b7-b0b1-aedad1b34a69.id.repl.co/images/{cosmetic.id}/icon.png")
      embed.set_footer(text=footertext)
      await ctx.respond(embed=embed)
    else:
      embed = no_bot()
      await ctx.respond(embed=embed)
  except Exception as e:
    embed = error_embed(e)
    await ctx.respond(embed=embed)


@discord_bot.slash_command()
async def stop(ctx):
    try:
      client = onlinebots.get(ctx.author.id)
      if client:
        embed = discord.Embed(title=f'Shut Down {client.user.display_name}', color=color)
        embed.set_footer(text=footertext)
        try:
          index = indexes.get(ctx.author.id)
          with open("auths.json") as f:
            old_auths=json.load(f)
          old_auths['auths'][int(index)]['running'] = False
          with open(f'auths.json', 'w') as ffs:
            json.dump(old_auths, ffs, indent=2)
        except:
          print()
        del onlinebots[ctx.author.id]
        uid = uuids[ctx.author.id]
        del uuids[uid]
        del uid
        await ctx.respond(embed=embed)
        print(f"[-] {client.user.display_name} Bot stopped")
        await client.close()
      else:
        embed = no_bot()
        await ctx.respond(embed=embed)
    except Exception as e:
          embed = error_embed(e)
    
          await ctx.author.send(embed=embed)


class HideList(discord.ui.View):
		def __init__(
			self, 
			user,
			result
		):
				super().__init__()
				self.add_item(
					HideDropdown(
						user=user,
						result=result
					)
				)


class HideDropdown(discord.ui.Select):
	def __init__(
		self, 
		user,
		result,
	):
			self.choice_list = {
				"Cancel": "CANCEL_SKIN_TASK"
			}
			options = []
			counting = 0
			for outfit in result:
				self.choice_list.update({outfit['name']:outfit['id']})
				counting+=1
				options.append(
					discord.SelectOption(
						label=outfit['name'], 
						description=f"Hide This Member"
					)
				)

			# The placeholder is what will be shown when no option is chosen
			# The min and max values indicate we can only pick one of the three options
			# The options parameter defines the dropdown options. We defined this above
			super().__init__(
					placeholder="Select A Party Member",
					min_values=1,
					max_values=1,
					options=options,
			)

	async def callback(self, interaction: discord.Interaction):
			final = self.choice_list[self.values[0]]
			client = onlinebots.get(interaction.user.id)
			async def set_and_update_party_prop(schema_key: str, new_value: str):
				prop = {schema_key: client.party.me.meta.set_prop(schema_key, new_value)}
				await client.party.patch(updated=prop)
			user = await client.fetch_profile(final)
			member = client.party.get_member(user.id)
			raw_squad_assignments = client.party.meta.get_prop('Default:RawSquadAssignments_j')["RawSquadAssignments"]
			for m in raw_squad_assignments:
				if m['memberId'] == member.id:
					raw_squad_assignments.remove(m)
			await set_and_update_party_prop('Default:RawSquadAssignments_j',{'RawSquadAssignments': raw_squad_assignments})
						
			return await interaction.response.send_message(f"Hid {final}")


@party.command()
async def hide(ctx):
    await ctx.defer()
    client = onlinebots.get(ctx.author.id)
    if client:
        result = []
        for member in client.party.members:
          result.append(
			      {
					  'name': member.display_name,
					  'id': member.display_name
				  }
			  )


    view = HideList(
		user=ctx.author,
		result=result
	)
    return await ctx.respond("Who do you want to hide?", view=view)

@party.command()
async def unhide(ctx, user):
    client=onlinebots.get(ctx.author.id, None)
    if client.party.me.leader:
        user = await client.fetch_profile(user)
        member = client.party.get_member(user.id)

        await member.promote()

        await ctx.respond("Unhid all players.")

    else:
        await ctx.respond("I am not party leader.")

@set.command()
async def crowns(ctx, amount):
  await ctx.defer()
  client=onlinebots.get(ctx.author.id, None)
  try:
    meta = client.party.me.meta
    data = (meta.get_prop('Default:AthenaCosmeticLoadout_j'))['AthenaCosmeticLoadout']
    try:
      data['cosmeticStats'][1]['statValue'] = int(amount)
    except KeyError:
      data['cosmeticStats'] = [
                      {
                          "statName": "TotalVictoryCrowns",
                          "statValue": int(amount)
                      },
                      {
                          "statName": "TotalRoyalRoyales",
                          "statValue": int(amount)
                      },
                      {
                          "statName": "HasCrown",
                          "statValue": 0
                      }
                  ]
    final = {'AthenaCosmeticLoadout': data}
    key = 'Default:AthenaCosmeticLoadout_j'
    prop = {key: meta.set_prop(key, final)}
      
    await client.party.me.patch(updated=prop)
    await client.party.me.clear_emote()
    await client.party.me.set_emote(asset='EID_Coronet')
    embed=discord.Embed(title=f"Set Crown Wins To {amount}", color=color)
    embed.set_footer(text=footertext)
    await ctx.respond(embed = embed)
    print(data['cosmeticStats'][1]['statValue'])
  except Exception as e:
    embed = error_embed(e)
    await ctx.respond(embed=embed)

@discord_bot.slash_command()
async def platform(ctx, setting = None):
  try:
    client=onlinebots.get(ctx.author.id, None)
    if client:
      if setting.lower() == 'xbox':
        client.platform = fortnitepy.Platform.XBOX
        await client.restart()
        embed=discord.Embed(title='Platform changed to: **XBOX (XBL)**', color=color)
        embed.set_footer(text=footertext)
        await ctx.respond(embed=embed)
      elif setting.lower() == 'pc':   
        client.platform = fortnitepy.Platform.WINDOWS
        embed=discord.Embed(title='Platform changed to: **PC**', color=color)
        await client.restart()
        embed.set_footer(text=footertext)
        await ctx.respond(embed=embed)
      elif setting.lower() == 'playstation':
        client.platform = fortnitepy.Platform.PLAYSTATION
        await client.restart()
        embed=discord.Embed(title='Platform changed to: **Playstation**', color=color)
        embed.set_footer(text=footertext)
        await ctx.respond(embed=embed)
      elif setting.lower() == 'switch':
        client.platform = fortnitepy.Platform.SWITCH
        await client.restart()
        embed=discord.Embed(title='Platform changed to: **SWITCH**', color=color)
        embed.set_footer(text=footertext)
        await ctx.respond(embed=embed)
      elif setting.lower() == 'mobile':
        client.platform = fortnitepy.Platform.IOS
        await client.restart()
        embed=discord.Embed(title='Platform changed to: **MOBILE**', color=color)
        embed.set_footer(text=footertext)
        await ctx.respond(embed=embed)
      elif setting.lower() == 'ps5':
        client.platform = fortnitepy.Platform.PLAYSTATION_5
        await client.restart()
        embed=discord.Embed(title='Platform changed to: **Playstation 5**', color=color)
        embed.set_footer(text=footertext)
        await ctx.respond(embed=embed)
      elif setting.lower() == 'xbox_x':
        client.platform = fortnitepy.Platform.XBOX_X
        await client.restart()
        embed=discord.Embed(title='Platform changed to: **Xbox Series X**', color=color)
        embed.set_footer(text=footertext)
        await ctx.respond(embed=embed)
      else:
        embed=discord.Embed(title="Platform Not Found!", color=color)
        embed.set_footer(text=footertext)
        await ctx.respond(embed=embed)
    else:
      embed = no_bot()
      await ctx.respond(embed=embed)
  except Exception as e:
          embed = error_embed(e)
    
          await ctx.author.send(embed=embed)

@discord_bot.slash_command()
async def restart(ctx):
        try:
                client=onlinebots.get(ctx.author.id, None)

                if client:


                    await client.restart()
                    embed=discord.Embed(title=f"LobbyBot Was Restarted!", color=color)
                    embed.set_footer(text=footertext)
                    await ctx.respond(embed=embed)
                    return
                embed = no_bot()
                await ctx.respond(embed=embed)

        except Exception as e:
          embed = error_embed(e)
    
          await ctx.author.send(embed=embed)


async def get_variants(
	client, 
	type_, 
	variant_channel=None, 
	selected_int=None, 
	selected=None
	):
		config_overrides = {"item": type_, variant_channel: selected['tag']}
		if variant_channel != None:
				if variant_channel == 'pattern':
					variants = client.party.me.create_variant(config_overrides=config_overrides, pattern=str(selected_int))
				if variant_channel == 'numeric':
					variants = client.party.me.create_variant(config_overrides=config_overrides, numeric=str(selected_int))
				if variant_channel == 'clothingcolor':
					variants = client.party.me.create_variant(config_overrides=config_overrides, clothing_color=str(selected_int))
				if variant_channel == 'jerseycolor':
					variants = client.party.me.create_variant(config_overrides=config_overrides, jersey_color=str(selected_int))
				if variant_channel == 'parts':
					variants = client.party.me.create_variant(config_overrides=config_overrides, parts=str(selected_int))
				if variant_channel == 'progressive':
					variants = client.party.me.create_variant(config_overrides=config_overrides, progressive=str(selected_int))
				if variant_channel == 'particle':
					variants = client.party.me.create_variant(config_overrides=config_overrides, particle=str(selected_int))
				if variant_channel == 'material':
					variants = client.party.me.create_variant(config_overrides=config_overrides, material=str(selected_int))
				if variant_channel == 'emissive':
					variants = client.party.me.create_variant(config_overrides=config_overrides, emissive=str(selected_int))
				if variant_channel == 'hair':
					variants = client.party.me.create_variant(config_overrides=config_overrides, hair=str(selected_int))
				if variant_channel == 'mesh':
					variants = client.party.me.create_variant(config_overrides=config_overrides, mesh=str(selected_int))

				return variants


@outfit.command(description="Change Styles")
async def styles(ctx, *, name):
  await ctx.defer()
  client =onlinebots.get(ctx.author.id, None)
  r = requests.get(f'https://fortnite-api.com/v2/cosmetics/br/search/all?name={name}')
  data = r.json()
  for sub_dict in data['data']:
    embed=discord.Embed(title=sub_dict['name'], color=color)
    embed.set_footer(text=f"Type the style number to change to it | {footertext}")
    embed.set_thumbnail(url=sub_dict['images']['icon'])
    for troll in sub_dict['variants']:
      yy = troll['channel']
      pp = troll['options']
      id = sub_dict['id']
      stylenum = 0
      for style in pp:
        stylenum+=1
        embed.add_field(name=f"style #{stylenum}:", value=style['name'], inline=True)
      await ctx.respond(embed=embed)
      def check(m):
        return m.content  and m.author.id == ctx.author.id

      cnt = await discord_bot.wait_for('message', check=check)
      stylenum = int(cnt.content) - 1
      selected = pp[int(stylenum)]
      
      user_selection_int = int(stylenum)
      variants = await get_variants(client=client, type_="AthenaCharacter",         variant_channel=yy.lower(), selected_int=user_selection_int, selected=selected)
      await client.party.me.edit_and_keep(
				partial(
					client.party.me.set_outfit, 
					asset=id, 
					variants=variants
				)
			)
      embed=discord.Embed(title="Style set to " + selected['name'], color=color)
      embed.set_thumbnail(url=selected['image'])
      embed.set_footer(text=footertext)
      await ctx.respond(embed=embed)

@discord_bot.slash_command()
async def template(ctx):
  await ctx.defer()
  client = onlinebots.get(ctx.author.id, None)
  if client:
    try:
      print()
    except Exception as e:
      print(e)
      embed = error_embed(e)
      await ctx.respond(embed=embed)
  else:
    embed = no_bot()
    await ctx.respond(embed=embed)

@party.command()
async def send(ctx, *, message = None):
        await ctx.defer()
        try:
                client=onlinebots.get(ctx.author.id, None)

                if client:


                    await client.party.send(message)
                    embed=discord.Embed(title=f"Sent ã€Ž{message}ã€ to party chat", color=color)
                    embed.set_footer(text=footertext)
                    await ctx.respond(embed=embed)
                    return
                client=None
                embed = no_bot()
                await ctx.respond(embed=embed)

        except Exception as e:
          embed=error_embed(e)
    
          await ctx.author.send(embed=embed)


@party.command()
async def member_whisper(ctx, member, *, content):
  await ctx.defer()
  client = onlinebots.get(ctx.author.id, None)
  if client:
    try:
      user = await client.fetch_user(member)
      member = client.party.get_member(user.id)
      await member.send(content)
      embed=discord.Embed(title=f"Whispered {content} to {member.display_name}", color=color)
      embed.set_footer(text=footertext)
      await ctx.respond(embed=embed)
    except Exception as e:
      print(e)
      embed = error_embed(e)
      await ctx.respond(embed=embed)
  else:
    embed = no_bot()
    await ctx.respond(embed=embed)

@party.command()
async def unready(ctx):
        try:
                client=onlinebots.get(ctx.author.id, None)

                if client:


                    await client.party.me.set_ready(fortnitepy.ReadyState.NOT_READY)
                    embed=discord.Embed(title=f"UnReady!", color=color)
                    embed.set_footer(text=footertext)
                    await ctx.respond(embed=embed)
                    return
                client=None
                print('i eat kids')
                embed = no_bot()
                await ctx.respond(embed=embed)

        except Exception as e:
          embed=error_embed(e)
    
          await ctx.respond(embed=embed)


@party.command()
async def ready(ctx):
        try:
                client=onlinebots.get(ctx.author.id, None)

                if client:


                    await client.party.me.set_ready(fortnitepy.ReadyState.READY)
                    embed=discord.Embed(title=f"Ready!", color=color)
                    embed.set_footer(text=footertext)
                    await ctx.respond(embed=embed)
                    return
                client=None
                embed = no_bot()
                await ctx.respond(embed=embed)

        except Exception as e:
          embed=error_embed(e)
    
          await ctx.respond(embed=embed)

@party.command()
async def sitout(ctx):
        try:
                client=onlinebots.get(ctx.author.id, None)

                if client:


                    await client.party.me.set_ready(fortnitepy.ReadyState.SITTING_OUT)
                    embed=discord.Embed(title=f"Sitting Out!", color=color)
                    embed.set_footer(text=footertext)
                    await ctx.respond(embed=embed)
                    return
                client=None
                embed = no_bot()
                await ctx.respond(embed=embed)

        except Exception as e:
          embed=error_embed(e)
    
          await ctx.respond(embed=embed)

@party.command()
async def sitin(ctx):
        try:
                client=onlinebots.get(ctx.author.id, None)

                if client:


                    await client.party.me.set_ready(fortnitepy.ReadyState.NOT_READY)
                    embed=discord.Embed(title=f"Sitting In!", color=color)
                    embed.set_footer(text=footertext)
                    await ctx.respond(embed=embed)
                    return
                client=None
                embed = no_bot()
                await ctx.respond(embed=embed)

        except Exception as e:
          embed=error_embed(e)
    
          await ctx.respond(embed=embed)

@party.command()
async def leave(ctx):
        try:
                client=onlinebots.get(ctx.author.id, None)

                if client:


                    await client.party.me.leave()
                    embed=discord.Embed(title="Left party.", color=color)
                    embed.set_footer(text=footertext)
                    await ctx.respond(embed=embed)
                    return
                client=None
                embed = no_bot()
                await ctx.respond(embed=embed)
        except Exception as e:
          embed=error_embed(e)
    
          await ctx.author.send(embed=embed)


@party.command()
async def join(ctx, *, member = None):
        await ctx.defer()
        try:
                client=onlinebots.get(ctx.author.id, None)

                if client:


                    if member is None:
                      user = await client.fetch_profile(ctx.message.author.id)
                      friend = client.get_friend(user.id)
                    elif member is not None:
                      user = await client.fetch_profile(member)
                      friend = client.get_friend(user.id)
                    await friend.join_party()
                    embed=discord.Embed(title=f"Joined {friend.display_name}'s party.", color=color)
                    embed.set_footer(text=footertext)
                    await ctx.respond(embed=embed)


                    return
                client=None
                print('i eat kids')
                embed = no_bot()
                await ctx.respond(embed=embed)

        except Exception as e:
          embed=error_embed(e)
    
          await ctx.respond(embed=embed)

@party.command()
async def invite(ctx, *, member = None):
  try:
    client=onlinebots.get(ctx.author.id, None)
    if client:
      if member == 'all':
          friends = client.friends
          invited = []

          try:
              for f in friends:
                  friend = client.get_friend(f)

                  if friend.is_online():
                      invited.append(friend.display_name)
                      await friend.invite()
              
              embed=discord.Embed(title=f"Invited {len(invited)} friends to the party.", color=color)
              embed.set_footer(text=footertext)
              await ctx.respond(embed=embed)

          except Exception:
              pass

      else:
          try:
              if member is None:
                  user = await client.fetch_profile(ctx.message.author.id)
                  friend = client.get_friend(user.id)
              if member is not None:
                  user = await client.fetch_profile(member)
                  friend = client.get_friend(user.id)

              await friend.invite()
              embed=discord.Embed(title=f"Invited {friend.display_name} to the party.", color=color)
              embed.set_footer(text=f"{footertext}")
              await ctx.respond(embed=embed)
          except fortnitepy.PartyError:
              embed=discord.Embed(title=f"That user is already in the party.", color=color)
              embed.set_footer(text=f"{footertext}")
              await ctx.respond(embed=embed)
          except fortnitepy.HTTPException:
              embed=discord.Embed(title=f"Something went wrong inviting that user.", color=color)
              embed.set_footer(text=f"{footertext}")
              await ctx.respond(embed=embed)

  except Exception as e:
          embed=error_embed(e)
    
          await ctx.respond(embed=embed)


@party.command()
async def playlist(ctx, playlist_id):
  await ctx.defer()
  client = onlinebots.get(ctx.author.id, None)
  if client:
    try:
      await client.party.set_playlist(playlist=playlist_id)
      embed = discord.Embed(title=f"Set the party Playlist to **{playlist_id}**")
      embed.set_footer(text=footertext)
      await ctx.respond(embed=embed)
    except Exception as e:
      print(e)
      embed = error_embed(e)
      await ctx.respond(embed=embed)
  else:
    embed = no_bot()
    await ctx.respond(embed=embed)

@party.command()
async def kick(ctx, member):
  await ctx.defer()
  client = onlinebots.get(ctx.author.id, None)
  if client:
    try:
      user = await client.fetch_user(member)
      member = client.party.get_member(user.id)
      await member.kick()
      embed=discord.Embed(title=f"Kicked {member.display_name} from the party!", color=color)
      embed.set_footer(text=footertext)
      await ctx.respond(embed=embed)
    except fortnitepy.Forbidden:
      await ctx.respond("I can't kick that user because I am not party leader")
      return
    except AttributeError:
      await ctx.send("Couldn't find that user.")
      return
    except Exception as e:
      print(e)
      embed = error_embed(e)
      await ctx.respond(embed=embed)
  else:
    embed = no_bot()
    await ctx.respond(embed=embed)


@party.command()
async def privacy(ctx, setting = None):
        await ctx.defer()
        try:
                client=onlinebots.get(ctx.author.id, None)

                if client:
                    if setting.lower() == 'public':
                        await client.party.set_privacy(fortnitepy.PartyPrivacy.PUBLIC)
                        embed=discord.Embed(title='Party Privacy set to: Public', color=color)
                        embed.set_footer(text=footertext)
                        await ctx.respond(embed=embed)
                    if setting.lower() == 'private':
                        await client.party.set_privacy(fortnitepy.PartyPrivacy.PRIVATE)
                        embed=discord.Embed(title='Party Privacy set to: Private', color=color)
                        embed.set_footer(text=footertext)
                        await ctx.respond(embed=embed)
                    if setting.lower() == 'friends':
                        await client.party.set_privacy(fortnitepy.PartyPrivacy.FRIENDS)
                        embed=discord.Embed(title='Party Privacy set to: Friends', color=color)
                        embed.set_footer(text=footertext)
                        await ctx.respond(embed=embed)



                    return
                client=None
                embed = no_bot()
                await ctx.respond(embed=embed)
        except fortnitepy.Forbidden:
            embed=discord.Embed(title='I can not set the party privacy because I am not party leader.', color=color)
            embed.set_footer(text=footertext)
            await ctx.respond(embed=embed)

        except Exception as e:
          embed = error_embed(e)
    
          await ctx.author.send(embed=embed)




@party.command()
async def promote(ctx, user):
  await ctx.defer()
  client = onlinebots.get(ctx.author.id, None)
  if client:
    try:
      user = await client.fetch_profile(user)
      member = client.party.get_member(user.id)
      await member.promote()
      embed=discord.Embed(title=f"Promoted {member.display_name} To Party Leader!", color=color)
      embed.set_footer(text=footertext)
      await ctx.respond(embed=embed)
    except Exception as e:
      print(e)
      embed = error_embed(e)
      await ctx.respond(embed=embed)
  else:
    embed = no_bot()
    await ctx.respond(embed=embed)

@discord_bot.slash_command(name="map")
async def slash_map(ctx):
  """Shows The Current Map Of Fortnite!"""
  embed=discord.Embed(
    title="Fortnite Map",
    description="Fortnite Map"
  )
  embed.set_image(url="https://fortnite-api.com/images/map_en.png")
  await ctx.respond(embed=embed)



@discord_bot.slash_command(name="onlinebots")
async def slash_onlineusers(ctx):
  """Shows All OnlineBots!"""
  if len(onlinebots) == 0:
    return await ctx.respond("There Are No Online Bots")
  embed = discord.Embed(
    title=f"{len(onlinebots)} Bots Online!",
  )
  await ctx.respond(embed=embed)
  

@discord_bot.slash_command(name="aes")
async def aes(ctx):
        botdata.commands_today += 1
        a = await fetch("https://fortnite-api.com/v2/aes")
        embed = discord.Embed(title="AES", description=a['data']['build'], color=0x00ff00)
        embed.add_field(name="MAIN", value="`" + a['data']['mainKey'] + "`")
        for x in a['data']['dynamicKeys']:
                embed.add_field(name=x['pakFilename'], value=f"pakGuid: `{x['pakGuid']}`\nKey: `{x['key']}`", inline=False)
        await ctx.send(embed=embed)


@discord_bot.slash_command(name="news")
async def brnews(ctx, l=None):

	response = requests.get(f'https://fortnite-api.com/v2/news/br?language=en')

	geted = response.json()

	if response.status_code == 200:

		image = geted['data']['image']

		embed = discord.Embed(title="NEWS")
		embed.set_image(url=image)

		await ctx.respond(embed=embed)

	elif response.status_code == 400:

		error = geted['error']

		embed = discord.Embed(title='Error', description=f'`{error}`')

		await ctx.respond(embed=embed)

	elif response.status_code == 404:

		error = geted['error']

		embed = discord.Embed(title='Error', description=f'``{error}``')

		await ctx.respond(embed=embed)
  

@discord_bot.slash_command(name="ping")
async def ping(ctx):
  """Shows The Latency Of The Bot"""
  embed = discord.Embed(
    title=f"{round(bot.latency * 1000)}ms",
  )
  await ctx.respond(embed=embed)







@discord_bot.slash_command(name="uptime")
async def slash_uptime(ctx):
    """Shows The Uptime Of The Bot."""
    # Calculate the uptime by getting the current time and subtracting the start time
    uptime = datetime.datetime.utcnow() - bot.start_time
    # Convert the uptime to a formatted string
    uptime_str = str(uptime).split(".")[0]
    # Create the embed message
    embed = discord.Embed(
        title="Uptime",
        description=uptime_str
    )
    await ctx.respond(embed=embed)


@discord_bot.slash_command()
async def friend_add(ctx, *, member = None):
        await ctx.defer()
        try:
                client=onlinebots.get(ctx.author.id, None)

                if client:


                    user = await client.fetch_profile(member)
                    friends = client.friends
                    if user.id in friends:
                        embed=discord.Embed(title=f"I already have {user.display_name} as a friend", color=color)
                        embed.set_footer(text=footertext)
                        await ctx.respond(embed=embed)
                    else:
                        await client.add_friend(user.id)
                        embed=discord.Embed(title=f"Sent a friend request to {user.display_name}", color=color)
                        embed.set_footer(text=footertext)
                        await ctx.respond(embed=embed)
                        return
                client=None
                print('i eat kids')
                embed = no_bot()
                await ctx.respond(embed=embed)

        except fortnitepy.HTTPException:
                await ctx.respond("There was a problem trying to add this friend.")

        except AttributeError:
                embed=discord.Embed(title="I can't find a player with that name.", color=color)
                embed.set_footer(text=footertext)
                await ctx.respond(embed=embed)

        except Exception as e:
          embed = error_embed(e)
    
          await ctx.author.send(embed=embed)

@discord_bot.slash_command()
async def friend_remove(ctx, *, member = None):
        await ctx.defer()
        try:
                client=onlinebots.get(ctx.author.id, None)

                if client:


                    user = await client.fetch_profile(member)
                    friends = client.friends
                    if user.id != friends:
                        embed=discord.Embed(title=f"I dont have {user.display_name} added", color=color)
                        embed.set_footer(text=footertext)
                        await ctx.respond(embed=embed)
                    else:
                        await client.remove_friend(user.id)
                        embed=discord.Embed(title=f"Removed {user.display_name} From Friends List", color=color)
                        embed.set_footer(text=footertext)
                        await ctx.respond(embed=embed)
                        return
                client=None
                embed = no_bot()
                await ctx.respond(embed=embed)

        except fortnitepy.HTTPException:
                await ctx.respond("There was a problem trying to add this friend.")

        except AttributeError:
                embed=discord.Embed(title="I can't find a player with that name.", color=color)
                embed.set_footer(text=footertext)
                await ctx.respond(embed=embed)

        except Exception as e:
          embed=error_embed(e)
    
          await ctx.author.send(embed=embed)


@set.command()
async def level(ctx, level = None):
        try:
                client=onlinebots.get(ctx.author.id, None)

                if client:


                    await client.party.me.set_banner(season_level=level)
                    embed=discord.Embed(title=f"Level set to: {level}", color=color)
                    embed.set_footer(text=footertext)
                    await ctx.respond(embed=embed)
                    return
                client=None
                embed = no_bot()
                await ctx.respond(embed=embed)

        except Exception as e:
          embed=error_embed(e)
    
          await ctx.author.send(embed=embed)

import websockets


discord_bot.run(os.environ['token'])
