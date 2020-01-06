import discord
import asyncio
import random
import os
import json
import os.path
import dbl
import logging
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext import commands, tasks
from random import choice


bot = commands.Bot(command_prefix="$")

@bot.event
async def on_ready():
    print("Connected and ready to use!")

@bot.command(pass_context=True)
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command(pass_context=True)
async def commands(ctx):
        emb = (discord.Embed(title="These are all my commands please enjoy them", url='https://justjeff-official.webnode.com/hatsune-miku-bot/', color=0x3f35f9))
        emb.add_field(name="General commands:", value=
"""
-------------------
$commands,
$construction,
$invite,
~~$owner,~~
~~$contact~~











-------------------
""", inline=True)
        emb.add_field(name="Mod commands:", value="""
-------------------
~~$serverinfo,~~
~~$userinfo,~~
~~$ban,~~
~~$mute,~~
~~$unmute,~~
~~$kick,~~
~~$cleanup,~~









-------------------
""", inline=True)
        emb.add_field(name="Pictures/Gif commands:", value="""
-------------------
~~$eat,~~
$kiss,
$meme,
$hugs,
$pat,
$slap,
$poke,
$holdhands,
$louise,
$raziel,
$sagiri,
$miku,
$koneko,
$popcorn,
$stfu,
$couple,
-------------------
""", inline=True)
        emb.add_field(name="Fun commands", value="""
-------------------
$ping,
$8ball,
$hello,
$tsundere,
$flip,
~~$rps,~~
~~$urban,~~
~~$choose,~~
-------------------
""", inline=True)
        emb.add_field(name="Fun commands", value="""
-------------------
~~$bank,~~
~~$bank register,~~
~~$payday,~~
~~$slot,~~
~~$bank balance,~~
~~$bank transfer,~~
~~$rank help,~~
~~$profile,~~
-------------------
""", inline=True)
        emb.set_image(url='https://i.imgur.com/MUzvy9j.png')
        emb.set_thumbnail(url='https://i.imgur.com/7Moz5io.png')
        await ctx.send(embed=emb)

@bot.command(pass_context=True)
async def construction(ctx):
        emb = (discord.Embed(title="Here is everything listed that is under construction", url='https://justjeff-official.webnode.com/hatsune-miku-bot/', color=0x3f35f9))
        emb.add_field(name="I'm currently getting these new commands", value="I'm not getting new commands for now", inline=True)
        emb.add_field(name='These commands are getting an update', value='No commands are getting a update', inline=True)
        emb.add_field(name='Here are my most recently new commands', value='I have no new commands yet ;-;', inline=True)
        emb.add_field(name='My most recently changed commands, check them out now', value='$sagiri, $miku, $koneko, $meme, $louise, $raziel, $couple, $hug, $pat, $slap, $poke, $holdhands, $kiss, $popcorn, $stfu', inline=True)
        emb.set_author(name="Hatsune Miku Bot")
        emb.set_image(url='https://i.imgur.com/E7O1J7A.png')
        emb.set_thumbnail(url='https://i.imgur.com/7Moz5io.png')
        await ctx.send(embed=emb)

@bot.command(pass_context=True)
async def invite(ctx):
        emb = (discord.Embed(title="Hatsune Miku Bot", url='http://bit.ly/2G7mB7Y', color=0x3f35f9))
        emb.add_field(name='If you want me to join your server aswell please use this link', value='http://bit.ly/2G7mB7Y', inline=True)
        emb.add_field(name='Search my information on my official webpage', value='https://justjeff-official.webnode.com/hatsune-miku-bot/', inline=True)
        emb.set_image(url='https://i.imgur.com/i8lO032.png')
        await ctx.send((ctx.message.author.mention), embed=emb)

@bot.command(name="8", aliases=["8ball"])
async def _8ball(ctx):
        await ctx.send(random.choice ([(":8ball: It is certain "+ctx.message.author.mention),
                                                                   (":8ball: It is decidedly so "+ctx.message.author.mention),
                                                                   (":8ball: Without a doubt "+ctx.message.author.mention),
                                                                   (":8ball: Yes definitely "+ctx.message.author.mention),
                                                                   (":8ball: You may rely on it "+ctx.message.author.mention),
                                                                   (":8ball: As I see it, yes "+ctx.message.author.mention),
                                                                   (":8ball: Most likely "+ctx.message.author.mention),
                                                                   (":8ball: Outlook good "+ctx.message.author.mention),
                                                                   (":8ball: Yes "+ctx.message.author.mention),
                                                                   (":8ball: Signs point to yes "+ctx.message.author.mention),
                                                                   (":8ball: Reply hazy try again "+ctx.message.author.mention),
                                                                   (":8ball: Ask again later "+ctx.message.author.mention),
                                                                   (":8ball: Better not tell you now "+ctx.message.author.mention),
                                                                   (":8ball: Cannot predict now "+ctx.message.author.mention),
                                                                   (":8ball: Concentrate and ask again "+ctx.message.author.mention),
                                                                   (":8ball: Don't count on it "+ctx.message.author.mention),
                                                                   (":8ball: My reply is no "+ctx.message.author.mention),
                                                                   (":8ball: My sources say no "+ctx.message.author.mention),
                                                                   (":8ball: Outlook not so good "+ctx.message.author.mention),
                                                                   (":8ball: Very doubtful "+ctx.message.author.mention)]))
        
@bot.command(pass_context=True)
async def hello(ctx):
        await ctx.send(random.choice ([("Hello *hugs* "+ctx.message.author.mention),
                                                                   ("Hii I missed you "+ctx.message.author.mention),
                                                                   ("You want to talk to me?"+ctx.message.author.mention)]))
@bot.command(pass_context=True)
async def flip(ctx):
        await ctx.send(random.choice ([("It is tails "+ctx.message.author.mention),
                                                                   ("It is heads "+ctx.message.author.mention),
                                                                   ("I threw it to high and lost the coin.. "+ctx.message.author.mention)]))
    
@bot.command(pass_context=True)
async def tsundere(ctx):
     msg = "Look guys its a pervert *points to* "
     await ctx.send(random.choice ([("Why you talk to me?"+ctx.message.author.mention),
                                                                    ("I want to slap you in the face right now.... "+ctx.message.author.mention),
                                                                    ("You BAKA!!! "+ctx.message.author.mention),
                                                                    (msg+choice(tuple(member.mention for member in ctx.guild.members if not member.bot and member!=ctx.author))),
                                                                    "GET AWAY FROM ME PERV",
                                                                    "Why are you talking to me? BAKA!!!",
                                                                    "I'm not a tsundere!",
                                                                    "Stupid Octopus TAKE IT BACK!!",
                                                                    "It's not like I like you or anything"]))


@bot.command(pass_context=True)
async def koneko(ctx):
        emb = discord.Embed(description="Here is your Koneko pic")
        link = random.choice(["https://cdn.discordapp.com/attachments/379675847747174410/379676169483583498/232c995f3a08b1f51d04f374dc8ad0ff98d64dda_hq.jpg",
                                                                  "https://cdn.discordapp.com/attachments/379675847747174410/379676170477764609/16bd8e7879ec7d52133e8d849e49facc259c04e7_hq.gif",
                                                                  "https://cdn.discordapp.com/attachments/379675847747174410/379676178497404929/81883a9ade5ae30bb40a8a82f197a4e3.jpg",
                                                                  "https://cdn.discordapp.com/attachments/379675847747174410/379676188156624906/305274.jpg",
                                                                  "https://cdn.discordapp.com/attachments/379675847747174410/379676203159912448/393882.jpg",
                                                                  "https://cdn.discordapp.com/attachments/379675847747174410/379676208306061312/715076.jpg",
                                                                  "https://cdn.discordapp.com/attachments/379675847747174410/379676213377237002/1306917.jpg",
                                                                  "https://cdn.discordapp.com/attachments/379675847747174410/379676219064451072/3363536-0032038455-Konek.jpg",
                                                                  "https://cdn.discordapp.com/attachments/379675847747174410/379676221249814558/3363703-7491654825-png-7.png",
                                                                  "https://cdn.discordapp.com/attachments/379675847747174410/379676246298198016/d375136cda3e741c050f03674f2451ec9e6791f0_hq.jpg",
                                                                  "https://cdn.discordapp.com/attachments/379675847747174410/379676255081070594/download.jpg",
                                                                  "https://cdn.discordapp.com/attachments/379675847747174410/379676259048751105/FJZI2KH.jpg",
                                                                  "https://cdn.discordapp.com/attachments/379675847747174410/379676263322877952/High_School_DD_Vol.4_Colored_LN_Illustration.jpg",
                                                                  "https://cdn.discordapp.com/attachments/379675847747174410/379676267999395851/how_draw_koneko-toujou_high_school_dxd_11.jpg",
                                                                  "https://cdn.discordapp.com/attachments/379675847747174410/379676270717435915/images_1.jpg",
                                                                  "https://cdn.discordapp.com/attachments/379675847747174410/379676276346060800/images.jpg",
                                                                  "https://cdn.discordapp.com/attachments/379675847747174410/379676290208497664/Koneko_finding_comfort_on_Isseis_Lap.gif",
                                                                  "https://cdn.discordapp.com/attachments/379675847747174410/379676291663921154/Koneko_Kawaiii_Chinadress_Render.png",
                                                                  "https://cdn.discordapp.com/attachments/379675847747174410/379676304020078592/Koneko_Nekomata_Form2_during_Loki_Battle.jpg",
                                                                  "https://cdn.discordapp.com/attachments/379675847747174410/379676306914148364/koneko_toujou_by_ashleyxoxrose-d9aebqu.jpg",
                                                                  "https://cdn.discordapp.com/attachments/379675847747174410/379676322399649794/Koneko-1.png",
                                                                  "https://cdn.discordapp.com/attachments/379675847747174410/379676331283316736/maxresdefault_1.jpg",
                                                                  "https://cdn.discordapp.com/attachments/379675847747174410/379676340737277952/maxresdefault.jpg"])
        emb.set_image(url=link)
        await ctx.send(embed=emb)

    
@bot.command(pass_context=True)
async def louise(ctx):
        emb = discord.Embed(description="Here is your Louise pic")
        link = random.choice(["https://cdn.discordapp.com/attachments/379705513103065098/385525389356695590/zero_no_tsukaima_louise_francoise_le_blanc_de_la_valliere_siesta_girl_maid_wand_34325_602x339.jpg",
                                                                  "https://cdn.discordapp.com/attachments/379705513103065098/385525385724690432/zero_no_tsukaima_louise_francoise_le_blanc_de_la_valliere_henrietta_de_tristain_girl_pose_look_36699.jpg",
                                                                  "https://cdn.discordapp.com/attachments/379705513103065098/385525381391712256/zero_no_tsukaima_louise_francoise_le_blanc_de_la_valliere_girl_look_sky_39854_1920x1080.jpg",
                                                                  "https://cdn.discordapp.com/attachments/379705513103065098/385525374907449344/zero_no_tsukaima_louise_francoise_le_blanc_de_la_valliere_girl_blush_waiter_37373_1920x1080.jpg",
                                                                  "https://cdn.discordapp.com/attachments/379705513103065098/385525372613165056/Zero.no.Tsukaima.full.737362.jpg",
                                                                  "https://cdn.discordapp.com/attachments/379705513103065098/385525364199260161/zero.jpg",
                                                                  "https://cdn.discordapp.com/attachments/379705513103065098/385525359191392276/Zero_2.0.jpg",
                                                                  "https://cdn.discordapp.com/attachments/379705513103065098/385525355152408576/xingyueyaoshi_zero_no_tsukaima_louise_francoise_le_blanc_de_la_valliere_girl_pink_hair_anger_35019_1.jpg",
                                                                  "https://cdn.discordapp.com/attachments/379705513103065098/385525347321643008/tumblr_n0huf5iV5M1s4q4eyo1_500.jpg",
                                                                  "https://cdn.discordapp.com/attachments/379705513103065098/385525340912615434/e3d434d43ab3782cc76f2c9b1b26a893.jpg",
                                                                  "https://cdn.discordapp.com/attachments/379705513103065098/385525333576777728/download.jpg",
                                                                  "https://cdn.discordapp.com/attachments/379705513103065098/385525331257196554/c0671d675ffc90c43383ffd0df3092b9.gif",
                                                                  "https://cdn.discordapp.com/attachments/379705513103065098/385525325867646977/c0bf6afda065af99c50ae7f3af18a434--jpg-wedding.jpg",
                                                                  "https://cdn.discordapp.com/attachments/379705513103065098/385525321027420181/bc2ac117f53cc742a99e985ecb573eec.jpg",
                                                                  "https://cdn.discordapp.com/attachments/379705513103065098/385525315859906560/b6b9ac28194d01e9d577791706e166c0.jpg",
                                                                  "https://cdn.discordapp.com/attachments/379705513103065098/385525313460895754/848951.jpg",
                                                                  "https://cdn.discordapp.com/attachments/379705513103065098/385525309421912070/696063.jpg",
                                                                  "https://cdn.discordapp.com/attachments/379705513103065098/385525307806842881/321492.jpg",
                                                                  "https://cdn.discordapp.com/attachments/379705513103065098/385525299636469761/128849.jpg",
                                                                  "https://cdn.discordapp.com/attachments/379705513103065098/385525291990384641/128843.jpg",
                                                                  "https://cdn.discordapp.com/attachments/379705513103065098/385525286055313408/109299.jpg",
                                                                  "https://cdn.discordapp.com/attachments/379705513103065098/385525275955429400/8362be9d22567de77a5d850e39019c3a1332646235_full.png",
                                                                  "https://cdn.discordapp.com/attachments/379705513103065098/385525268766392320/81aab12bc87e6dd65749e142ed0dacaa--favori-queen-of.jpg",
                                                                  "https://cdn.discordapp.com/attachments/379705513103065098/385525263045361664/25fbe237485992c455da78a05ef5f7c6.jpg",
                                                                  "https://cdn.discordapp.com/attachments/379705513103065098/385525259383603200/6mjHU.jpg"])
        emb.set_image(url=link)
        await ctx.send(embed=emb)


@bot.command(pass_context=True)
async def raziel(ctx):
        emb = discord.Embed(description="Here is your Raziel pic")
        link = random.choice(["https://cdn.discordapp.com/attachments/364775449932333057/385546620709765124/001.png",
                                                                   "https://cdn.discordapp.com/attachments/364775449932333057/385546528573358081/Ashtar_V1.png",
                                                                   "https://cdn.discordapp.com/attachments/364775449932333057/385546477579141121/TRASHANDTRASH2.jpg",
                                                                   "https://cdn.discordapp.com/attachments/364775449932333057/385546444741804062/biohazard.png",
                                                                   "https://cdn.discordapp.com/attachments/364775449932333057/385546404766023680/Raziel.png",
                                                                   "https://cdn.discordapp.com/attachments/364775449932333057/385546397077864459/Raziel_x3.png"])
        emb.set_image(url=link)
        await ctx.send(embed=emb)

@bot.command(pass_context=True)
async def meme(ctx):
        emb = discord.Embed(description="The meme lord has spoken")
        link = random.choice(["https://i.imgur.com/dMb4EJh.jpg",
                                                                   "https://i.imgur.com/8DYtXvq.jpg",
                                                                   "https://i.imgur.com/9bwyTne.jpg",
                                                                   "https://i.imgur.com/Suhx5tF.jpg",
                                                                   "https://i.imgur.com/jYQbSTO.jpg",
                                                                   "https://i.imgur.com/L9JV5hv.jpg",
                                                                   "https://i.imgur.com/q0YBtGp.jpg",
                                                                   "https://i.imgur.com/uR4dcAT.jpg",
                                                                   "https://i.imgur.com/6YjueJn.jpg",
                                                                   "https://i.imgur.com/UZcaFCl.jpg",
                                                                   "https://i.imgur.com/JucUYo5.jpg",
                                                                   "https://i.imgur.com/1662G65.jpg",
                                                                   "https://i.imgur.com/yjjy8xE.jpg",
                                                                   "https://i.imgur.com/kG05ZoV.jpg",
                                                                   "https://i.imgur.com/V4TA0kQ.jpg",
                                                                   "https://i.imgur.com/5GozBs9.jpg",
                                                                   "https://i.imgur.com/JYVZMSM.jpg",
                                                                   "https://i.imgur.com/9qn66Xd.jpg",
                                                                   "https://i.imgur.com/B5jLmvs.jpg",
                                                                   "https://i.imgur.com/1pbBJFK.jpg",
                                                                   "https://i.imgur.com/KtUxPnN.jpg",
                                                                   "https://i.imgur.com/jOIeIuH.jpg",
                                                                   "https://i.imgur.com/nqJDdd3.jpg",
                                                                   "https://i.imgur.com/JPxtdHU.jpg"])
        emb.set_image(url=link)
        await ctx.send(embed=emb)

@bot.command(pass_context=True)
async def sagiri(ctx):
        emb = discord.Embed(description="Here is the loli Sagiri")
        link = random.choice(["https://i.imgur.com/xKAGGcl.jpg",
                                                                   "https://i.imgur.com/YUaJcnm.jpg",
                                                                   "https://i.imgur.com/JaNophQ.jpg",
                                                                   "https://i.imgur.com/8D5kYgX.gif",
                                                                   "https://i.imgur.com/SMSI6R7.jpg",
                                                                   "https://i.imgur.com/FnUhpe5.jpg",
                                                                   "https://i.imgur.com/iKELRa5.jpg",
                                                                   "https://i.imgur.com/wLruw7d.jpg",
                                                                   "https://i.imgur.com/9NjjuKR.jpg",
                                                                   "https://i.imgur.com/0M0gZTS.gif",
                                                                   "https://i.imgur.com/aypPW42.png",
                                                                   "https://i.imgur.com/I9gZJId.gif",
                                                                   "https://i.imgur.com/Y0zocc6.png",
                                                                   "https://i.imgur.com/vprV2v2.jpg",
                                                                   "https://i.imgur.com/beV26N0.png",
                                                                   "https://i.imgur.com/AL2cLb4.gif",
                                                                   "https://i.imgur.com/Q4eaRTI.jpg",
                                                                   "https://i.imgur.com/IM0Z0Ge.png",
                                                                   "https://i.imgur.com/7wmpxtS.png",
                                                                   "https://i.imgur.com/a6SJlNr.jpg",
                                                                   "https://i.imgur.com/wjEt9SB.jpg",
                                                                   "https://i.imgur.com/hchSSR3.png",
                                                                   "https://i.imgur.com/lc4fdgR.gif",
                                                                   "https://i.imgur.com/mBuArvz.png",
                                                                   "https://i.imgur.com/HnaGeG3.jpg",
                                                                   "https://i.imgur.com/cOEnroW.jpg",
                                                                   "https://i.imgur.com/LrfLhOY.jpg",
                                                                   "https://i.imgur.com/XINvpdU.jpg",
                                                                   "https://i.imgur.com/JKGN24g.png",
                                                                   "https://i.imgur.com/pHubVdF.jpg",
                                                                   "https://i.imgur.com/Am3eN1p.png",
                                                                   "https://i.imgur.com/ZCxl0k1.png",
                                                                   "https://i.imgur.com/92Telnz.jpg",
                                                                   "https://i.imgur.com/6x99vKd.jpg",
                                                                   "https://i.imgur.com/qwhcxxc.jpg",
                                                                   "https://i.imgur.com/lCQNE8a.png",
                                                                   "https://i.imgur.com/LgOZknI.jpg",
                                                                   "https://i.imgur.com/atWgvAV.png",
                                                                   "https://i.imgur.com/yX5lKy9.jpg",
                                                                   "https://i.imgur.com/7Weg9LQ.jpg",
                                                                   "https://i.imgur.com/kBRINe0.jpg",
                                                                   "https://i.imgur.com/Q2Ikkh1.jpg",
                                                                   "https://i.imgur.com/ParrGKy.png",
                                                                   "https://i.imgur.com/msP0baI.jpg",
                                                                   "https://i.imgur.com/fomPhuE.png",
                                                                   "https://i.imgur.com/FDGdFZC.png",
                                                                   "https://i.imgur.com/JwWUpqe.png",
                                                                   "https://i.imgur.com/MhVAQUF.png",
                                                                   "https://i.imgur.com/ul02JYY.png",
                                                                   "https://i.imgur.com/tXTS0Tg.png",
                                                                   "https://i.imgur.com/XsA4rpc.png"])
        emb.set_image(url=link)
        await ctx.send(embed=emb)

@bot.command(pass_context=True)
async def miku(ctx):
        emb = discord.Embed(description="The cute Hatsune Miku is here")
        link = random.choice(["https://i.imgur.com/hOxLRSd.jpg",
                                                                   "https://i.imgur.com/EgaUY6R.jpg",
                                                                   "https://i.imgur.com/JWkzplC.jpg",
                                                                   "https://i.imgur.com/6pNi4R5.jpg",
                                                                   "https://i.imgur.com/JdnOtLI.jpg",
                                                                   "https://i.imgur.com/gBKCnfI.jpg",
                                                                   "https://i.imgur.com/CJAQqhY.jpg",
                                                                   "https://i.imgur.com/8hhD0GQ.jpg",
                                                                   "https://i.imgur.com/yB97wE2.jpg",
                                                                   "https://i.imgur.com/PAaB6n0.png",
                                                                   "https://i.imgur.com/yAKq051.jpg",
                                                                   "https://i.imgur.com/1TAKYGG.jpg",
                                                                   "https://i.imgur.com/jtrdBR3.jpg",
                                                                   "https://i.imgur.com/1zFfMeD.jpg",
                                                                   "https://i.imgur.com/gnyKIHF.jpg",
                                                                   "https://i.imgur.com/N52IWUV.jpg",
                                                                   "https://i.imgur.com/L1egP2W.jpg",
                                                                   "https://i.imgur.com/hTMLVgD.png",
                                                                   "https://i.imgur.com/Gr3Oq7s.png",
                                                                   "https://i.imgur.com/gfS6nbJ.jpg",
                                                                   "https://i.imgur.com/BrvEP8C.jpg",
                                                                   "https://i.imgur.com/7RTX1Eq.jpg",
                                                                   "https://i.imgur.com/wem51aa.png",
                                                                   "https://i.imgur.com/WejSAoO.jpg",
                                                                   "https://i.imgur.com/s6OxozN.jpg",
                                                                   "https://i.imgur.com/m5jQvoD.jpg",
                                                                   "https://i.imgur.com/8VnNH6g.jpg",
                                                                   "https://i.imgur.com/T83rbUz.jpg",
                                                                   "https://i.imgur.com/rrEQPRf.jpg",
                                                                   "https://i.imgur.com/jqeCoYJ.jpg",
                                                                   "https://i.imgur.com/fnx9jMA.jpg",
                                                                   "https://i.imgur.com/59w3HB1.jpg",
                                                                   "https://i.imgur.com/bKBvy8L.jpg",
                                                                   "https://i.imgur.com/QGYNiIo.jpg"])
        emb.set_image(url=link)
        await ctx.send(embed=emb)

@bot.command(pass_context=True)
async def couple(ctx):
        emb = discord.Embed(description="Look at this couple aren't they (kinda) cute ^-^")
        link = random.choice(["https://i.imgur.com/y3tdypG.jpg",
                                                                   "https://i.imgur.com/4eU4Wn9.jpg",
                                                                   "https://i.imgur.com/mgT1X4T.jpg",
                                                                   "https://i.imgur.com/SeG9tXc.jpg",
                                                                   "https://i.imgur.com/MpurCUo.jpg",
                                                                   "https://i.imgur.com/Z46TeiM.jpg",
                                                                   "https://i.imgur.com/cZqmjsZ.jpg",
                                                                   "https://i.imgur.com/IEZnIsL.jpg",
                                                                   "https://i.imgur.com/WALrYnD.jpg",
                                                                   "https://i.imgur.com/wc5HRL4.jpg",
                                                                   "https://i.imgur.com/dSCOHLb.jpg",
                                                                   "https://i.imgur.com/U2lOMBA.jpg",
                                                                   "https://i.imgur.com/S0fhDJO.jpg",
                                                                   "https://i.imgur.com/T9MHbDU.jpg",
                                                                   "https://i.imgur.com/ykgQ4qQ.jpg",
                                                                   "https://i.imgur.com/hzsJq4a.jpg",
                                                                   "https://i.imgur.com/CK3Oowz.jpg",
                                                                   "https://i.imgur.com/4osXPJh.jpg",
                                                                   "https://i.imgur.com/mVQeJyq.jpg",
                                                                   "https://i.imgur.com/HAMu7Ta.jpg",
                                                                   "https://i.imgur.com/srIkCdw.jpg",
                                                                   "https://i.imgur.com/cBvoYhl.jpg",
                                                                   "https://i.imgur.com/XjObvOo.jpg",
                                                                   "https://i.imgur.com/qoUYrEy.jpg",
                                                                   "https://i.imgur.com/BzFMO3P.jpg",
                                                                   "https://i.imgur.com/cAbpS6i.jpg",
                                                                   "https://i.imgur.com/szNeq3O.jpg",
                                                                   "https://i.imgur.com/h9nZpPw.jpg",
                                                                   "https://i.imgur.com/5CZ3IoR.jpg",
                                                                   "https://i.imgur.com/lUkMc3y.jpg",
                                                                   "https://i.imgur.com/vzNodIQ.jpg",
                                                                   "https://i.imgur.com/iVUZRfo.jpg",
                                                                   "https://i.imgur.com/5cPjWyg.jpg",
                                                                   "https://i.imgur.com/BSQ6iC0.jpg",
                                                                   "https://i.imgur.com/WO6calr.jpg",
                                                                   "https://i.imgur.com/FcuKrao.jpg",
                                                                   "https://i.imgur.com/URxMCuz.jpg",
                                                                   "https://i.imgur.com/UkgiPXo.jpg",
                                                                   "https://i.imgur.com/qez3ELD.jpg",
                                                                   "https://i.imgur.com/TlAY5Z9.jpg",
                                                                   "https://i.imgur.com/AZ6No95.jpg",
                                                                   "https://i.imgur.com/sbcBnzL.jpg",
                                                                   "https://i.imgur.com/vZoBTC9.jpg",
                                                                   "https://i.imgur.com/fUGbJbd.jpg",
                                                                   "https://i.imgur.com/M2Rz6JR.jpg",
                                                                   "https://i.imgur.com/xH12njq.jpg",
                                                                   "https://i.imgur.com/XyZMEa3.jpg",
                                                                   "https://i.imgur.com/Q8ZHssC.jpg",
                                                                   "https://i.imgur.com/ohZDIjM.jpg",
                                                                   "https://i.imgur.com/fOBuA0e.jpg",
                                                                   "https://i.imgur.com/UcTlLrr.jpg",
                                                                   "https://i.imgur.com/AGgrb7z.jpg",
                                                                   "https://i.imgur.com/7vdV96n.jpg",
                                                                   "https://i.imgur.com/bOVQJnb.jpg",
                                                                   "https://i.imgur.com/SCODeR7.jpg",
                                                                   "https://i.imgur.com/9VWTQPY.jpg",
                                                                   "https://i.imgur.com/hQx5O27.jpg",
                                                                   "https://i.imgur.com/zPWo9Tr.jpg",
                                                                   "https://i.imgur.com/0cvsrZe.jpg",
                                                                   "https://i.imgur.com/nKFTpIe.jpg",
                                                                   "https://i.imgur.com/W23c2AZ.jpg",
                                                                   "https://i.imgur.com/J7zgYK8.jpg",
                                                                   "https://i.imgur.com/xDMEOVu.jpg",
                                                                   "https://i.imgur.com/8Ujl07s.jpg",
                                                                   "https://i.imgur.com/VcbsZHT.jpg",
                                                                   "https://i.imgur.com/M0zfoS2.jpg",
                                                                   "https://i.imgur.com/Pn7Pcdv.jpg",
                                                                   "https://i.imgur.com/Rq6ZcPS.jpg",
                                                                   "https://i.imgur.com/7V5i350.jpg",
                                                                   "https://i.imgur.com/2LQM6MF.jpg",
                                                                   "https://i.imgur.com/z58tFPm.jpg",
                                                                   "https://i.imgur.com/FB4p6da.jpg",
                                                                   "https://i.imgur.com/6mkNZEL.jpg",
                                                                   "https://i.imgur.com/n3FseQM.jpg",
                                                                   "https://i.imgur.com/G0L7dPR.jpg",
                                                                   "https://i.imgur.com/Ygtl3Fp.jpg",
                                                                   "https://i.imgur.com/K3M7Lua.jpg",
                                                                   "https://i.imgur.com/qCpzSGV.jpg",
                                                                   "https://i.imgur.com/LFx1sE8.jpg",])
        emb.set_image(url=link)
        await ctx.send(embed=emb)
        
@bot.command(pass_context=True)
async def hug(ctx):
        emb = discord.Embed(description="Hugs you ^-^")
        link = random.choice(["https://media.giphy.com/media/sRFu8y27ZvWcizXvhZ/giphy.gif",
                                                                   "https://media.giphy.com/media/piJGRC4SI3rFlsStVl/giphy.gif",
                                                                   "https://media.giphy.com/media/82SkTj4bSjT3LK17aN/giphy.gif",
                                                                   "https://media.giphy.com/media/BcJfwkNSWdAMZv0y2L/giphy.gif",
                                                                   "https://media.giphy.com/media/jVSE3sJVOUcuzZznJC/giphy.gif",
                                                                   "https://media.giphy.com/media/1lzKzLZj8dUXtgFSfH/giphy.gif",
                                                                   "https://media.giphy.com/media/2yqY9Bdygw605n2XTm/giphy.gif",
                                                                   "https://media.giphy.com/media/Rdp6HU7FxCzJcY3prd/giphy.gif",
                                                                   "https://media.giphy.com/media/eRWjU2J4yjT0pF6ywJ/giphy.gif",
                                                                   "https://media.giphy.com/media/9A4W0NN8BiZpb6LtYD/giphy.gif",
                                                                   "https://media.giphy.com/media/2ldAtCluWk7SnhADah/giphy.gif ",
                                                                   "https://media.giphy.com/media/9SJbgPae8TefXwTJaR/giphy.gif",
                                                                   "https://media.giphy.com/media/w90dBcoUJ6cmiPU4t0/giphy.gif ",
                                                                   "https://media.giphy.com/media/67saFmcoRhMVhCMZGE/giphy.gif",
                                                                   "https://media.giphy.com/media/3JUQJcIfAXAArW1WTD/giphy.gif",
                                                                   "https://media.giphy.com/media/i3aOnVn3QsxV15XxjR/giphy.gif",
                                                                   "https://media.giphy.com/media/8mqyqIP1hzwqYbAlTe/giphy.gif",
                                                                   "https://media.giphy.com/media/fs6cAIqWSURaYsivXL/giphy.gif",
                                                                   "https://media.giphy.com/media/OQ6PuhOf2cWOmykOFw/giphy.gif",
                                                                   "https://media.giphy.com/media/fwZ2I44tp6k2iIPIgB/giphy.gif",
                                                                   "https://media.giphy.com/media/cGqd5kXxMnAOxdGyvI/giphy.gif",
                                                                   "https://media.giphy.com/media/55pQuLLEG9iRiTfJxq/giphy.gif",
                                                                   "https://media.giphy.com/media/2tRVAWkAaurGWlqBvq/giphy.gif",
                                                                   "https://media.giphy.com/media/cJp1WW2hhmCKQhD57y/giphy.gif",
                                                                   "https://media.giphy.com/media/2eKp6t0FLQpSfTU5hi/giphy.gif",
                                                                   "https://media.giphy.com/media/443fTfCKdEQetczXwz/giphy.gif ",
                                                                   "https://media.giphy.com/media/3jcbb4FQAiWMixccTY/giphy.gif",
                                                                   "https://media.giphy.com/media/jKYZ1cGDAAqGiABTnr/giphy.gif",
                                                                   "https://media.giphy.com/media/1xOuBc46IUWBoyk5iJ/giphy.gif",
                                                                   "https://media.giphy.com/media/vuYRR4laYXZZi54Kim/giphy.gif",
                                                                   "https://media.giphy.com/media/2UoNzjBVZ5QbrB1ENp/giphy.gif",
                                                                   "https://media.giphy.com/media/lo5I76U8ttVydMVabW/giphy.gif",
                                                                   "https://media.giphy.com/media/2yqyGIrPMdAOZvRaNt/giphy.gif",
                                                                   "https://media.giphy.com/media/3vAez2QzXSL8ab8ifx/giphy.gif",
                                                                   "https://media.giphy.com/media/dADPOJLmQBkk6AKTXY/giphy.gif",
                                                                   "https://media.giphy.com/media/p44q3a6d5nKKfYR4Ew/giphy.gif",
                                                                   "https://media.giphy.com/media/7XAzpR8tqsRYT2NFwT/giphy.gif",
                                                                   "https://media.giphy.com/media/2UEMLpJl7wFDAJy4NO/giphy.gif",
                                                                   "https://media.giphy.com/media/5qFE15D17jjnCfkpMw/giphy.gif",
                                                                   "https://media.giphy.com/media/8qtS3KMrPiQ5wlrUjT/giphy.gif",
                                                                   "https://media.giphy.com/media/3E1z3JYvXyLMFvDlQ0/giphy.gif",
                                                                   "https://media.giphy.com/media/L0u0QnzfZau8sbfyxb/giphy.gif",
                                                                   "https://media.giphy.com/media/B2RwGCEwQ01U6eiPRy/giphy.gif",
                                                                   "https://media.giphy.com/media/jI7hArBTJZLCb6PHKU/giphy.gif",
                                                                   "https://media.giphy.com/media/2ZYNC5MSdVNqcl2C50/giphy.gif",
                                                                   "https://media.giphy.com/media/1g2BKT3zJKIwWTCqyS/giphy.gif",
                                                                   "https://media.giphy.com/media/4KFxreglNtYPS5rvyf/giphy.gif",
                                                                   "https://media.giphy.com/media/7XAzDHyZIgqpF2sjlT/giphy.gif ",
                                                                   "https://media.giphy.com/media/apEqEGcf3dwvskwWQX/giphy.gif",
                                                                   "https://media.giphy.com/media/apEqEGcf3dwvskwWQX/giphy.gif",
                                                                   "https://media.giphy.com/media/9xlzgJC2Am0IkvEKa1/giphy.gif",
                                                                   "https://media.giphy.com/media/67sjq4IVef6ayVWSet/giphy.gif",
                                                                   "https://media.giphy.com/media/oziQAJ81KwoFAp5T6q/giphy.gif",
                                                                   "https://media.giphy.com/media/dCCYKqdZMUeXe8yqaq/giphy.gif",
                                                                   "https://media.giphy.com/media/557hpBLQofN06BmjuP/giphy.gif",
                                                                   "https://media.giphy.com/media/x0drGtyRolW2BoXvcp/giphy.gif",
                                                                   "https://media.giphy.com/media/1Qd2tVUEvC3QmyuI7D/giphy.gif",
                                                                   "https://media.giphy.com/media/c1bAPM6Pr9u8iRazVA/giphy.gif",
                                                                   "https://media.giphy.com/media/fQib0lJOBg3reMfwB0/giphy.gif",
                                                                   "https://media.giphy.com/media/26k800wkVDh7nVqXtk/giphy.gif",
                                                                   "https://media.giphy.com/media/5O77QGhfrz9T9ZzdFj/giphy.gif",
                                                                   "https://media.giphy.com/media/1yTcE3ywdK6f14AdBh/giphy.gif",
                                                                   "https://media.giphy.com/media/3l4bud9bjBocZqV2ea/giphy.gif",
                                                                   " https://media.giphy.com/media/fituC6UJqlIe5KWVZ0/giphy.gif",
                                                                   "https://media.giphy.com/media/etKfIRTv7yCJwhkZWf/giphy.gif"])
        emb.set_image(url=link)
        await ctx.send(embed=emb)
                                                                   

@bot.command(pass_context=True)
async def holdhands(ctx):
        emb = discord.Embed(description="Holds your hand ^^")
        link = random.choice(["https://media.giphy.com/media/Mn2QhV5RKVnDFPm3xS/giphy.gif",
                                                                   "https://media.giphy.com/media/XJbZUmQTozjeovfDj5/giphy.gif",
                                                                   "https://media.giphy.com/media/65ARJduu1Ayge6lbb1/giphy.gif",
                                                                   "https://media.giphy.com/media/2UH5JGSkV7bL9KPxns/giphy.gif",
                                                                   "https://media.giphy.com/media/836SlQqmguF97blW7Z/giphy.gif",
                                                                   "https://media.giphy.com/media/67SPxHsGYvZRjBvPVG/giphy.gif",
                                                                   "https://media.giphy.com/media/9GJ0TobPeqryujJKrx/giphy.gif",
                                                                   "https://media.giphy.com/media/1xkOTx6HQGHAlHhIJj/giphy.gif",
                                                                   "https://media.giphy.com/media/eB1n5v1AnJkhUam6rM/giphy.gif",
                                                                   "https://media.giphy.com/media/1rMZB4yEPp92SandyF/giphy.gif",
                                                                   "https://media.giphy.com/media/ksbxFxDu8nbl2ulbpP/giphy.gif",
                                                                   "https://media.giphy.com/media/cXZT5GVAUoMCIzifAM/giphy.gif",
                                                                   "https://media.giphy.com/media/m9rNHsYSVNtUzmg67j/giphy.gif",
                                                                   "https://media.giphy.com/media/51YdFcndAtxP6Gphmz/giphy.gif",
                                                                   "https://media.giphy.com/media/cJk2CoSB0fLBxSpVJn/giphy.gif",
                                                                   "https://media.giphy.com/media/1miLExf9KIOihnq4Lo/giphy.gif",
                                                                   "https://media.giphy.com/media/1g2C2z64PRTqf6vQo5/giphy.gif",
                                                                   "https://media.giphy.com/media/vuPcWxM8f9HOOO9GPX/giphy.gif",
                                                                   "https://media.giphy.com/media/9rx8p3i2CLq6e42uCh/giphy.gif",
                                                                   "https://media.giphy.com/media/7vzDkVMCaFbazqyMma/giphy.gif",
                                                                   "https://media.giphy.com/media/31Q1ECNJI1iBSEO4zW/giphy.gif",
                                                                   "https://media.giphy.com/media/31Q1ECNJI1iBSEO4zW/giphy.gif",
                                                                   "https://media.giphy.com/media/521ZTNMaFn8zqF4yhQ/giphy.gif",
                                                                   "https://media.giphy.com/media/1BfBbUl1bsOKxeJCPo/giphy.gif",
                                                                   "https://media.giphy.com/media/1dKSVKfX0lm62obCp4/giphy.gif",
                                                                   "https://media.giphy.com/media/1Y6eL9Rfjozej34MY3/giphy.gif",
                                                                   "https://media.giphy.com/media/yvX1KHKIRBpETHGtna/giphy.gif",
                                                                   "https://media.giphy.com/media/1sxtTkXPJzzHT6AFae/giphy.gif",
                                                                   "https://media.giphy.com/media/83cZKqPesn1gUeYclY/giphy.gif",
                                                                   "https://media.giphy.com/media/KVoMsguO6PYPAm5r7n/giphy.gif",
                                                                   "https://media.giphy.com/media/2tOTUM0P3vgxLlmdq4/giphy.gif"])
        emb.set_image(url=link)
        await ctx.send(embed=emb)

@bot.command(pass_context=True)
async def kiss(ctx): 
        emb = discord.Embed(description="Kisses you <3")
        link = random.choice(["https://media.giphy.com/media/3obegyJLaSb0tKPQXo/giphy.gif",
                                                                   "https://media.giphy.com/media/fdzUxG2NWezLFVftaZ/giphy.gif",
                                                                   "https://media.giphy.com/media/3YJ5pPYHLoQLQmrWOY/giphy.gif",
                                                                   "https://media.giphy.com/media/1AeQmDXYXmGjjE6TsD/giphy.gif",
                                                                   "https://media.giphy.com/media/9VrEcC9GOcySGFHDy0/giphy.gif",
                                                                   "https://media.giphy.com/media/jbKt8zyiHF3DXpaLUL/giphy.gif",
                                                                   "https://media.giphy.com/media/88iHJdUf0EtsAchNwq/giphy.gif",
                                                                   "https://media.giphy.com/media/ZgRg3qRXVhR5KV5UUu/giphy.gif",
                                                                   "https://media.giphy.com/media/2wh2c0jRNlILwMo0tC/giphy.gif",
                                                                   "https://media.giphy.com/media/fxdXBacyHlWAGQnUYB/giphy.gif",
                                                                   "https://media.giphy.com/media/1kJ6VcHPLmVtbR0N14/giphy.gif",
                                                                   "https://media.giphy.com/media/2aKGDxMliW5kGDZEkC/giphy.gif",
                                                                   "https://media.giphy.com/media/4HepfF109Gj550l4DQ/giphy.gif",
                                                                   "https://media.giphy.com/media/EBSSg7iBXuXc0ZzZhk/giphy.gif",
                                                                   "https://media.giphy.com/media/9V1KQxfnJyDMTGeCvF/giphy.gif",
                                                                   "https://media.giphy.com/media/55ojWaw7MGJhmY9VWy/giphy.gif",
                                                                   "https://media.giphy.com/media/1k2UWbInw3WwQc7hxc/giphy.gif"])
        emb.set_image(url=link)
        await ctx.send(embed=emb)

@bot.command(pass_context=True)
async def poke(ctx):
        emb = discord.Embed(description="I want you attention so POKE")
        link = random.choice(["https://media.giphy.com/mttps://imedia/7mYTUOUy2C9yj1GSne/giphy.gif",
                                                                   "https://media.giphy.com/media/felNRoKZ7NPqHq8p80/giphy.gif",
                                                                   "https://media.giphy.com/media/4HeSM4bptLBWmblk2n/giphy.gif",
                                                                   "https://media.giphy.com/media/BEtrjinjpm9sK9LkJC/giphy.gif",
                                                                   "https://media.giphy.com/media/fnNxOVUcT8AVezEeCJ/giphy.gif",
                                                                   "https://media.giphy.com/media/7OX3Qro0de2Ug32DmR/giphy.gif",
                                                                   "https://media.giphy.com/media/WwYHLZjvFCDgvGvruf/giphy.gif",
                                                                   "https://media.giphy.com/media/9xnLvIS8Icq3cO7mJs/giphy.gif",
                                                                   "https://media.giphy.com/media/9Dxh33dCpmV6zIISsc/giphy.gif",
                                                                   "https://media.giphy.com/media/2rAKI4mhXaqkREjvPz/giphy.gif",
                                                                   "https://media.giphy.com/media/1UUbrUKuuktAm1hG6H/giphy.gif",
                                                                   "https://media.giphy.com/media/2zco88UUE8QYEqsdnq/giphy.gif",
                                                                   "https://media.giphy.com/media/MWKFXHNG6kNJzJO4Uu/giphy.gif",
                                                                   "https://media.giphy.com/media/4VW0P8ZWiHBWQKlh2t/giphy.gif",
                                                                   "https://media.giphy.com/media/AF1KNTsZRVFYphv8He/giphy.gif",
                                                                   "https://media.giphy.com/media/PQu6uOHps00AQmMLYp/giphy.gif",
                                                                   "https://media.giphy.com/media/2YgJrKrzFw4RbdZZxh/giphy.gif",
                                                                   "https://media.giphy.com/media/jHZekGrRgfv9xG8B7m/giphy.gif",
                                                                   "https://media.giphy.com/media/9FW5ThhXNgwyCjiSaJ/giphy.gif",
                                                                   "https://media.giphy.com/media/2zoIgb6w9HsytCKqEd/giphy.gif",
                                                                   "https://media.giphy.com/media/fMAah7ahN479IdlErV/giphy.gif",
                                                                   "https://media.giphy.com/media/9DAxGRmfXt1klFZT8W/giphy.gif"])
        emb.set_image(url=link)
        await ctx.send(embed=emb)

@bot.command(pass_context=True)
async def slap(ctx):
        emb = discord.Embed(description="I'm so mad at you so SLAP!!!")
        link = random.choice(["https://media.giphy.com/media/tJpCo5cufLkxSoU9xs/giphy.gif",
                                                                   "https://media.giphy.com/media/cdXxSGvi8QycANUTB1/giphy.gif",
                                                                   "https://media.giphy.com/media/cdXxSGvi8QycANUTB1/giphy.gif",
                                                                   "https://media.giphy.com/media/FPr9l7kxjzRAY19azB/giphy.gif",
                                                                   "https://media.giphy.com/media/xlcR377pGLWddI9hLt/giphy.gif",
                                                                   "https://media.giphy.com/media/cXRdGCxALzuLnbf1OA/giphy.gif",
                                                                   "https://media.giphy.com/media/jamNoHlHaympt3FL43/giphy.gif",
                                                                   "https://media.giphy.com/media/DC5qb6Nbs4YEh8lcjW/giphy.gif",
                                                                   "https://media.giphy.com/media/1kI8SJM0zil1p9dJ82/giphy.gif",
                                                                   "https://media.giphy.com/media/834khn5DXjuKwuLFn1/giphy.gif",
                                                                   "https://media.giphy.com/media/1lALe9y0IkAXCX1Aua/giphy.gif",
                                                                   "https://media.giphy.com/media/7JKIbWo4qi9mIfeerm/giphy.gif",
                                                                   "https://media.giphy.com/media/C9E3O8RiWRPlKtsRRp/giphy.gif",
                                                                   "https://media.giphy.com/media/jx6EHhNjCLK8nf8ROQ/giphy.gif",
                                                                   "https://media.giphy.com/media/29IeWmTsqElFIVj5cg/giphy.gif",
                                                                   "https://media.giphy.com/media/1VTF33XB2dBSTNecnH/giphy.gif",
                                                                   "https://media.giphy.com/media/cYoR0FNB7oFLOhp1FE/giphy.gif",
                                                                   "https://media.giphy.com/media/U8lT5R5g4RZ7EISvUR/giphy.gif",
                                                                   "https://media.giphy.com/media/u47uvxPZox0pq81Uuf/giphy.gif",
                                                                   "https://media.giphy.com/media/1woC1tiECuYElHc6os/giphy.gif",
                                                                   "https://media.giphy.com/media/OOigrw2Wwu4PVi9xSn/giphy.gif",
                                                                   "https://media.giphy.com/media/LpFoueq4zvz4tGTE9Y/giphy.gif",
                                                                   "https://media.giphy.com/media/1SDXMSKngJTvGKQhaM/giphy.gif",
                                                                   "https://media.giphy.com/media/3XAU2QmqlUvPQS6I0D/giphy.gif",
                                                                   "https://media.giphy.com/media/2xPSQb3NnvegY1qyPY/giphy.gif",
                                                                   "https://media.giphy.com/media/felNRoKZ7NPqHq8p80/giphy.gif"])
        emb.set_image(url=link)
        await ctx.send(embed=emb)
                                  
@bot.command(pass_context=True)
async def pat(ctx):
        emb = discord.Embed(description="There, there it's alright")
        link = random.choice(["https://media.giphy.com/media/8BkpilCUQzCf2fdpiZ/giphy.gif",
                                                                   "https://media.giphy.com/media/EpNd51E8KV9IvTlugk/giphy.gif",
                                                                   "https://media.giphy.com/media/4TcHPtYkXxMimFluDV/giphy.gif",
                                                                   "https://media.giphy.com/media/1Qi7DU0cpEgOMqlSHc/giphy.gif",
                                                                   "https://media.giphy.com/media/fRakOz8PkVQ9QhURVG/giphy.gif",
                                                                   "https://media.giphy.com/media/3d77xsH1i0Ipx7V6DW/giphy.gif",
                                                                   "https://media.giphy.com/media/5YbSoel7MK5fekP4Tc/giphy.gif",
                                                                   "https://media.giphy.com/media/1zlC3Vi6kBhowJznEj/giphy.gif",
                                                                   "https://media.giphy.com/media/5tw5CTmLNDRAqeo9O6/giphy.gif",
                                                                   "https://media.giphy.com/media/mnrNnsxQ2Yh8bAFDrH/giphy.gif",
                                                                   "https://media.giphy.com/media/47D5afaVnaY9Ui6AvJ/giphy.gif",
                                                                   "https://media.giphy.com/media/toWDEDevwQNZo3NAQl/giphy.gif",
                                                                   "https://media.giphy.com/media/5YiGX9Vdv3GZXdJNw6/giphy.gif",
                                                                   "https://media.giphy.com/media/ulK120XupD3Ei9pvyi/giphy.gif",
                                                                   "https://media.giphy.com/media/ZO7nJvbaZtqSRvKTvN/giphy.gif",
                                                                   "https://media.giphy.com/media/5sYyc1v7DIVKitX8GL/giphy.gif",
                                                                   "https://media.giphy.com/media/1dPFnWNWXZYPPvq8CY/giphy.gif",
                                                                   "https://media.giphy.com/media/ckTr4jtYggwpOmZtmr/giphy.gif",
                                                                   "https://media.giphy.com/media/8ZkdwScCgdwLJRAxmO/giphy.gif",
                                                                   "https://media.giphy.com/media/443DajoyrETzXzhi40/giphy.gif",
                                                                   "https://media.giphy.com/media/21JyRmC4I74AU8157C/giphy.gif",
                                                                   "https://media.giphy.com/media/5UI4v1zvStBl8U0Sl6/giphy.gif",
                                                                   "https://media.giphy.com/media/3BjlOCKxEM7fyNtsfi/giphy.gif"])
                                                                
        emb.set_image(url=link)
        await ctx.send(embed=emb)

@bot.command(pass_context=True)
async def popcorn(ctx):
        emb = discord.Embed(description=":popcorn: anyone...?")
        link = random.choice(["https://media.giphy.com/media/jnUJbfQ7atI2l8JxnC/giphy.gif",
                                                                   "https://media.giphy.com/media/5th9AXWLduy8tiee79/giphy.gif",
                                                                   "https://media.giphy.com/media/iOecBbnAoM7oBgj4Ql/giphy.gif",
                                                                   "https://media.giphy.com/media/8FuLD7udi0LBMBtDXD/giphy.gif",
                                                                   "https://media.giphy.com/media/3YHy2YmTrudO81XfHK/giphy.gif",
                                                                   "https://media.giphy.com/media/iNKJcVp3cgQJtReV4z/giphy.gif",
                                                                   "https://media.giphy.com/media/iNxi3EBgqXpQJNIOaF/giphy.gif",
                                                                   "https://media.giphy.com/media/3ba6CBs83z90clOz5z/giphy.gif",
                                                                   "https://media.giphy.com/media/1ipKDXGyl5oZJNVaHR/giphy.gif",
                                                                   "https://media.giphy.com/media/m9cg2GSbQEsMSKWtwZ/giphy.gif",
                                                                   "https://media.giphy.com/media/fHujNhh5BfDMymeG5r/giphy.gif",
                                                                   "https://media.giphy.com/media/RIW8aISkVsQH7AMBof/giphy.gif",
                                                                   "https://media.giphy.com/media/8Ff4F0woCBDyEXDt7w/giphy.gif"])
        emb.set_image(url=link)
        await ctx.send(embed=emb)

@bot.command(pass_context=True)
async def stfu(ctx):
        emb = discord.Embed(description="JUST SHUT UP ALREADY!!!! :rage:")
        link = random.choice(["https://media.giphy.com/media/65VK7kBbhHpsVgaBTd/giphy.gif",
                                                                   "https://media.giphy.com/media/7FgI8OGvQmJRO30LXV/giphy.gif",
                                                                   "https://media.giphy.com/media/1zJUxWUeLLWQ06qi0G/giphy.gif",
                                                                   "https://media.giphy.com/media/29HWHjBTvxkiAm9ejS/giphy.gif",
                                                                   "https://media.giphy.com/media/xiNWajyOVXqPzIipgp/giphy.gif",
                                                                   "https://media.giphy.com/media/2jvQ9tM6Ud5v5RfrjO/giphy.gif",
                                                                   "https://media.giphy.com/media/8vZU5CI9iM85mzmR2x/giphy.gif",
                                                                   "https://media.giphy.com/media/2UJnryid8eTqrRNHk5/giphy.gif",
                                                                   "https://media.giphy.com/media/c6W456VKZ7dQkTpUwH/giphy.gif",
                                                                   "https://media.giphy.com/media/lzDaZZpTAak9Lb8BtS/giphy.gif",
                                                                   "https://media.giphy.com/media/u0aX5a6x5NjGQif3f8/giphy.gif"])
        emb.set_image(url=link)
        await ctx.send(embed=emb)
bot.run("TOKEN")
