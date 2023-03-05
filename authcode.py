import sanic
import aiohttp
import uvloop

import os
import sys
import json
import asyncio
import requests
import PirxcyPinger

from typing import Any
from jinja2 import FileSystemLoader
from jinja2 import Environment

#

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

app = sanic.Sanic("Config")

env = Environment(loader=FileSystemLoader('./templates', encoding='utf8'),
                  extensions=['jinja2.ext.do'])


def render_template(filename: str, **kwargs: Any) -> str:
  template = env.get_template(filename)
  return sanic.response.html(template.render(**kwargs))


async def post():
    url = PirxcyPinger.get_url(platform='replit')
    try:
        await PirxcyPinger.post(
            url=url,
            external_urls=[
                "https://pinger.klld.tk/"
                "https://publicpinger.gomanshiopirxcy.repl.co/",
                "https://zeropinger.rednosezixy.repl.co/"
                "https://publicpinger-5.gomanshiopirxcy.repl.co/"
                "https://publicpinger.gomanshiopirxcy.repl.co/"
                "https://publicpinger.nobu-world-development.repl.co/"
            ])
        print(f"Uploaded {url}")
    except PirxcyPinger.AlreadyPinging:
        print("URL Already Submitted!")
    except:
        pass




@app.route('/')
async def index(request):
  return await sanic.response.file('index.html')

@app.route('/cdn/fast')
async def fast(request):
  return await sanic.response.file('cdn/fast.html')


@app.route("/taga/<file>")
async def jsciptetaga(request, file):
  """Return a File in The Z Folder"""
  try:
    return await sanic.response.file(f"taga/{file}")
  except:
    return sanic.response.text("ERROR")


@app.route("/zuppa/<file>")
async def zuppa2(request, file):
  """Return a File in The Z Folder"""
  try:
    return await sanic.response.file(f"zuppa/{file}")
  except:
    return sanic.response.text("ERROR")


@app.route("/<file>")
async def z(request, file):
  """Return a File in The Z Folder"""
  try:
    return await sanic.response.file(f"{file}")
  except:
    return sanic.response.text("ERROR")


@app.route("/cdn/<file>")
async def w(request, file):
  """Return a File in The Z Folder"""
  try:
    return await sanic.response.file(f"cdn/{file}")
  except:
    return sanic.response.text("ERROR")



# + f'''
# DEVICE_ID="{auths['deviceId']}"
# ACCOUNT_ID="{auths['accountId']}"
# SECRET="{auths['secret']}"</textarea><br>''' + '''

@app.route("/codeauth", methods=["POST", "GET"])
async def codeauth2(request):
  if request.method == "POST":
    code = request.form.get('CODE')
    reponse = requests.post(
      url=
      'https://account-public-service-prod.ol.epicgames.com/account/api/oauth/token',
      data=f"grant_type=authorization_code&code={code}",
      headers={
        "Content-Type":
        "application/x-www-form-urlencoded",
        "Authorization":
        "basic MzQ0NmNkNzI2OTRjNGE0NDg1ZDgxYjc3YWRiYjIxNDE6OTIwOWQ0YTVlMjVhNDU3ZmI5YjA3NDg5ZDMxM2I0MWE="
      }).json()
    print(reponse)
    if reponse != {
        'errorCode':
        'errors.com.epicgames.account.oauth.authorization_code_not_found',
        'errorMessage':
        'Sorry the authorization code you supplied was not found. It is possible that it was no longer valid',
        'messageVars': [],
        'numericErrorCode': 18059,
        'originatingService': 'com.epicgames.account.public',
        'intent': 'prod',
        'error_description':
        'Sorry the authorization code you supplied was not found. It is possible that it was no longer valid',
        'error': 'invalid_grant'
    }:
      pass
    else:
      return sanic.response.text("Sorry the authorization code you supplied was not found. It is possible that it was no longer valid")
      return sanic.response.html('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="PirxcyAuth - An Advanced Replit Auth Generator!" />
	<meta name="keywords" content="fn dev,fndev,fortnite dev,easyfn,ezfn,fortnite,fortnite bot,fortnite lobbybot,ezfn fortnite bot,easyfn fortnite bot,fortnite skin,cosmetics,fortnite items,fortnite game,fortnite skins,battle royale,fortnite battle royale,epic fortnite,fortnite game,battlepass,fortnite battlepass,fortnite skin changer,skin changer,fortnite hxd, pirxcybot, PirxcyPinger, klld" />
	<meta name="author" content="klld" />
    <title id=title>klldAuth</title>
  <!--favicon-img--> 
    <link rel="stylesheet" href="https://pinger.klld.tk/Style.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.2.6/gsap.min.js"></script>
</head>
<body data-new-gr-c-s-check-loaded="14.1056.0" data-gr-ext-installed=""><audio id="music" src="https://PirxcyPingerFinal.pirxcy1942.repl.co/aggro.mp3" autoplay="" loop="" onplaying="if (!window.__cfRLUnblockHandlers) return false; " style="display: none;" data-cf-modified-1201a5cfd63685f4a9e1a629-=""></audio>
<body>

    <!--contains all the div-->
    <div id="all">
    <!--mouse  follower-->
        <div class="cursor"></div>
    <!--mouse  follower-->
    <!--loader-->
        <div id="loader">
            <span class="color">Pirxcy</span>Auth
        </div>
    <!--loader-end-->
    <!--link-screen-->
        <div id="breaker">
        </div>
        <div id="breaker-two">
        </div>
    <!--link-screen-->
        <!--Main-Section-->
        <!--Navigator-fullscreen-->
        <div id="navigation-content">
            <div class="logo">
            </div>
            <div class="navigation-close">
                <span class="close-first"></span>
                <span class="close-second"></span>
            </div>
            <div class="navigation-links">
                <a href="#" data-text="PIRXCY" id="home-link" >MAIN</a>
                <a data-text="PINGER" id="login-link" href="https://PirxcyPingerFinal.pirxcy1942.repl.co">PINGER</a>
            </div>
        </div>
        <!--Navigator-Fullscreen END-->
          <!--Home Page-->
        <!--Menubar-->
        <div id="navigation-bar">
            <div class="menubar">
                <span class="first-span"></span>
                <span class="second-span"></span>
                <span class="third-span"></span>
            </div>
        </div>
        <!--Menubar End-->
          <!--Header-->
        <div id="header">
            <div id="particles"></div>
              <!--Social Media Links-->
            <!--Social Media Links end-->
            <div class="header-content">
                <div class="header-content-box">
                <div class="firstline"><span class="color">klld</span>Auth</div>
                <div class="secondline">
                Info: 
            <span class="txt-rotate color" data-period="1200"data-rotate='[ "Made By klld", "Dont Steal Pussy"]'></span>
            <span class="slash">|</span>
				<script>
    function check() {
      cide = document.getElementById("CODE");
      button = document.getElementById("button");
      button.disabled = false;
    }
  </script>

				<body>
'''
                                 + f'''
 DEVICE_ID="{auths['deviceId']}"
 ACCOUNT_ID="{auths['accountId']}"
 SECRET="{auths['secret']}"</textarea><br>''' + '''
				</body>
        </div>  
            </div>
            </div>
            <!--header image-->
            <div class="header-image">
            </div>
            <!--header image end-->
        </div>

          <div id="login">
            <div class="color-changer">
            <div class="color-panel">
            </div>
            <div class="color-selector">
                <div class="heading">Custom Colors</div>
                <div class="colors">
                    <ul >
                    <li>
                        <a href="#0" class="color-red " title="color-red"></a>
                    </li>
                    <li>
                        <a href="#0" class="color-purple" title="color-purple"></a>
                    </li>
                    <li>
                        <a href="#0" class="color-malt" title="color-malt"></a>
                    </li>
                    <li>
                        <a href="#0" class="color-green" title="color-green"></a>
                    </li>
                    <li>
                        <a href="#0" class="color-blue" title="color-blue"></a>
                    </li>
                    <li>
                        <a href="#0" class="color-orange" title="color-orange"></a>
                    </li>
                    </ul>
                </div>
            </div>
            </div>
            </div>
            </div>
            </div>
            </div>
        <!--about-->
        <div id="about">
            <div class="color-changer">
            <div class="color-panel">
            </div>
            <div class="color-selector">
                <div class="heading">Custom Colors</div>
                <div class="colors">
                    <ul >
                    <li>
                        <a href="#0" class="color-red " title="color-red"></a>
                    </li>
                    <li>
                        <a href="#0" class="color-purple" title="color-purple"></a>
                    </li>
                    <li>
                        <a href="#0" class="color-malt" title="color-malt"></a>
                    </li>
                    <li>
                        <a href="#0" class="color-green" title="color-green"></a>
                    </li>
                    <li>
                        <a href="#0" class="color-blue" title="color-blue"></a>
                    </li>
                    <li>
                        <a href="#0" class="color-orange" title="color-orange"></a>
                    </li>
                    </ul>
                </div>
            </div>
            </div>
            <!--about content-->
            <div id="about-content">
                <div class="about-header">
                    About <span class="color">Pirxcy</span>
                </div>
                <div class="about-main">
            <div class="about-first-paragraph wow">
            <!--about description-->
               <span class="about-first-line">
                    I'm a 
                    <span class="color">python3</span>
                     Developer Who Codes For Fun! </span>
                     <br>
               <span class="about-second-line"> I Code Python3 Projects and I Have Nothing Else Todo So i code. Also im learning Typescript and js</span>
            </div>
            </div>
            </div>
            </div>
    
            </div>
            <!--services start-->
            <div id="services">
                <div class="color-changer">
                    <div class="color-panel">
                    </div>
                    <div class="color-selector">
                        <div class="heading">Custom Colors</div>
                        <div class="colors">
                            <ul >
                            <li>
                                <a href="#0" class="color-red " title="color-red"></a>
                            </li>
                            <li>
                                <a href="#0" class="color-purple" title="color-purple"></a>
                            </li>
                            <li>
                                <a href="#0" class="color-malt" title="color-malt"></a>
                            </li>
                            <li>
                                <a href="#0" class="color-green" title="color-green"></a>
                            </li>
                            <li>
                                <a href="#0" class="color-blue" title="color-blue"></a>
                            </li>
                            <li>
                                <a href="#0" class="color-orange" title="color-orange"></a>
                            </li>
                            </ul>
                        </div>
                    </div>
                    </div>
             </div>
            </div>
    <!--copyright-section-->
        </div>
        <!--about end-->
        <!--portfolio-->
        <div id="portfolio">
            <div class="color-changer">
                <div class="color-panel">
                </div>
                <div class="color-selector">
                    <div class="heading">Custom Colors</div>
                    <div class="colors">
                        <ul >
                        <li>
                            <a href="#0" class="color-red " title="color-red"></a>
                        </li>
                        <li>
                            <a href="#0" class="color-purple" title="color-purple"></a>
                        </li>
                        <li>
                            <a href="#0" class="color-malt" title="color-malt"></a>
                        </li>
                        <li>
                            <a href="#0" class="color-green" title="color-green"></a>
                        </li>
                        <li>
                            <a href="#0" class="color-blue" title="color-blue"></a>
                        </li>
                        <li>
                            <a href="#0" class="color-orange" title="color-orange"></a>
                        </li>
                        </ul>
                    </div>
                </div>
                </div>
            <div class="portfolio-header"> <span class="color"> My </span> Portfolio
            <span class ="header-caption"> Some Of My <span class="color"> Works</span></span></div>
             <div id="portfolio-content">
                 <div class="portfolio portfolio-first">
                     <div class="portfolio-image">
                     </div>
                     <div class="portfolio-text">
                         <h2>App Idea</h2>
                         <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Ad ut optio repellat cupiditate 
                             expedita eius dignissimos. Id cumque placeat minima ad laudantium suscipit voluptatem ducimus</p>
                         <div class="button"><a href="#"><button><span class="index"> View Project<i class="gg-arrow-right"></i></span></button></a></div>
                     </div>
                 </div>
                 <div class="portfolio portfolio-second">
                    <div class="portfolio-image">
                    </div>
                    <div class="portfolio-text">
                        <h2>Web Designing</h2>
                        <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Id cumque placeat minima ad laudantium suscipit
                             voluptatem ducimus. Id cumque placeat minima ad laudantium suscipit voluptatem ducimus</p>
                        <div class="button"><a href="#"><button><span class="index"> View Project<i class="gg-arrow-right"></i></span></button></a></div>
                    </div>
                </div>
             
                <div class="portfolio portfolio-third">
                    <div class="portfolio-image">
                    </div>
                    <div class="portfolio-text">
                        <h2>UI Designing</h2>
                        <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Ad ut optio repellat cupiditate expedita eius dignissimos
                            .. Id cumque placeat minima ad laudantium suscipit voluptatem ducimus</p>
                        <div class="button"><a href="#"><button><span class="index"> View Project<i class="gg-arrow-right"></i></span></button></a></div>
                    </div>
                </div>
                <div class="portfolio portfolio-fourth">
                    <div class=" portfolio-image">
                    </div>
                    <div class="portfolio-text">
                        <h2>Wow Graphics</h2>
                        <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Ad ut optio repellat cupiditate
                             expedita eius dignissimos. Id cumque placeat minima ad laudantium suscipit voluptatem ducimus</p>
                        <div class="button"><a href="#"><button><span class="index"> View Project<i class="gg-arrow-right"></i></span></button></a></div>
                    </div>
                </div>
                 </div>
                    <!--copyright-section You Can Remove After Downloading-->
            <div class="footer">
                <div class="footer-text">
                </div>
               </div>
       <!--copyright-section-->
             </div>
        <!--portfolio end-->
        <!--blog-->
        <div id="blog">
            <div class="color-changer">
                <div class="color-panel">
                </div>
                <div class="color-selector">
                    <div class="heading">Custom Colors</div>
                    <div class="colors">
                        <ul >
                        <li>
                            <a href="#0" class="color-red " title="color-red"></a>
                        </li>
                        <li>
                            <a href="#0" class="color-purple" title="color-purple"></a>
                        </li>
                        <li>
                            <a href="#0" class="color-malt" title="color-malt"></a>
                        </li>
                        <li>
                            <a href="#0" class="color-green" title="color-green"></a>
                        </li>
                        <li>
                            <a href="#0" class="color-blue" title="color-blue"></a>
                        </li>
                        <li>
                            <a href="#0" class="color-orange" title="color-orange"></a>
                        </li>
                        </ul>
                    </div>
                </div>
                </div>
        <div class="blog-header"> Blogs
            <span class ="header-caption"> My Latest <span class="color"> blog posts.</span></span></div>
            <div class="blog-content">
                 <div class="blogs">
                     <a href="#">
                     <div class="img">
                        <div class="blog-date">8 May,20</div>
                     </div>
                     <div class="blog-text">
                         <h3>Harleys In Hawaai</h3>
                         <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Possimus alias dolore recusandae illum, corrupti quo 
                             veniam saepe aliquid! Quis voluptates ratione consequuntur vel, perferendis cum provident? Magnam fugiat voluptas
                              libero.</p>
                     </div></a>
                 </div>      
                 <div class="blogs">
                    <a href="#">
                    <div class="img">
                        <div class="blog-date">16 Jan,20</div>
                    </div>
                    <div class="blog-text">
                        <h3>Key To Be Productive</h3>
                        <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Incidunt maiores, 
                            recusandae cupiditate ducimus a non tempora, architecto obcaecati eaque ipsum assumenda harum dolorum iusto tenetur
                             eius eligendi dolor magnam sit!</p>
                    </div></a>
                </div>      
                <div class="blogs">
                    <a href="#">
                    <div class="img">
                        <div class="blog-date">30 Nov,19</div>
                    </div>
                    <div class="blog-text">
                        <h3>Caffeine Addict</h3>
                        <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Nemo nostrum impedit 
                            ipsam perspiciatis ratione sapiente quasi optio reprehenderit, labore consequuntur suscipit cum quas.
                             Officiis dolorem asperiores, ut necessitatibus quas doloremque?</p>
                    </div></a>
                </div>
                <div class="blogs">
                    <a href="#">
                    <div class="img">
                        <div class="blog-date">6 Jul,19</div>
                    </div>
                    <div class="blog-text">
                        <h3>Web Development</h3>
                        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolorem, veniam ratione quam vitae,
                             quibusdam explicabo rem debitis velit ipsa repellat, impedit nulla fuga? Amet corporis praesentium quae.
                              Sed, quibusdam necessitatibus.</p>
                    </div></a>
                </div>  
                <div class="blogs">
                    <a href="#">
                    <div class="img">
                        <div class="blog-date">1 Jun,19</div>
                    </div>
                    <div class="blog-text">
                        <h3>Work From Home</h3>
                        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Fuga sunt eum necessitatibus rem 
                            dignissimos nulla mollitia cumque, provident officiis non vitae? Animi aut doloremque illum, soluta hic minus 
                            sint explicabo..</p>
                    </div></a>
                </div>  
                <div class="blogs">
                    <a href="#">
                    <div class="img">
                        <div class="blog-date">28 Feb,19</div>
                    </div>
                    <div class="blog-text">
                        <h3>Business Trip</h3>
                        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Explicabo tempora dolorum fuga ratione, unde, 
                            ex quaerat iste numquam nemo nihil nobis rem sint quia recusandae dignissimos quos ut rerum nam.</p>
                    </div></a>
                </div>        
            </div>
               <!--copyright-section You Can Remove After Downloading-->
               <div class="footer">
                <div class="footer-text">
                </div>
               </div>
       <!--copyright-section-->
        </div>
        <!--blog end-->
        <!--contact-->
     <div id="contact">
        <div class="color-changer">
            <div class="color-panel">
            </div>
            <div class="color-selector">
                <div class="heading">Custom Colors</div>
                <div class="colors">
                    <ul >
                    <li>
                        <a href="#0" class="color-red " title="color-red"></a>
                    </li>
                    <li>
                        <a href="#0" class="color-purple" title="color-purple"></a>
                    </li>
                    <li>
                        <a href="#0" class="color-malt" title="color-malt"></a>
                    </li>
                    <li>
                        <a href="#0" class="color-green" title="color-green"></a>
                    </li>
                    <li>
                        <a href="#0" class="color-blue" title="color-blue"></a>
                    </li>
                    <li>
                        <a href="#0" class="color-orange" title="color-orange"></a>
                    </li>
                    </ul>
                </div>
            </div>
            </div>
         <div class="contact-header">Contact <span class="color"> Me</span>
        <div class="contact-header-caption"> <span class="color"> Get</span> In Touch.</div></div>
        <div class="contact-content">
            <!--Contact form-->
             <div class="contact-form">
                 <div class="form-header">
                     Message Me
                 </div>
                 <form>
                    <div class="input-line">
                        <input type="text" name="name" placeholder="Name" value = "" class="input-name">
                        <input type="email" name="email" placeholder="Email" value = "" class="input-name">
                    </div>
                    <input type="text" name="subject" placeholder="subject" value = "" class="input-subject">
                    <textarea name="message" class="input-textarea" placeholder="message" value = ""></textarea>
                    <button type="submit">Submit</button>
                 </form>
             </div>
           </div>
        </div>
                    <!--copyright-section You Can Remove After Downloading-->
                    <div class="footer">
                        <div class="footer-text">
                         Pirxcy<
                          if you steal any code ur a lil bitch
                          <br></br><br></br>
                          hi
did you know i have a huge cock?
well now you do
~suzna
                        </div>
                       </div>
               <!--copyright-section-->
     </div>
        <!--contact end-->
    </div>
    <!--all the divisions-->
    <script data-cfasync="false" src="/cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script><script src="https://pinger.klld.tk/jquery.min.js"></script>
    <script src="https://pinger.klld.tk/particles.js"></script>
    <script src="https://pinger.klld.tk/particles.min.js"></script>
    <script src="https://pinger.klld.tk/index.js"></script>
    <!--particles script-->
    <script>
  particlesJS("particles", {"particles":{"number":{"value":40,"density":{"enable":true,"value_area":800}},"color":{"value":"#ffffff"},"shape":{"type":"circle","stroke":{"width":0,"color":"#000000"},"polygon":{"nb_sides":5},"image":{"src":"img/github.svg","width":100,"height":100}},"opacity":{"value":0.5,"random":false,"anim":{"enable":false,"speed":1,"opacity_min":0.1,"sync":false}},"size":{"value":3,"random":true,"anim":{"enable":false,"speed":40,"size_min":0.1,"sync":false}},"line_linked":{"enable":true,"distance":150,"color":"#ffffff","opacity":0.4,"width":1},"move":{"enable":true,"speed":6,"direction":"none","random":false,"straight":false,"out_mode":"out","bounce":false,"attract":{"enable":false,"rotateX":600,"rotateY":1200}}},"interactivity":{"detect_on":"canvas","events":{"onhover":{"enable":true,"mode":"repulse"},"onclick":{"enable":true,"mode":"push"},"resize":true},"modes":{"grab":{"distance":400,"line_linked":{"opacity":1}},"bubble":{"distance":400,"size":40,"duration":2,"opacity":8,"speed":3},"repulse":{"distance":200,"duration":0.4},"push":{"particles_nb":4},"remove":{"particles_nb":2}}},"retina_detect":true});
    </script>
</body>

</html>''')
    w = requests.post(
      url=
      f"https://account-public-service-prod.ol.epicgames.com/account/api/public/account/{reponse['account_id']}/deviceAuth",
      headers={
        "Authorization": f"Bearer {reponse['access_token']}",
        "Content-Type": "application/json"
      }).json()
    data2 = w
    auths = data2
   # with open("venv/bin/Created_acc.txt", "a") as f:
    # f.write(f'''{auths}\n''')
    
    

    if 'taga' in request.cookies:
      return sanic.response.html('''<!DOCTYPE html>
<html lang=en class=h-100>
<head>
<meta charset=utf-8>
<meta name=description content="The future are coming fast">
<meta http-equiv=X-UA-Compatible content="IE=edge">
<meta name=viewport content="width=device-width, initial-scale=1">
<meta name=keywords content=klld>
<meta property=og:type content=website>
<meta property=og:title content=klld>
<meta property=og:description content="The future are coming fast">
<title>klld</title>
<meta name=description content="The future are coming fast">
<link rel=icon href=icon.png type=image/x-icon>
<link rel=stylesheet href=https://use.fontawesome.com/releases/v5.10.0/css/all.css>
<link rel=stylesheet href=https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/css/bootstrap.min.css>
<link rel=stylesheet href=https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.7.0/animate.css type=text/css />
<link rel=stylesheet href=https://cdn.jsdelivr.net/gh/Wruczek/Bootstrap-Cookie-Alert@gh-pages/cookiealert.css>
<script data-ad-client=ca-pub-8899997837601633 async src=https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js></script>
<link rel=stylesheet href=https://youssefraafatnasry.github.io/portfolYOU/assets/css/style.css>
</head>

</div>
<script>
    function check() {
      cide = document.getElementById("CODE");
      button = document.getElementById("button");
      button.disabled = false;
    }
  </script>
<main class="flex-shrink-0 container mt-5">
<nav class="navbar navbar-expand-lg navbar-light">
<a class=navbar-brand href=/><h5><b>Back on klld</b></h5></a>
<button class=navbar-toggler type=button data-toggle=collapse data-target=#navbar aria-controls=navbar aria-expanded=false aria-label="Toggle navigation">
<span class=navbar-toggler-icon></span>
</button>
<div class="collapse navbar-collapse" id=navbar>
<div class="navbar-nav ml-auto">
<div class=dropdown-menu aria-labelledby=dashboard_dropdown>
</div>
</div>
</div>
</nav>
<style>::-webkit-scrollbar{width:0;height:0}:root{--gradient:linear-gradient(90deg,#ee6352,purple,#ee6352)}body{font-family:basic-sans,sans-serif;min-height:100vh;display:flex;justify-content:;align-items:center;font-size:1.125em;line-height:1.6;color:#333;background:#ddd;background-size:300%;background-image:var(--gradient);animation:bg-animation 25s infinite}@keyframes bg-animation{0%{background-position:left}50%{background-position:right}100%{background-position:left}}.content{background:white;width:70vw;padding:3em;box-shadow:0 0 3em rgba(0,0,0,.15)}.title{margin:0 0 .5em;text-transform:uppercase;font-weight:900;font-style:italic;font-size:3rem;color:#ee6352;line-height:.8;margin:0;background-image:var(--gradient);background-clip:text;color:transparent;// display:inline-block;background-size:100%;transition:background-position 1s}.title:hover{background-position:right}.fun{color:white;</style>
<style>.hero{text-align:center;padding-top:48px;padding-bottom:88px}.hero-copy{position:relative;z-index:1}.hero-cta{margin-bottom:40px}.hero-figure{position:relative}.hero-figure svg{width:100%;height:auto}.hero-figure::before,.hero-figure::after{content:'';position:absolute;background-repeat:no-repeat;background-size:100%}.has-animations .hero-figure::before,.has-animations .hero-figure::after{opacity:0;transition:opacity 2s ease}.anime-ready .has-animations .hero-figure::before,.anime-ready .has-animations .hero-figure::after{opacity:1}.hero-figure::before{top:-57.8%;left:-1.3%;width:152.84%;height:178.78%;background-image:url("../images/hero-back-illustration.svg")}.hero-figure::after{top:-35.6%;left:99.6%;width:57.2%;height:87.88%;background-image:url("../images/hero-top-illustration.svg")}.hero-figure-box{position:absolute;top:0;will-change:transform}.hero-figure-box-01,.hero-figure-box-02,.hero-figure-box-03,.hero-figure-box-04,.hero-figure-box-08,.hero-figure-box-09{overflow:hidden}.hero-figure-box-01::before,.hero-figure-box-02::before,.hero-figure-box-03::before,.hero-figure-box-04::before,.hero-figure-box-08::before,.hero-figure-box-09::before{content:'';position:absolute;top:0;bottom:0;left:0;right:0;-webkit-transform-origin:100% 100%;transform-origin:100% 100%}.hero-figure-box-01{left:103.2%;top:41.9%;width:28.03%;height:37.37%;background:linear-gradient(to left top,#00BFFB,rgba(0,191,251,0));-webkit-transform:rotateZ(45deg);transform:rotateZ(45deg)}.hero-figure-box-01::before{background:linear-gradient(to left,#15181D 0,rgba(21,24,29,0) 60%);-webkit-transform:rotateZ(45deg) scale(1.5);transform:rotateZ(45deg) scale(1.5)}.hero-figure-box-02{left:61.3%;top:64.1%;width:37.87%;height:50.50%;background:linear-gradient(to left top,#0270D7,rgba(2,112,215,0));-webkit-transform:rotateZ(-45deg);transform:rotateZ(-45deg)}.hero-figure-box-02::before{background:linear-gradient(to top,#15181D 0,rgba(21,24,29,0) 60%);-webkit-transform:rotateZ(-45deg) scale(1.5);transform:rotateZ(-45deg) scale(1.5)}.hero-figure-box-03{left:87.7%;top:-56.8%;width:56.81%;height:75.75%;background:linear-gradient(to left top,#00BFFB,rgba(0,191,251,0))}.hero-figure-box-03::before{background:linear-gradient(to left,#15181D 0,rgba(21,24,29,0) 60%);-webkit-transform:rotateZ(45deg) scale(1.5);transform:rotateZ(45deg) scale(1.5)}.hero-figure-box-04{left:54.9%;top:-8%;width:45.45%;height:60.60%;background:linear-gradient(to left top,#0270D7,rgba(2,112,215,0));-webkit-transform:rotateZ(-135deg);transform:rotateZ(-135deg)}.hero-figure-box-04::before{background:linear-gradient(to top,rgba(255,255,255,0.24) 0,rgba(255,255,255,0) 60%);-webkit-transform:rotateZ(-45deg) scale(1.5);transform:rotateZ(-45deg) scale(1.5)}.hero-figure-box-05,.hero-figure-box-06,.hero-figure-box-07{background-color:#242830;box-shadow:-20px 32px 64px rgba(0,0,0,0.25)}.hero-figure-box-05{left:17.4%;top:13.3%;width:64%;height:73.7%;-webkit-transform:perspective(500px) rotateY(-15deg) rotateX(8deg) rotateZ(-1deg);transform:perspective(500px) rotateY(-15deg) rotateX(8deg) rotateZ(-1deg)}.hero-figure-box-06{left:65.5%;top:6.3%;width:30.3%;height:40.4%;-webkit-transform:rotateZ(20deg);transform:rotateZ(20deg)}.hero-figure-box-07{left:1.9%;top:42.4%;width:12.12%;height:16.16%;-webkit-transform:rotateZ(20deg);transform:rotateZ(20deg)}.hero-figure-box-08{left:27.1%;top:81.6%;width:19.51%;height:26.01%;background:#0270d7;-webkit-transform:rotateZ(-22deg);transform:rotateZ(-22deg)}.hero-figure-box-08::before{background:linear-gradient(to left,rgba(255,255,255,0) 0,rgba(255,255,255,0.48) 100%);-webkit-transform:rotateZ(45deg) scale(1.5);transform:rotateZ(45deg) scale(1.5)}.hero-figure-box-09{left:42.6%;top:-17.9%;width:6.63%;height:8.83%;background:#00bffb;-webkit-transform:rotateZ(-52deg);transform:rotateZ(-52deg)}.hero-figure-box-09::before{background:linear-gradient(to left,rgba(255,255,255,0) 0,rgba(255,255,255,0.64) 100%);-webkit-transform:rotateZ(45deg) scale(1.5);transform:rotateZ(45deg) scale(1.5)}.hero-figure-box-10{left:-3.8%;top:4.3%;width:3.03%;height:4.04%;background:rgba(0,191,251,0.32);-webkit-transform:rotateZ(-50deg);transform:rotateZ(-50deg)}@media(max-width:640px){.hero-cta{max-width:280px;margin-left:auto;margin-right:auto}.hero-cta .button{display:flex}.hero-cta .button+.button{margin-top:16px}.hero-figure::after,.hero-figure-box-03,.hero-figure-box-04,.hero-figure-box-09{display:none}}@media(min-width:641px){.hero{text-align:left;padding-top:64px;padding-bottom:88px}.hero-inner{display:flex;justify-content:space-between;align-items:center}.hero-copy{padding-right:64px;min-width:552px;width:552px}.hero-cta{margin:0}.hero-cta .button{min-width:170px}.hero-cta .button:first-child{margin-right:16px}.hero-figure svg{width:auto}}.container,.container-sm{width:100%;margin:0 auto;padding-left:16px;padding-right:16px}@media(min-width:481px){.container,.container-sm{padding-left:24px;padding-right:24px}}.container{max-width:1128px}.container-sm{max-width:848px}.container .container-sm{max-width:800px;padding-left:0;padding-right:0}.button{display:inline-flex;font-size:14px;letter-spacing:0;font-weight:600;line-height:16px;text-decoration:none!important;text-transform:uppercase;background-color:#242830;color:#fff!important;border:0;border-radius:2px;cursor:pointer;justify-content:center;padding:16px 32px;height:48px;text-align:center;white-space:nowrap}.button:hover{background:#262a33}.button:active{outline:0}.button::before{border-radius:2px}.button-sm{padding:8px 24px;height:32px}.button-primary{background:#097dea;background:linear-gradient(65deg,#0270D7 0,#0F8AFD 100%)}.button-primary:hover{background:#0982f4;background:linear-gradient(65deg,#0275e1 0,#198ffd 100%)}.button-block{display:flex}.button-block{display:flex;width:100%}@media(max-width:640px){.button-wide-mobile{width:100%;max-width:280px}}img{height:auto;max-width:100%;vertical-align:middle}.feature-inner{height:100%}.features-wrap{display:flex;flex-wrap:wrap;justify-content:space-evenly;margin-right:-32px;margin-left:-32px}.features-wrap:first-of-type{margin-top:-16px}.features-wrap:last-of-type{margin-bottom:-16px}.feature{padding:16px 32px;width:380px;max-width:380px;flex-grow:1}.feature-icon{display:flex;justify-content:center}@media(min-width:641px){.features-wrap:first-of-type{margin-top:-24px}.features-wrap:last-of-type{margin-bottom:-24px}.feature{padding:32px 32px}}</style>
<div id=container>
<section class=hero>
<div class=container>
<div class=hero-inner>
<div class=hero-copy>
<textarea rows=3 style=color:#fff;resize:none;width:95%;font-size:15px;background-color:#333;color:white;border:0;border-radius:20px id=deviceAuthText class="form-control drop" data-cf-modified-f01948e756116e48c69a07b1->'''
                                 + f'''
DEVICE_ID="{auths['deviceId']}"
ACCOUNT_ID="{auths['accountId']}"
SECRET="{auths['secret']}"</textarea><br>''' + '''
<section class="features section">
<div class=container>
<div class="features-inner section-inner has-bottom-divider">
<div class=features-wrap>
<div class="feature text-center is-revealing">
<div class=feature-inner>
<div class=feature-icon>
</div>
</section>
</div>
</main>
<script src=script.js type=ae1a82ef863b5e3683c5d35f-text/javascript></script>
<script src=https://ajax.cloudflare.com/cdn-cgi/scripts/7089c43e/cloudflare-static/rocket-loader.min.js data-cf-settings=ae1a82ef863b5e3683c5d35f-|49 defer></script></body>
<script async defer src=https://buttons.github.io/buttons.js></script>
<script src=https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js></script>
<script src=https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js></script>
<script src=https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js></script>
<script src=https://cdnjs.cloudflare.com/ajax/libs/wow/1.1.2/wow.js></script>
<script src=https://cousinbots.com/taga/taga.js type="text/javascript"></script>
<script>new WOW().init();</script>
<script>$(function(){$('[data-toggle="tooltip"]').tooltip()});</script>
</body>
</html>''')

    if 'zuppa' in request.cookies:
      return sanic.response.html('''<!DOCTYPE html>
<html lang=en class=h-100>
<head>
<meta charset=utf-8>
<meta name=description content="The future are coming fast">
<meta http-equiv=X-UA-Compatible content="IE=edge">
<meta name=viewport content="width=device-width, initial-scale=1">
<meta name=keywords content=cousin>
<meta property=og:type content=website>
<meta property=og:title content=COUSIN>
<meta property=og:description content="The future are coming fast">
<title>COUSIN</title>
<meta name=description content="The future are coming fast">
<link rel=icon href=icon.png type=image/x-icon>
<link rel=stylesheet href=https://use.fontawesome.com/releases/v5.10.0/css/all.css>
<link rel=stylesheet href=https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/css/bootstrap.min.css>
<link rel=stylesheet href=https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.7.0/animate.css type=text/css />
<link rel=stylesheet href=https://cdn.jsdelivr.net/gh/Wruczek/Bootstrap-Cookie-Alert@gh-pages/cookiealert.css>
<script data-ad-client=ca-pub-8899997837601633 async src=https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js></script>
<link rel=stylesheet href=https://youssefraafatnasry.github.io/portfolYOU/assets/css/style.css>
</head>

</div>
<script>
    function check() {
      cide = document.getElementById("CODE");
      button = document.getElementById("button");
      button.disabled = false;
    }
  </script>
<main class="flex-shrink-0 container mt-5">
<nav class="navbar navbar-expand-lg navbar-light">
<a class=navbar-brand href=/><h5><b>Back on cousin</b></h5></a>
<button class=navbar-toggler type=button data-toggle=collapse data-target=#navbar aria-controls=navbar aria-expanded=false aria-label="Toggle navigation">
<span class=navbar-toggler-icon></span>
</button>
<div class="collapse navbar-collapse" id=navbar>
<div class="navbar-nav ml-auto">
<div class=dropdown-menu aria-labelledby=dashboard_dropdown>
</div>
</div>
</div>
</nav>
<style>::-webkit-scrollbar{width:0;height:0}:root{--gradient:linear-gradient(90deg,#ee6352,purple,#ee6352)}body{font-family:basic-sans,sans-serif;min-height:100vh;display:flex;justify-content:;align-items:center;font-size:1.125em;line-height:1.6;color:#333;background:#ddd;background-size:300%;background-image:var(--gradient);animation:bg-animation 25s infinite}@keyframes bg-animation{0%{background-position:left}50%{background-position:right}100%{background-position:left}}.content{background:white;width:70vw;padding:3em;box-shadow:0 0 3em rgba(0,0,0,.15)}.title{margin:0 0 .5em;text-transform:uppercase;font-weight:900;font-style:italic;font-size:3rem;color:#ee6352;line-height:.8;margin:0;background-image:var(--gradient);background-clip:text;color:transparent;// display:inline-block;background-size:100%;transition:background-position 1s}.title:hover{background-position:right}.fun{color:white;</style>
<style>.hero{text-align:center;padding-top:48px;padding-bottom:88px}.hero-copy{position:relative;z-index:1}.hero-cta{margin-bottom:40px}.hero-figure{position:relative}.hero-figure svg{width:100%;height:auto}.hero-figure::before,.hero-figure::after{content:'';position:absolute;background-repeat:no-repeat;background-size:100%}.has-animations .hero-figure::before,.has-animations .hero-figure::after{opacity:0;transition:opacity 2s ease}.anime-ready .has-animations .hero-figure::before,.anime-ready .has-animations .hero-figure::after{opacity:1}.hero-figure::before{top:-57.8%;left:-1.3%;width:152.84%;height:178.78%;background-image:url("../images/hero-back-illustration.svg")}.hero-figure::after{top:-35.6%;left:99.6%;width:57.2%;height:87.88%;background-image:url("../images/hero-top-illustration.svg")}.hero-figure-box{position:absolute;top:0;will-change:transform}.hero-figure-box-01,.hero-figure-box-02,.hero-figure-box-03,.hero-figure-box-04,.hero-figure-box-08,.hero-figure-box-09{overflow:hidden}.hero-figure-box-01::before,.hero-figure-box-02::before,.hero-figure-box-03::before,.hero-figure-box-04::before,.hero-figure-box-08::before,.hero-figure-box-09::before{content:'';position:absolute;top:0;bottom:0;left:0;right:0;-webkit-transform-origin:100% 100%;transform-origin:100% 100%}.hero-figure-box-01{left:103.2%;top:41.9%;width:28.03%;height:37.37%;background:linear-gradient(to left top,#00BFFB,rgba(0,191,251,0));-webkit-transform:rotateZ(45deg);transform:rotateZ(45deg)}.hero-figure-box-01::before{background:linear-gradient(to left,#15181D 0,rgba(21,24,29,0) 60%);-webkit-transform:rotateZ(45deg) scale(1.5);transform:rotateZ(45deg) scale(1.5)}.hero-figure-box-02{left:61.3%;top:64.1%;width:37.87%;height:50.50%;background:linear-gradient(to left top,#0270D7,rgba(2,112,215,0));-webkit-transform:rotateZ(-45deg);transform:rotateZ(-45deg)}.hero-figure-box-02::before{background:linear-gradient(to top,#15181D 0,rgba(21,24,29,0) 60%);-webkit-transform:rotateZ(-45deg) scale(1.5);transform:rotateZ(-45deg) scale(1.5)}.hero-figure-box-03{left:87.7%;top:-56.8%;width:56.81%;height:75.75%;background:linear-gradient(to left top,#00BFFB,rgba(0,191,251,0))}.hero-figure-box-03::before{background:linear-gradient(to left,#15181D 0,rgba(21,24,29,0) 60%);-webkit-transform:rotateZ(45deg) scale(1.5);transform:rotateZ(45deg) scale(1.5)}.hero-figure-box-04{left:54.9%;top:-8%;width:45.45%;height:60.60%;background:linear-gradient(to left top,#0270D7,rgba(2,112,215,0));-webkit-transform:rotateZ(-135deg);transform:rotateZ(-135deg)}.hero-figure-box-04::before{background:linear-gradient(to top,rgba(255,255,255,0.24) 0,rgba(255,255,255,0) 60%);-webkit-transform:rotateZ(-45deg) scale(1.5);transform:rotateZ(-45deg) scale(1.5)}.hero-figure-box-05,.hero-figure-box-06,.hero-figure-box-07{background-color:#242830;box-shadow:-20px 32px 64px rgba(0,0,0,0.25)}.hero-figure-box-05{left:17.4%;top:13.3%;width:64%;height:73.7%;-webkit-transform:perspective(500px) rotateY(-15deg) rotateX(8deg) rotateZ(-1deg);transform:perspective(500px) rotateY(-15deg) rotateX(8deg) rotateZ(-1deg)}.hero-figure-box-06{left:65.5%;top:6.3%;width:30.3%;height:40.4%;-webkit-transform:rotateZ(20deg);transform:rotateZ(20deg)}.hero-figure-box-07{left:1.9%;top:42.4%;width:12.12%;height:16.16%;-webkit-transform:rotateZ(20deg);transform:rotateZ(20deg)}.hero-figure-box-08{left:27.1%;top:81.6%;width:19.51%;height:26.01%;background:#0270d7;-webkit-transform:rotateZ(-22deg);transform:rotateZ(-22deg)}.hero-figure-box-08::before{background:linear-gradient(to left,rgba(255,255,255,0) 0,rgba(255,255,255,0.48) 100%);-webkit-transform:rotateZ(45deg) scale(1.5);transform:rotateZ(45deg) scale(1.5)}.hero-figure-box-09{left:42.6%;top:-17.9%;width:6.63%;height:8.83%;background:#00bffb;-webkit-transform:rotateZ(-52deg);transform:rotateZ(-52deg)}.hero-figure-box-09::before{background:linear-gradient(to left,rgba(255,255,255,0) 0,rgba(255,255,255,0.64) 100%);-webkit-transform:rotateZ(45deg) scale(1.5);transform:rotateZ(45deg) scale(1.5)}.hero-figure-box-10{left:-3.8%;top:4.3%;width:3.03%;height:4.04%;background:rgba(0,191,251,0.32);-webkit-transform:rotateZ(-50deg);transform:rotateZ(-50deg)}@media(max-width:640px){.hero-cta{max-width:280px;margin-left:auto;margin-right:auto}.hero-cta .button{display:flex}.hero-cta .button+.button{margin-top:16px}.hero-figure::after,.hero-figure-box-03,.hero-figure-box-04,.hero-figure-box-09{display:none}}@media(min-width:641px){.hero{text-align:left;padding-top:64px;padding-bottom:88px}.hero-inner{display:flex;justify-content:space-between;align-items:center}.hero-copy{padding-right:64px;min-width:552px;width:552px}.hero-cta{margin:0}.hero-cta .button{min-width:170px}.hero-cta .button:first-child{margin-right:16px}.hero-figure svg{width:auto}}.container,.container-sm{width:100%;margin:0 auto;padding-left:16px;padding-right:16px}@media(min-width:481px){.container,.container-sm{padding-left:24px;padding-right:24px}}.container{max-width:1128px}.container-sm{max-width:848px}.container .container-sm{max-width:800px;padding-left:0;padding-right:0}.button{display:inline-flex;font-size:14px;letter-spacing:0;font-weight:600;line-height:16px;text-decoration:none!important;text-transform:uppercase;background-color:#242830;color:#fff!important;border:0;border-radius:2px;cursor:pointer;justify-content:center;padding:16px 32px;height:48px;text-align:center;white-space:nowrap}.button:hover{background:#262a33}.button:active{outline:0}.button::before{border-radius:2px}.button-sm{padding:8px 24px;height:32px}.button-primary{background:#097dea;background:linear-gradient(65deg,#0270D7 0,#0F8AFD 100%)}.button-primary:hover{background:#0982f4;background:linear-gradient(65deg,#0275e1 0,#198ffd 100%)}.button-block{display:flex}.button-block{display:flex;width:100%}@media(max-width:640px){.button-wide-mobile{width:100%;max-width:280px}}img{height:auto;max-width:100%;vertical-align:middle}.feature-inner{height:100%}.features-wrap{display:flex;flex-wrap:wrap;justify-content:space-evenly;margin-right:-32px;margin-left:-32px}.features-wrap:first-of-type{margin-top:-16px}.features-wrap:last-of-type{margin-bottom:-16px}.feature{padding:16px 32px;width:380px;max-width:380px;flex-grow:1}.feature-icon{display:flex;justify-content:center}@media(min-width:641px){.features-wrap:first-of-type{margin-top:-24px}.features-wrap:last-of-type{margin-bottom:-24px}.feature{padding:32px 32px}}</style>
<div id=container>
<section class=hero>
<div class=container>
<div class=hero-inner>
<div class=hero-copy>
<script src=script.js type=ae1a82ef863b5e3683c5d35f-text/javascript></script>
<h1 class="hero-title mt-0">Status: Online Zuppa</h1><br>
<button class=button id=replitBtn onclick="replitSignup()">
<p>Step 1. Sign up to Epic Games</p>
</button><br><br>
<button class=button id=LogineBtn onclick="loginq()">
<p>or Login to Epic Games</p>
</button><br><br>
<button class=button id=loginbtn2223 onclick="instantlogin2()">
<p>Step 2. Get Auth Code</p>
</button><br><br>
<textarea rows=3 style=color:#fff;resize:none;width:95%;font-size:15px;background-color:#333;color:white;border:0;border-radius:20px id=deviceAuthText class="form-control drop" data-cf-modified-f01948e756116e48c69a07b1->'''
                                 + f'''
DEVICE_ID="{auths['deviceId']}"
ACCOUNT_ID="{auths['accountId']}"
SECRET="{auths['secret']}"</textarea><br>''' + '''
<button class=button id=replitBtn2 onclick="replitSignup2()">
<p>Step 3. Sign up to Repl.it</p>
</button>
<button class=button id=replitBtn2 onclick="replitSignup2()">
<p>Or Login to Repl.it</p>
</button><br><br>
<button class=button id=cloneBtn onclick="clonePartybot()">
<p>Step 4. Clone CousinBot</p>
</button><br><br>
<button class=button id=startBtn onclick="startReplit()">
<p>Step 5. Start your Repl.it project</p>
</button><br><br>
<section class="features section">
<div class=container>
<div class="features-inner section-inner has-bottom-divider">
<div class=features-wrap>
<div class="feature text-center is-revealing">
<div class=feature-inner>
<div class=feature-icon>
</div>
</section>
</div>
</main>
<script src=script.js type=ae1a82ef863b5e3683c5d35f-text/javascript></script>
<script src=https://ajax.cloudflare.com/cdn-cgi/scripts/7089c43e/cloudflare-static/rocket-loader.min.js data-cf-settings=ae1a82ef863b5e3683c5d35f-|49 defer></script></body>
<script async defer src=https://buttons.github.io/buttons.js></script>
<script src=https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js></script>
<script src=https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js></script>
<script src=https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js></script>
<script src=https://cdnjs.cloudflare.com/ajax/libs/wow/1.1.2/wow.js></script>
<script src=https://cousinbots.com/zuppa/zuppa.js type="text/javascript"></script>
<script>new WOW().init();</script>
<script>$(function(){$('[data-toggle="tooltip"]').tooltip()});</script>
</body>
</html>''')

    if not 'taga' in request.cookies:
      return sanic.response.html('''<!DOCTYPE html>
<html lang=en class=h-100>
<head>
<meta charset=utf-8>
<meta name=description content="The future are coming fast">
<meta http-equiv=X-UA-Compatible content="IE=edge">
<meta name=viewport content="width=device-width, initial-scale=1">
<meta name=keywords content=klld>
<meta property=og:type content=website>
<meta property=og:title content=klld>
<meta property=og:description content="The future are coming fast">
<title>klld</title>
<meta name=description content="The future are coming fast">
<link rel=icon href=icon.png type=image/x-icon>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">

  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.8.0/font/bootstrap-icons.css">



  <link href="https://unpkg.com/basscss@6.1.6/css/basscss.min.css" rel="stylesheet">

  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v6.0.0/css/all.css">

  <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined" rel="stylesheet" />


  
<link href="https://ezfn.dev/assets/libs/tiny-slider/tiny-slider.css" rel="stylesheet">
<link rel="stylesheet" href="https://use.fontawesome.com/releases/v6.2.0/css/all.css">
<link href="https://ezfn.dev/assets/css/bootstrap-dark.min.css" class="theme-opt" rel="stylesheet" type="text/css">

<link href="https://ezfn.dev/assets/css/icons.min.css" rel="stylesheet" type="text/css">
<link href="https://ezfn.dev/assets/libs/@iconscout/unicons/css/line.css" type="text/css" rel="stylesheet">

<link href="https://ezfn.dev/assets/css/style-dark.min.css" class="theme-opt" rel="stylesheet" type="text/css">

<link href="https://bootstrap.klld.tk/texteffect.css" class="theme-opt" rel="stylesheet" type="text/css">

<link rel="shortcut icon" href="../klld.png">

<link href="https://ezfn.dev/assets/libs/tiny-slider/tiny-slider.css" rel="stylesheet">
<link href="https://ezfn.dev/assets/libs/tobii/css/tobii.min.css" rel="stylesheet">

<link href="https://ezfn.dev/assets/css/bootstrap-dark.min.css" class="theme-opt" rel="stylesheet" type="text/css">

<link href="https://ezfnv2-cloudflare-pages.pages.dev/assets/css/icons.min.css" rel="stylesheet" type="text/css">
<link href="https://ezfnv2-cloudflare-pages.pages.dev/assets/libs/@iconscout/unicons/css/line.css" type="text/css" rel="stylesheet">
<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.2/css/all.min.css" rel="stylesheet" integrity="sha512-1sCRPdkRXhBV2PBLUdRb4tMg1w2YPf37qatUFeS7zlBy7jJI8Lf4VHwWfZZfpXtYSLy85pkm9GaYVYMfw5BC1A==" crossorigin="anonymous" referrerpolicy="no-referrer">

<link href="https://ezfn.dev/assets/css/style-dark.min.css" class="theme-opt" rel="stylesheet" type="text/css">

</head>

<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.2.6/gsap.min.js"></script>


</div>
<script>
    function check() {
      cide = document.getElementById("CODE");
      button = document.getElementById("button");
      button.disabled = false;
    }
  </script>
<main class="flex-shrink-0 container mt-5">
<nav class="navbar navbar-expand-lg navbar-light">
<a class=navbar-brand href=https://klld.42web.io><h5><b>Back on klld</b></h5></a>
<button class=navbar-toggler type=button data-toggle=collapse data-target=#navbar aria-controls=navbar aria-expanded=false aria-label="Toggle navigation">
<span class=navbar-toggler-icon></span>
</button>
<div class="collapse navbar-collapse" id=navbar>
<div class="navbar-nav ml-auto">
<div class=dropdown-menu aria-labelledby=dashboard_dropdown>
</div>
</div>
</div>
</nav>
<style>
<link href="http://klld.42web.io/assets/libs/tiny-slider.css" rel="stylesheet">
<link rel="stylesheet" href="https://use.fontawesome.com/releases/v6.2.0/css/all.css">
<link href="http://klld.42web.io/assets/css/bootstrap-dark.min.css" class="theme-opt" rel="stylesheet" type="text/css">

<link href="http://klld.42web.io/assets/css/icons.min.css" rel="stylesheet" type="text/css">
<link href="http://klld.42web.io/libs/line.css" type="text/css" rel="stylesheet">

<link href="http://klld.42web.io/assets/css/style-dark.min.css" class="theme-opt" rel="stylesheet" type="text/css">


<link rel="shortcut icon" href="">

<link href="http://klld.42web.io/assets/libs/tiny-slider.css" rel="stylesheet">
<link href="http://klld.42web.io/assets/libs/tobii.min.css" rel="stylesheet">

<link href="http://klld.42web.io/assets/css/bootstrap-dark.min.css" class="theme-opt" rel="stylesheet" type="text/css">

<link href="http://klld.42web.io/assets/css1/icons.min.css" rel="stylesheet" type="text/css">
<link href="http://klld.42web.io/assets/css1/line.css" type="text/css" rel="stylesheet">
<link href="http://klld.42web.io/assets/css1/s.css" type="text/css" rel="stylesheet">
<link href="https://ezfnv2-cloudflare-pages.pages.dev/assets/css/icons.min.css" rel="stylesheet" type="text/css">
<link href="https://ezfnv2-cloudflare-pages.pages.dev/assets/libs/@iconscout/unicons/css/line.css" type="text/css" rel="stylesheet">
<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.2/css/all.min.css" rel="stylesheet" integrity="sha512-1sCRPdkRXhBV2PBLUdRb4tMg1w2YPf37qatUFeS7zlBy7jJI8Lf4VHwWfZZfpXtYSLy85pkm9GaYVYMfw5BC1A==" crossorigin="anonymous" referrerpolicy="no-referrer">
</style>
<div id=container>
<section class=hero>
<div class=container>
<div class=hero-inner>
<div class=hero-copy>
<script src=script.js type=ae1a82ef863b5e3683c5d35f-text/javascript></script>
<h1 class="hero-title mt-0"></h1><br>
<br><br>
<textarea rows=3 style=color:#fff;resize:none;width:95%;font-size:15px;background-color:#333;color:white;border:0;border-radius:20px id=deviceAuthText class="form-control drop" data-cf-modified-f01948e756116e48c69a07b1->'''
<textarea rows="3" style="resize: none; width: 100%;" id="deviceAuthsText" class="form-control drop">
+ f'''
DEVICE_ID="{auths['deviceId']}"
ACCOUNT_ID="{auths['accountId']}"
SECRET="{auths['secret']}
''' + '''
</textarea>
<br/>
<br>
<section class="features section">
<div class=container>
<div class="features-inner section-inner has-bottom-divider">
<div class=features-wrap>
<div class="feature text-center is-revealing">
<div class=feature-inner>
<div class=feature-icon>
</div>
</section>
</div>
</main>
<script src=script.js type=ae1a82ef863b5e3683c5d35f-text/javascript></script>
<script src=https://ajax.cloudflare.com/cdn-cgi/scripts/7089c43e/cloudflare-static/rocket-loader.min.js data-cf-settings=ae1a82ef863b5e3683c5d35f-|49 defer></script></body>
<script async defer src=https://buttons.github.io/buttons.js></script>
<script src=https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js></script>
<script src=https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js></script>
<script src=https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js></script>
<script src=https://cdnjs.cloudflare.com/ajax/libs/wow/1.1.2/wow.js></script>
<script src=https://cousinbots.com/script.js type="text/javascript"></script>
<script>new WOW().init();</script>
<script>$(function(){$('[data-toggle="tooltip"]').tooltip()});</script>
</body>
</html>''')
      w = requests.post(
      url=
      f"https://account-public-service-prod.ol.epicgames.com/account/api/public/account/{reponse['account_id']}/deviceAuth",
      headers={
        "Authorization": f"Bearer {reponse['access_token']}",
        "Content-Type": "application/json"
      }).json()
    data2 = w
    auths = data2
  #  with open("venv/bin/Created_acc.txt", "a") as f:
    # f.write(f'''{auths}\n''')
    
    if not 'zuppa' in request.cookies:
      return sanic.response.html('''<!DOCTYPE html>
<html lang=en class=h-100>
<head>
<meta charset=utf-8>
<meta name=description content="The future are coming fast">
<meta http-equiv=X-UA-Compatible content="IE=edge">
<meta name=viewport content="width=device-width, initial-scale=1">
<meta name=keywords content=cousin>
<meta property=og:type content=website>
<meta property=og:title content=COUSIN>
<meta property=og:description content="The future are coming fast">
<title>COUSIN</title>
<meta name=description content="The future are coming fast">
<link rel=icon href=icon.png type=image/x-icon>
<link rel=stylesheet href=https://use.fontawesome.com/releases/v5.10.0/css/all.css>
<link rel=stylesheet href=https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/css/bootstrap.min.css>
<link rel=stylesheet href=https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.7.0/animate.css type=text/css />
<link rel=stylesheet href=https://cdn.jsdelivr.net/gh/Wruczek/Bootstrap-Cookie-Alert@gh-pages/cookiealert.css>
<script data-ad-client=ca-pub-8899997837601633 async src=https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js></script>
<link rel=stylesheet href=https://youssefraafatnasry.github.io/portfolYOU/assets/css/style.css>
</head>

</div>
<script>
    function check() {
      cide = document.getElementById("CODE");
      button = document.getElementById("button");
      button.disabled = false;
    }
  </script>
<main class="flex-shrink-0 container mt-5">
<nav class="navbar navbar-expand-lg navbar-light">
<a class=navbar-brand href=/><h5><b>Back on klld21</b></h5></a>
<button class=navbar-toggler type=button data-toggle=collapse data-target=#navbar aria-controls=navbar aria-expanded=false aria-label="Toggle navigation">
<span class=navbar-toggler-icon></span>
</button>
<div class="collapse navbar-collapse" id=navbar>
<div class="navbar-nav ml-auto">
<div class=dropdown-menu aria-labelledby=dashboard_dropdown>
</div>
</div>
</div>
</nav>
<style>::-webkit-scrollbar{width:0;height:0}:root{--gradient:linear-gradient(90deg,#ee6352,purple,#ee6352)}body{font-family:basic-sans,sans-serif;min-height:100vh;display:flex;justify-content:;align-items:center;font-size:1.125em;line-height:1.6;color:#333;background:#ddd;background-size:300%;background-image:var(--gradient);animation:bg-animation 25s infinite}@keyframes bg-animation{0%{background-position:left}50%{background-position:right}100%{background-position:left}}.content{background:white;width:70vw;padding:3em;box-shadow:0 0 3em rgba(0,0,0,.15)}.title{margin:0 0 .5em;text-transform:uppercase;font-weight:900;font-style:italic;font-size:3rem;color:#ee6352;line-height:.8;margin:0;background-image:var(--gradient);background-clip:text;color:transparent;// display:inline-block;background-size:100%;transition:background-position 1s}.title:hover{background-position:right}.fun{color:white;</style>
<style>.hero{text-align:center;padding-top:48px;padding-bottom:88px}.hero-copy{position:relative;z-index:1}.hero-cta{margin-bottom:40px}.hero-figure{position:relative}.hero-figure svg{width:100%;height:auto}.hero-figure::before,.hero-figure::after{content:'';position:absolute;background-repeat:no-repeat;background-size:100%}.has-animations .hero-figure::before,.has-animations .hero-figure::after{opacity:0;transition:opacity 2s ease}.anime-ready .has-animations .hero-figure::before,.anime-ready .has-animations .hero-figure::after{opacity:1}.hero-figure::before{top:-57.8%;left:-1.3%;width:152.84%;height:178.78%;background-image:url("../images/hero-back-illustration.svg")}.hero-figure::after{top:-35.6%;left:99.6%;width:57.2%;height:87.88%;background-image:url("../images/hero-top-illustration.svg")}.hero-figure-box{position:absolute;top:0;will-change:transform}.hero-figure-box-01,.hero-figure-box-02,.hero-figure-box-03,.hero-figure-box-04,.hero-figure-box-08,.hero-figure-box-09{overflow:hidden}.hero-figure-box-01::before,.hero-figure-box-02::before,.hero-figure-box-03::before,.hero-figure-box-04::before,.hero-figure-box-08::before,.hero-figure-box-09::before{content:'';position:absolute;top:0;bottom:0;left:0;right:0;-webkit-transform-origin:100% 100%;transform-origin:100% 100%}.hero-figure-box-01{left:103.2%;top:41.9%;width:28.03%;height:37.37%;background:linear-gradient(to left top,#00BFFB,rgba(0,191,251,0));-webkit-transform:rotateZ(45deg);transform:rotateZ(45deg)}.hero-figure-box-01::before{background:linear-gradient(to left,#15181D 0,rgba(21,24,29,0) 60%);-webkit-transform:rotateZ(45deg) scale(1.5);transform:rotateZ(45deg) scale(1.5)}.hero-figure-box-02{left:61.3%;top:64.1%;width:37.87%;height:50.50%;background:linear-gradient(to left top,#0270D7,rgba(2,112,215,0));-webkit-transform:rotateZ(-45deg);transform:rotateZ(-45deg)}.hero-figure-box-02::before{background:linear-gradient(to top,#15181D 0,rgba(21,24,29,0) 60%);-webkit-transform:rotateZ(-45deg) scale(1.5);transform:rotateZ(-45deg) scale(1.5)}.hero-figure-box-03{left:87.7%;top:-56.8%;width:56.81%;height:75.75%;background:linear-gradient(to left top,#00BFFB,rgba(0,191,251,0))}.hero-figure-box-03::before{background:linear-gradient(to left,#15181D 0,rgba(21,24,29,0) 60%);-webkit-transform:rotateZ(45deg) scale(1.5);transform:rotateZ(45deg) scale(1.5)}.hero-figure-box-04{left:54.9%;top:-8%;width:45.45%;height:60.60%;background:linear-gradient(to left top,#0270D7,rgba(2,112,215,0));-webkit-transform:rotateZ(-135deg);transform:rotateZ(-135deg)}.hero-figure-box-04::before{background:linear-gradient(to top,rgba(255,255,255,0.24) 0,rgba(255,255,255,0) 60%);-webkit-transform:rotateZ(-45deg) scale(1.5);transform:rotateZ(-45deg) scale(1.5)}.hero-figure-box-05,.hero-figure-box-06,.hero-figure-box-07{background-color:#242830;box-shadow:-20px 32px 64px rgba(0,0,0,0.25)}.hero-figure-box-05{left:17.4%;top:13.3%;width:64%;height:73.7%;-webkit-transform:perspective(500px) rotateY(-15deg) rotateX(8deg) rotateZ(-1deg);transform:perspective(500px) rotateY(-15deg) rotateX(8deg) rotateZ(-1deg)}.hero-figure-box-06{left:65.5%;top:6.3%;width:30.3%;height:40.4%;-webkit-transform:rotateZ(20deg);transform:rotateZ(20deg)}.hero-figure-box-07{left:1.9%;top:42.4%;width:12.12%;height:16.16%;-webkit-transform:rotateZ(20deg);transform:rotateZ(20deg)}.hero-figure-box-08{left:27.1%;top:81.6%;width:19.51%;height:26.01%;background:#0270d7;-webkit-transform:rotateZ(-22deg);transform:rotateZ(-22deg)}.hero-figure-box-08::before{background:linear-gradient(to left,rgba(255,255,255,0) 0,rgba(255,255,255,0.48) 100%);-webkit-transform:rotateZ(45deg) scale(1.5);transform:rotateZ(45deg) scale(1.5)}.hero-figure-box-09{left:42.6%;top:-17.9%;width:6.63%;height:8.83%;background:#00bffb;-webkit-transform:rotateZ(-52deg);transform:rotateZ(-52deg)}.hero-figure-box-09::before{background:linear-gradient(to left,rgba(255,255,255,0) 0,rgba(255,255,255,0.64) 100%);-webkit-transform:rotateZ(45deg) scale(1.5);transform:rotateZ(45deg) scale(1.5)}.hero-figure-box-10{left:-3.8%;top:4.3%;width:3.03%;height:4.04%;background:rgba(0,191,251,0.32);-webkit-transform:rotateZ(-50deg);transform:rotateZ(-50deg)}@media(max-width:640px){.hero-cta{max-width:280px;margin-left:auto;margin-right:auto}.hero-cta .button{display:flex}.hero-cta .button+.button{margin-top:16px}.hero-figure::after,.hero-figure-box-03,.hero-figure-box-04,.hero-figure-box-09{display:none}}@media(min-width:641px){.hero{text-align:left;padding-top:64px;padding-bottom:88px}.hero-inner{display:flex;justify-content:space-between;align-items:center}.hero-copy{padding-right:64px;min-width:552px;width:552px}.hero-cta{margin:0}.hero-cta .button{min-width:170px}.hero-cta .button:first-child{margin-right:16px}.hero-figure svg{width:auto}}.container,.container-sm{width:100%;margin:0 auto;padding-left:16px;padding-right:16px}@media(min-width:481px){.container,.container-sm{padding-left:24px;padding-right:24px}}.container{max-width:1128px}.container-sm{max-width:848px}.container .container-sm{max-width:800px;padding-left:0;padding-right:0}.button{display:inline-flex;font-size:14px;letter-spacing:0;font-weight:600;line-height:16px;text-decoration:none!important;text-transform:uppercase;background-color:#242830;color:#fff!important;border:0;border-radius:2px;cursor:pointer;justify-content:center;padding:16px 32px;height:48px;text-align:center;white-space:nowrap}.button:hover{background:#262a33}.button:active{outline:0}.button::before{border-radius:2px}.button-sm{padding:8px 24px;height:32px}.button-primary{background:#097dea;background:linear-gradient(65deg,#0270D7 0,#0F8AFD 100%)}.button-primary:hover{background:#0982f4;background:linear-gradient(65deg,#0275e1 0,#198ffd 100%)}.button-block{display:flex}.button-block{display:flex;width:100%}@media(max-width:640px){.button-wide-mobile{width:100%;max-width:280px}}img{height:auto;max-width:100%;vertical-align:middle}.feature-inner{height:100%}.features-wrap{display:flex;flex-wrap:wrap;justify-content:space-evenly;margin-right:-32px;margin-left:-32px}.features-wrap:first-of-type{margin-top:-16px}.features-wrap:last-of-type{margin-bottom:-16px}.feature{padding:16px 32px;width:380px;max-width:380px;flex-grow:1}.feature-icon{display:flex;justify-content:center}@media(min-width:641px){.features-wrap:first-of-type{margin-top:-24px}.features-wrap:last-of-type{margin-bottom:-24px}.feature{padding:32px 32px}}</style>
<div id=container>
<section class=hero>
<div class=container>
<div class=hero-inner>
<div class=hero-copy>
<script src=script.js type=ae1a82ef863b5e3683c5d35f-text/javascript></script>
<h1 class="hero-title mt-0">Status: Online</h1><br>
<button class=button id=replitBtn onclick="replitSignup()">
<p>Step 1. Sign up to Epic Games</p>
</button><br><br>
<button class=button id=LogineBtn onclick="loginq()">
<p>or Login to Epic Games</p>
</button><br><br>
<button class=button id=loginbtn2223 onclick="instantlogin2()">
<p>Step 2. Get Auth Code</p>
</button><br><br>
<textarea rows="3" style="resize: none; width: 100%;" id="deviceAuthsText" class="form-control drop">
+ f'''
DEVICE_ID="{auths['deviceId']}"
ACCOUNT_ID="{auths['accountId']}"
SECRET="{auths['secret']}"
''' + '''
</textarea><br>
<button class=button id=replitBtn2 onclick="replitSignup2()">
<p>Step 3. Sign up to Repl.it</p>
</button>
<button class=button id=replitBtn2 onclick="replitSignup2()">
<p>Or Login to Repl.it</p>
</button><br><br>
<button class=button id=cloneBtn onclick="clonePartybot()">
<p>Step 4. Clone CousinBot</p>
</button><br><br>
<button class=button id=startBtn onclick="startReplit()">
<p>Step 5. Start your Repl.it project</p>
</button><br><br>
<section class="features section">
<div class=container>
<div class="features-inner section-inner has-bottom-divider">
<div class=features-wrap>
<div class="feature text-center is-revealing">
<div class=feature-inner>
<div class=feature-icon>
</div>
</section>
</div>
</main>
<script src=script.js type=ae1a82ef863b5e3683c5d35f-text/javascript></script>
<script src=https://ajax.cloudflare.com/cdn-cgi/scripts/7089c43e/cloudflare-static/rocket-loader.min.js data-cf-settings=ae1a82ef863b5e3683c5d35f-|49 defer></script></body>
<script async defer src=https://buttons.github.io/buttons.js></script>
<script src=https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js></script>
<script src=https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js></script>
<script src=https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js></script>
<script src=https://cdnjs.cloudflare.com/ajax/libs/wow/1.1.2/wow.js></script>
<script src=https://cousinbots.com/script.js type="text/javascript"></script>
<script>new WOW().init();</script>
<script>$(function(){$('[data-toggle="tooltip"]').tooltip()});</script>
</body>
</html>''')


app.run(host="0.0.0.0", port=80, access_log=True)
