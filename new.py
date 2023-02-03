import sanic, aiohttp

app = sanic.Sanic("coscheck")

@app.route("/")
async def index(request):
  return await sanic.response.file("passy.mp4")


@app.route("/check")
async def check(request):
  """Check If The build Submitted is The Latest if not return cosmetics. Via Fortnite-api"""
  build = request.args.get("build")
  if not build:
    return sanic.response.json(
      {
        "status": 498,
        "error": "No Build Submitted"
      }
    )

  async with aiohttp.ClientSession() as session:
    async with session.get("https://fortnite-api.com/v2/cosmetics/br/new") as response:
      data = await response.json()
      data = data['data']
      
  if data['build'] == build:
    return sanic.response.json(
      {
        "status": 200,
        "newCosmetics": False
      }
    )

  else:
    cosmetics = {}
    items = data['items']
    for cosmetic in items:
      cosmetics[cosmetic["id"]] = {
        "name": str(cosmetic["name"]),
        "description": str(cosmetic["description"]),
        "id": str(cosmetic["id"]),
        "rarity": str(cosmetic["rarity"]["value"]),
        "type": str(cosmetic["type"]["value"]),
        "image": f"https://8490557b-ee16-43aa-89d5-ed272f5f0aee.id.repl.co/images/{str(cosmetic['id'])}/icon.png"
      }
    return sanic.response.json(
      {
        "status": 200, 
        "newCosmetics": True,
        "build": data['build'],
        "added": cosmetics
      }
    )

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=False, access_log=False)
