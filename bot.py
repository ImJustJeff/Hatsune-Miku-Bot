import discord
import asyncio
import random
import os
from discord.ext.commands import Bot
from discord.ext import commands

client = discord.Client()
bot = discord.Client()
discord.Client.setUsername='Koneko'
my_bot = Bot(command_prefix="$")
bothAuth = ''

@client.event
async def on_ready():
    print("Logged in as :")
    print(client.user.name)
    print("ID:")
    print(client.user.id)
    print("Ready to use")
    discord.Client.setUsername='Koneko'
async def wait_until_login():
    discord.Client.setUsername='Koneko'
    await client.change_presence(game=discord.Game(name="Reporting for Duty!! Use '$commands'to see all my commands"))


@client.event
async def on_message (message):
    if message.author == client.user:
        await client.change_presence(game=discord.Game(name="Reporting for Duty!! Use '$commands'to see all my commands"))
        discord.Client.setUsername='Koneko'
        return
    elif message.content.startswith("$owner"):
        await client.send_message(message.channel,"My master is <@266245400988614656>, he made me into what i am right now :D and he is still developing me :3")


    elif message.content.startswith("$start"):
        await client.send_message(message.channel,"""Check one: Completed
Check two: Complete
Check three: Completed
Hatsune Miku Bot is Reporting for Duty""")

    elif message.content.startswith("$commands"):
        emb = (discord.Embed(title="These are all my commands please enjoy them", url='https://justjeff-official.webnode.com/hatsune-miku-bot/', color=0x3f35f9))
        emb.add_field(name="General commands:", value=
"""
--------------------
$commands,
$construction,
$invite,
$owner,
$contact, (UNAVAILABLE)


--------------------
""", inline=True)
        emb.add_field(name="mod commands (THESE ARE UNAVAILABLE FOR NOW):", value="""
--------------------
$serverinfo,
$userinfo,
$ban,
$mute,
$unmute,
$kick,
$cleanup,
--------------------
""", inline=True)
        emb.add_field(name="Pictures/Gif commands:", value="""
--------------------
$kiss,
$meme,
$hug,
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
--------------------
""", inline=True)
        emb.add_field(name="Fun commands", value="""
--------------------
$ping,
$8ball,
$hello,
$tsundere,
$flip,
$rps, (UNAVAILABLE)
$urban, (UNAVAILABLE)
$choose, (UNAVAILABLE)
$accept,





--------------------
""", inline=True)
        emb.set_image(url='https://i.imgur.com/MUzvy9j.png')
        emb.set_thumbnail(url='https://i.imgur.com/7Moz5io.png')
        await client.send_message(message.channel, embed=emb)

    elif message.content.startswith("$gone"):
        emb = (discord.Embed(title="My commands are in these 2 categories", url='https://justjeff-official.webnode.com/hatsune-miku-bot/', color=0x3f35f9))
        emb.add_field(name="So here are all my general commands", value='$commands, $construction, $invite, $jeff & $owner', inline=True)
        emb.add_field(name='These are all my fun commands', value='$ping, $8ball, $kiss, $meme, $hugs, $pat, $slap, $poke, $holdhands, $hello, $tsundere, $louise, $raziel, $sagiri, $miku & $koneko', inline=True)
        emb.set_author(name="Hatsune Miku Bot")
        emb.set_author(name="Hatsune Miku Bot", url='http://bit.ly/2G7mB7Y')
        emb.set_image(url='https://i.imgur.com/MUzvy9j.png')
        emb.set_thumbnail(url='https://i.imgur.com/7Moz5io.png')
        await client.send_message(message.channel, embed=emb)


    elif message.content.startswith("$construction"):
        emb = (discord.Embed(title="Here is everything listed that is under construction", url='https://justjeff-official.webnode.com/hatsune-miku-bot/', color=0x3f35f9))
        emb.add_field(name="I'm currently getting these new commands", value="I'm not getting new commands for now", inline=True)
        emb.add_field(name='These commands are getting an update', value='No commands are getting a update', inline=True)
        emb.add_field(name='Here are my most recently new commands', value='$poke, $pat & $slap', inline=True)
        emb.add_field(name='My most recently changed commands, check them out now', value='There is no command that got a change', inline=True)
        emb.set_author(name="Hatsune Miku Bot")
        emb.set_image(url='https://i.imgur.com/E7O1J7A.png')
        emb.set_thumbnail(url='https://i.imgur.com/7Moz5io.png')
        await client.send_message(message.channel, embed=emb)

    elif message.content.startswith("$invite"):
        emb = (discord.Embed(title="Hatsune Miku Bot", url='http://bit.ly/2G7mB7Y', color=0x3f35f9))
        emb.add_field(name='If you want me to join your server aswell please use this link', value='http://bit.ly/2G7mB7Y', inline=True)
        emb.add_field(name='Search my information on my official webpage', value='https://justjeff-official.webnode.com/hatsune-miku-bot/', inline=True)
        emb.set_image(url='https://i.imgur.com/i8lO032.png')
        await client.send_message(message.channel, "{0.author.mention}".format(message), embed=emb)

    elif message.content.startswith("$nightcore"):
        emb = (discord.Embed(title="Janieck - Does It Matter [NightCore]", url='https://youtu.be/SkPuP6VglhQ', description="Ever wanted to just have some Little Talks with someone?", color=0x3f35f9))
        emb.add_field(name='Subscribe to my channel', value='https://www.youtube.com/c/JustJeff9924', inline=True)
        emb.add_field(name='Make sure to watch the new video', value='https://youtu.be/SkPuP6VglhQ', inline=True)
        emb.set_author(name="JustJeff Official NightCore", url='https://www.youtube.com/c/JustJeff9924')
        emb.set_image(url='https://i.imgur.com/7wgVrPZ.jpg')
        emb.set_thumbnail(url='https://i.imgur.com/We7bHyU.jpg')
        await client.send_message(message.channel, "@everyone", embed=emb)

    elif message.content.startswith("$jeff"):
        emb = (discord.Embed(title="Janieck - Does It Matter [NightCore]", url='https://youtu.be/SkPuP6VglhQ', description="Ever wanted to just have some Little Talks with someone?", color=0x3f35f9))
        emb.add_field(name='Subscribe to my channel', value='https://www.youtube.com/c/JustJeff9924', inline=True)
        emb.add_field(name='Make sure to watch the new video', value='https://youtu.be/SkPuP6VglhQ', inline=True)
        emb.set_author(name="JustJeff Official NightCore", url='https://www.youtube.com/c/JustJeff9924')
        emb.set_image(url='https://i.imgur.com/7wgVrPZ.jpg')
        emb.set_thumbnail(url='https://i.imgur.com/We7bHyU.jpg')
        await client.send_message(message.channel, embed=emb)

    elif message.content.startswith("$lel"):
        emb = (discord.Embed(title="Your Reality [NightCore Unreleased]", url='https://soundcloud.com/justjeff-205750120/your-reality', description="Another Doki Doki song? Yes we have another one people. I hope you can enjoy this in Your Reality", color=0x3f35f9))
        emb.add_field(name='Be sure to follow my SoundCloud', value='https://soundcloud.com/justjeff-205750120', inline=True)
        emb.add_field(name='Listen to my latest song here', value='https://soundcloud.com/justjeff-205750120/your-reality', inline=True)
        emb.set_author(name="JustJeff Official Unreleased NightCores", url='https://soundcloud.com/justjeff-205750120')
        emb.set_image(url='https://i.imgur.com/K0qlynx.png')
        emb.set_thumbnail(url='https://i.imgur.com/We7bHyU.jpg')
        await client.send_message(message.channel, embed=emb)

    elif message.content.startswith("$soundcloud"):
        emb = (discord.Embed(title="Your Reality [NightCore Unreleased]", url='https://soundcloud.com/justjeff-205750120/your-reality', description="Another Doki Doki song? Yes we have another one people. I hope you can enjoy this in Your Reality", color=0x3f35f9)) 
        emb.add_field(name='Be sure to follow my SoundCloud', value='https://soundcloud.com/justjeff-205750120', inline=True)
        emb.add_field(name='Listen to my latest song here', value='https://soundcloud.com/justjeff-205750120/your-reality', inline=True)
        emb.set_author(name="JustJeff Official Unreleased NightCores", url='https://soundcloud.com/justjeff-205750120')
        emb.set_image(url='https://i.imgur.com/K0qlynx.png')
        emb.set_thumbnail(url='https://i.imgur.com/We7bHyU.jpg')
        await client.send_message(message.channel, "@everyone", embed=emb)

    elif message.content.startswith("$stream"):
        emb = (discord.Embed(title="NightCore + Anime Music", url='https://www.youtube.com/c/JustJeff9924/live', description="And we are live again everyone come and join in for the fun :3", color=0x3f35f9))
        emb.add_field(name='Subscribe to my channel', value='https://www.youtube.com/channel/UCmVBqm9zCXCLe_bLSBx23nQ', inline=True)
        emb.add_field(name='Watch the stream here', value='https://www.youtube.com/c/JustJeff9924/live', inline=True)
        emb.set_author(name="JustJeff Official NightCore", url='https://www.youtube.com/channel/UCmVBqm9zCXCLe_bLSBx23nQ')
        emb.set_image(url='https://i.imgur.com/jaq7C9G.jpg')
        emb.set_thumbnail(url='https://i.imgur.com/We7bHyU.jpg')
        await client.send_message(message.channel, "@everyone", embed=emb)

    elif message.content.startswith("$live"):
        emb = (discord.Embed(title="NightCore + Anime Music", url='https://www.youtube.com/c/JustJeff9924/live', description="And we are live again everyone come and join in for the fun :3", color=0x3f35f9))
        emb.add_field(name='Subscribe to my channel', value='https://www.youtube.com/channel/UCmVBqm9zCXCLe_bLSBx23nQ', inline=True)
        emb.add_field(name='Watch the stream here', value='https://www.youtube.com/c/JustJeff9924/live', inline=True)
        emb.set_author(name="JustJeff Official NightCore", url='https://www.youtube.com/channel/UCmVBqm9zCXCLe_bLSBx23nQ')
        emb.set_image(url='https://i.imgur.com/jaq7C9G.jpg')
        emb.set_thumbnail(url='https://i.imgur.com/We7bHyU.jpg')
        await client.send_message(message.channel, embed=emb)

    elif message.content.startswith("$ping"):
        await client.send_message(message.channel, "pong!")

    elif message.content.startswith("$accept"):
        await client.send_message(message.channel, "accept")

    elif message.content.startswith("$8ball"):
        await client.send_message(message.channel, random.choice ([":8ball: It is certain {0.author.mention}".format(message),
                                                                   ":8ball: It is decidedly so {0.author.mention}".format(message),
                                                                   ":8ball: Without a doubt {0.author.mention}".format(message),
                                                                   ":8ball: Yes definitely {0.author.mention}".format(message),
                                                                   ":8ball: You may rely on it {0.author.mention}".format(message),
                                                                   ":8ball: As I see it, yes {0.author.mention}".format(message),
                                                                   ":8ball: Most likely {0.author.mention}".format(message),
                                                                   ":8ball: Outlook good {0.author.mention}".format(message),
                                                                   ":8ball: Yes {0.author.mention}".format(message),
                                                                   ":8ball: Signs point to yes {0.author.mention}".format(message),
                                                                   ":8ball: Reply hazy try again {0.author.mention}".format(message),
                                                                   ":8ball: Ask again later {0.author.mention}".format(message),
                                                                   ":8ball: Better not tell you now {0.author.mention}".format(message),
                                                                   ":8ball: Cannot predict now {0.author.mention}".format(message),
                                                                   ":8ball: Concentrate and ask again {0.author.mention}".format(message),
                                                                   ":8ball: Don't count on it {0.author.mention}".format(message),
                                                                   ":8ball: My reply is no {0.author.mention}".format(message),
                                                                   ":8ball: My sources say no {0.author.mention}".format(message),
                                                                   ":8ball: Outlook not so good {0.author.mention}".format(message),
                                                                   ":8ball: Very doubtful {0.author.mention}".format(message)]))
        
    elif message.content.startswith("$hello"):
        await client.send_message(message.channel, random.choice (["Hello *hugs* {0.author.mention}".format(message),
                                                                   "Hii I missed you {0.author.mention}".format(message),
                                                                   "You want to talk to me?{0.author.mention}".format(message)]))
    elif message.content.startswith("$flip"):
        await client.send_message(message.channel, random.choice (["It is tails {0.author.mention}".format(message),
                                                                   "It is heads {0.author.mention}".format(message),
                                                                   "I threw it to high and lost the coin.. {0.author.mention}".format(message)]))
    
    elif message.content.startswith("$tsundere"):
        await client.send_message(message.channel, random.choice (["Why you talk to me? {0.author.mention}".format(message),
                                                                    "I want to slap you in the face right now.... {0.author.mention}".format(message),
                                                                    "You BAKA!!! {0.author.mention}".format(message),
                                                                    "Look guys its a pervert *points to* {0.author.mention}".format(message),
                                                                    "GET AWAY FROM ME PERV",
                                                                    "Why are you talking to me? BAKA!!!",
                                                                    "I'm not a tsundere!",
                                                                    "Stupid Octopus TAKE IT BACK!!",
                                                                    "It's not like I like you or anything"]))
        
    elif message.content.startswith("$koneko"):
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
        await client.send_message(message.channel, embed=emb)

    
    elif message.content.startswith("$louise"):
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
        await client.send_message(message.channel, embed=emb)


    elif message.content.startswith("$raziel"):
        emb = discord.Embed(description="Here is your Raziel pic")
        link = random.choice(["https://cdn.discordapp.com/attachments/364775449932333057/385546620709765124/001.png",
                                                                   "https://cdn.discordapp.com/attachments/364775449932333057/385546528573358081/Ashtar_V1.png",
                                                                   "https://cdn.discordapp.com/attachments/364775449932333057/385546477579141121/TRASHANDTRASH2.jpg",
                                                                   "https://cdn.discordapp.com/attachments/364775449932333057/385546444741804062/biohazard.png",
                                                                   "https://cdn.discordapp.com/attachments/364775449932333057/385546404766023680/Raziel.png",
                                                                   "https://cdn.discordapp.com/attachments/364775449932333057/385546397077864459/Raziel_x3.png"])
        emb.set_image(url=link)
        await client.send_message(message.channel, embed=emb)

    elif message.content.startswith("$meme"):
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
        await client.send_message(message.channel, embed=emb)

    elif message.content.startswith("$sagiri"):
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
        await client.send_message(message.channel, embed=emb)

    elif message.content.startswith("$miku"):
       emb = discord.Embed(description="The cute Hatsune Miku is here")
       link = random.choice(["https://i.imgur.com/hOxLRSd.jpg",
                                                                   "https://i.imgur.com/EgaUY6R.jpg",
                                                                   "https://imgur.com/JWkzplC",
                                                                   "https://imgur.com/6pNi4R5",
                                                                   "https://imgur.com/JdnOtLI",
                                                                   "https://imgur.com/JdnOtLI",
                                                                   "https://imgur.com/8hhD0GQ",
                                                                   "https://imgur.com/yB97wE2",
                                                                   "https://imgur.com/PAaB6n0",
                                                                   "https://imgur.com/yAKq051",
                                                                   "https://imgur.com/bKBvy8L",
                                                                   "https://imgur.com/1TAKYGG",
                                                                   "https://imgur.com/jtrdBR3",
                                                                   "https://imgur.com/1zFfMeD",
                                                                   "https://imgur.com/gnyKIHF",
                                                                   "https://imgur.com/N52IWUV",
                                                                   "https://imgur.com/L1egP2W",
                                                                   "https://imgur.com/hTMLVgD",
                                                                   "https://imgur.com/Gr3Oq7s",
                                                                   "https://imgur.com/gfS6nbJ",
                                                                   "https://imgur.com/BrvEP8C",
                                                                   "https://imgur.com/7RTX1Eq",
                                                                   "https://imgur.com/wem51aa",
                                                                   "https://imgur.com/WejSAoO",
                                                                   "https://imgur.com/s6OxozN",
                                                                   "https://imgur.com/m5jQvoD",
                                                                   "https://imgur.com/8VnNH6g",
                                                                   "https://imgur.com/T83rbUz",
                                                                   "https://imgur.com/rrEQPRf",
                                                                   "https://imgur.com/jqeCoYJ",
                                                                   "https://imgur.com/fnx9jMA",
                                                                   "https://imgur.com/59w3HB1",
                                                                   "https://imgur.com/gBKCnfI",
                                                                   "https://imgur.com/QGYNiIo"]))
        emb.set_image(url=link)
        await client.send_message(message.channel, embed=emb)

    elif message.content.startswith("$off"):
        await client.send_message(message.channel, random.choice (["Look it is us ^-^ https://imgur.com/y3tdypG",
                                                                   "Look it is us ^-^ https://imgur.com/4eU4Wn9",
                                                                   "Look it is us ^-^ https://imgur.com/mgT1X4T",
                                                                   "Look it is us ^-^ https://imgur.com/SeG9tXc",
                                                                   "Look it is us ^-^ https://imgur.com/MpurCUo",
                                                                   "Look it is us ^-^ https://imgur.com/Z46TeiM",
                                                                   "Look it is us ^-^ https://imgur.com/cZqmjsZ",
                                                                   "Look it is us ^-^ https://imgur.com/IEZnIsL",
                                                                   "Look it is us ^-^ https://imgur.com/WALrYnD",
                                                                   "Look it is us ^-^ https://imgur.com/wc5HRL4",
                                                                   "Look it is us ^-^ https://imgur.com/dSCOHLb",
                                                                   "Look it is us ^-^ https://imgur.com/U2lOMBA",
                                                                   "Look it is us ^-^ https://imgur.com/S0fhDJO",
                                                                   "Look it is us ^-^ https://imgur.com/T9MHbDU",
                                                                   "Look it is us ^-^ https://imgur.com/ykgQ4qQ",
                                                                   "Look it is us ^-^ https://imgur.com/hzsJq4a",
                                                                   "Look it is us ^-^ https://imgur.com/CK3Oowz",
                                                                   "Look it is us ^-^ https://imgur.com/4osXPJh",
                                                                   "Look it is us ^-^ https://imgur.com/mVQeJyq",
                                                                   "Look it is us ^-^ https://imgur.com/HAMu7Ta",
                                                                   "Look it is us ^-^ https://imgur.com/srIkCdw",
                                                                   "Look it is us ^-^ https://imgur.com/cBvoYhl",
                                                                   "Look it is us ^-^ https://imgur.com/XjObvOo",
                                                                   "Look it is us ^-^ https://imgur.com/qoUYrEy",
                                                                   "Look it is us ^-^ https://imgur.com/BzFMO3P",
                                                                   "Look it is us ^-^ https://imgur.com/cAbpS6i",
                                                                   "Look it is us ^-^ https://imgur.com/szNeq3O",
                                                                   "Look it is us ^-^ https://imgur.com/h9nZpPw",
                                                                   "Look it is us ^-^ https://imgur.com/5CZ3IoR",
                                                                   "Look it is us ^-^ https://imgur.com/lUkMc3y",
                                                                   "Look it is us ^-^ https://imgur.com/Nn7AJ3g",
                                                                   "Look it is us ^-^ https://imgur.com/vzNodIQ",
                                                                   "Look it is us ^-^ https://imgur.com/iVUZRfo",
                                                                   "Look it is us ^-^ https://imgur.com/5cPjWyg",
                                                                   "Look it is us ^-^ https://imgur.com/BSQ6iC0",
                                                                   "Look it is us ^-^ https://imgur.com/WO6calr",
                                                                   "Look it is us ^-^ https://imgur.com/FcuKrao",
                                                                   "Look it is us ^-^ https://imgur.com/URxMCuz",
                                                                   "Look it is us ^-^ https://imgur.com/UkgiPXo",
                                                                   "Look it is us ^-^ https://imgur.com/qez3ELD",
                                                                   "Look it is us ^-^ https://imgur.com/TlAY5Z9",
                                                                   "Look it is us ^-^ https://imgur.com/AZ6No95",
                                                                   "Look it is us ^-^ https://imgur.com/sbcBnzL",
                                                                   "Look it is us ^-^ https://imgur.com/vZoBTC9",
                                                                   "Look it is us ^-^ https://imgur.com/fUGbJbd",
                                                                   "Look it is us ^-^ https://imgur.com/M2Rz6JR",
                                                                   "Look it is us ^-^ https://imgur.com/xH12njq",
                                                                   "Look it is us ^-^ https://imgur.com/XyZMEa3",
                                                                   "Look it is us ^-^ https://imgur.com/Q8ZHssC",
                                                                   "Look it is us ^-^ https://imgur.com/ohZDIjM",
                                                                   "Look it is us ^-^ https://imgur.com/fOBuA0e",
                                                                   "Look it is us ^-^ https://imgur.com/UcTlLrr",
                                                                   "Look it is us ^-^ https://imgur.com/AGgrb7z",
                                                                   "Look it is us ^-^ https://imgur.com/7vdV96n",
                                                                   "Look it is us ^-^ https://imgur.com/bOVQJnb",
                                                                   "Look it is us ^-^ https://imgur.com/SCODeR7",
                                                                   "Look it is us ^-^ https://imgur.com/9VWTQPY",
                                                                   "Look it is us ^-^ https://imgur.com/hQx5O27",
                                                                   "Look it is us ^-^ https://imgur.com/zPWo9Tr",
                                                                   "Look it is us ^-^ https://imgur.com/0cvsrZe",
                                                                   "Look it is us ^-^ https://imgur.com/nKFTpIe",
                                                                   "Look it is us ^-^ https://imgur.com/W23c2AZ",
                                                                   "Look it is us ^-^ https://imgur.com/J7zgYK8",
                                                                   "Look it is us ^-^ https://imgur.com/xDMEOVu",
                                                                   "Look it is us ^-^ https://imgur.com/8Ujl07s",
                                                                   "Look it is us ^-^ https://imgur.com/VcbsZHT",
                                                                   "Look it is us ^-^ https://imgur.com/M0zfoS2",
                                                                   "Look it is us ^-^ https://imgur.com/Pn7Pcdv",
                                                                   "Look it is us ^-^ https://imgur.com/Rq6ZcPS",
                                                                   "Look it is us ^-^ https://imgur.com/7V5i350",
                                                                   "Look it is us ^-^ https://imgur.com/2LQM6MF",
                                                                   "Look it is us ^-^ https://imgur.com/z58tFPm",
                                                                   "Look it is us ^-^ https://imgur.com/FB4p6da",
                                                                   "Look it is us ^-^ https://imgur.com/6mkNZEL",
                                                                   "Look it is us ^-^ https://imgur.com/n3FseQM",
                                                                   "Look it is us ^-^ https://imgur.com/G0L7dPR",
                                                                   "Look it is us ^-^ https://imgur.com/Ygtl3Fp",
                                                                   "Look it is us ^-^ https://imgur.com/K3M7Lua",
                                                                   "Look it is us ^-^ https://imgur.com/qCpzSGV",
                                                                   "Look it is us ^-^ https://imgur.com/LFx1sE8",]))
    elif message.content.startswith("$hug"):
        await client.send_message(message.channel, random.choice (["Hugs you ^-^ https://media.giphy.com/media/sRFu8y27ZvWcizXvhZ/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/piJGRC4SI3rFlsStVl/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/82SkTj4bSjT3LK17aN/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/BcJfwkNSWdAMZv0y2L/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/jVSE3sJVOUcuzZznJC/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/1lzKzLZj8dUXtgFSfH/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/2yqY9Bdygw605n2XTm/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/Rdp6HU7FxCzJcY3prd/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/eRWjU2J4yjT0pF6ywJ/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/9A4W0NN8BiZpb6LtYD/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/2ldAtCluWk7SnhADah/giphy.gif ",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/9SJbgPae8TefXwTJaR/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/w90dBcoUJ6cmiPU4t0/giphy.gif ",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/67saFmcoRhMVhCMZGE/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/3JUQJcIfAXAArW1WTD/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/i3aOnVn3QsxV15XxjR/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/8mqyqIP1hzwqYbAlTe/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/fs6cAIqWSURaYsivXL/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/OQ6PuhOf2cWOmykOFw/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/fwZ2I44tp6k2iIPIgB/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/cGqd5kXxMnAOxdGyvI/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/55pQuLLEG9iRiTfJxq/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/2tRVAWkAaurGWlqBvq/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/cJp1WW2hhmCKQhD57y/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/2eKp6t0FLQpSfTU5hi/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/443fTfCKdEQetczXwz/giphy.gif ",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/3jcbb4FQAiWMixccTY/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/jKYZ1cGDAAqGiABTnr/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/1xOuBc46IUWBoyk5iJ/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/vuYRR4laYXZZi54Kim/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/2UoNzjBVZ5QbrB1ENp/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/lo5I76U8ttVydMVabW/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/2yqyGIrPMdAOZvRaNt/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/3vAez2QzXSL8ab8ifx/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/dADPOJLmQBkk6AKTXY/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/p44q3a6d5nKKfYR4Ew/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/7XAzpR8tqsRYT2NFwT/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/2UEMLpJl7wFDAJy4NO/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/5qFE15D17jjnCfkpMw/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/8qtS3KMrPiQ5wlrUjT/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/3E1z3JYvXyLMFvDlQ0/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/L0u0QnzfZau8sbfyxb/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/B2RwGCEwQ01U6eiPRy/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/jI7hArBTJZLCb6PHKU/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/2ZYNC5MSdVNqcl2C50/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/1g2BKT3zJKIwWTCqyS/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/4KFxreglNtYPS5rvyf/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/7XAzDHyZIgqpF2sjlT/giphy.gif ",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/apEqEGcf3dwvskwWQX/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/apEqEGcf3dwvskwWQX/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/9xlzgJC2Am0IkvEKa1/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/67sjq4IVef6ayVWSet/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/oziQAJ81KwoFAp5T6q/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/dCCYKqdZMUeXe8yqaq/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/557hpBLQofN06BmjuP/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/x0drGtyRolW2BoXvcp/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/1Qd2tVUEvC3QmyuI7D/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/c1bAPM6Pr9u8iRazVA/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/fQib0lJOBg3reMfwB0/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/26k800wkVDh7nVqXtk/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/5O77QGhfrz9T9ZzdFj/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/1yTcE3ywdK6f14AdBh/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/3l4bud9bjBocZqV2ea/giphy.gif",
                                                                   "Hugs you ^-^  https://media.giphy.com/media/fituC6UJqlIe5KWVZ0/giphy.gif",
                                                                   "Hugs you ^-^ https://media.giphy.com/media/etKfIRTv7yCJwhkZWf/giphy.gif"]))
                                                                   

    elif message.content.startswith("$holdhands"):
        await client.send_message(message.channel, random.choice (["Holds your hand ^^ https://media.giphy.com/media/Mn2QhV5RKVnDFPm3xS/giphy.gif",
                                                                   "Holds your hand ^^ https://media.giphy.com/media/XJbZUmQTozjeovfDj5/giphy.gif",
                                                                   "Holds your hand ^^ https://media.giphy.com/media/65ARJduu1Ayge6lbb1/giphy.gif",
                                                                   "Holds your hand ^^ https://media.giphy.com/media/2UH5JGSkV7bL9KPxns/giphy.gif",
                                                                   "Holds your hand ^^ https://media.giphy.com/media/836SlQqmguF97blW7Z/giphy.gif",
                                                                   "Holds your hand ^^ https://media.giphy.com/media/67SPxHsGYvZRjBvPVG/giphy.gif",
                                                                   "Holds your hand ^^ https://media.giphy.com/media/9GJ0TobPeqryujJKrx/giphy.gif",
                                                                   "Holds your hand ^^ https://media.giphy.com/media/1xkOTx6HQGHAlHhIJj/giphy.gif",
                                                                   "Holds your hand ^^ https://media.giphy.com/media/eB1n5v1AnJkhUam6rM/giphy.gif",
                                                                   "Holds your hand ^^ https://media.giphy.com/media/1rMZB4yEPp92SandyF/giphy.gif",
                                                                   "Holds your hand ^^ https://media.giphy.com/media/ksbxFxDu8nbl2ulbpP/giphy.gif",
                                                                   "Holds your hand ^^ https://media.giphy.com/media/cXZT5GVAUoMCIzifAM/giphy.gif",
                                                                   "Holds your hand ^^ https://media.giphy.com/media/m9rNHsYSVNtUzmg67j/giphy.gif",
                                                                   "Holds your hand ^^ https://media.giphy.com/media/51YdFcndAtxP6Gphmz/giphy.gif",
                                                                   "Please hold my hand ;-; https://media.giphy.com/media/cJk2CoSB0fLBxSpVJn/giphy.gif",
                                                                   "Holds your hand ^^ https://media.giphy.com/media/1miLExf9KIOihnq4Lo/giphy.gif",
                                                                   "Holds your hand ^^ https://media.giphy.com/media/1g2C2z64PRTqf6vQo5/giphy.gif",
                                                                   "Holds your hand ^^ https://media.giphy.com/media/vuPcWxM8f9HOOO9GPX/giphy.gif",
                                                                   "Holds your hand ^^ https://media.giphy.com/media/9rx8p3i2CLq6e42uCh/giphy.gif",
                                                                   "Holds your hand ^^ https://media.giphy.com/media/7vzDkVMCaFbazqyMma/giphy.gif",
                                                                   "Holds your hand ^^ https://media.giphy.com/media/31Q1ECNJI1iBSEO4zW/giphy.gif",
                                                                   "Holds your hand ^^ https://media.giphy.com/media/31Q1ECNJI1iBSEO4zW/giphy.gif",
                                                                   "Holds your hand ^^ https://media.giphy.com/media/521ZTNMaFn8zqF4yhQ/giphy.gif",
                                                                   "Dammit that hurted :rage: https://media.giphy.com/media/1BfBbUl1bsOKxeJCPo/giphy.gif",
                                                                   "Holds your hand ^^ https://media.giphy.com/media/1dKSVKfX0lm62obCp4/giphy.gif",
                                                                   "Holds your hand ^^ https://media.giphy.com/media/1Y6eL9Rfjozej34MY3/giphy.gif",
                                                                   "Holds your hand ^^ https://media.giphy.com/media/yvX1KHKIRBpETHGtna/giphy.gif",
                                                                   "Holds your hand ^^ https://media.giphy.com/media/1sxtTkXPJzzHT6AFae/giphy.gif",
                                                                   "Holds your hand ^^ https://media.giphy.com/media/83cZKqPesn1gUeYclY/giphy.gif",
                                                                   "Holds your hand ^^ https://media.giphy.com/media/KVoMsguO6PYPAm5r7n/giphy.gif",
                                                                   "Holds your hand ^^ https://media.giphy.com/media/2tOTUM0P3vgxLlmdq4/giphy.gif"]))

    elif message.content.startswith("$kiss"):
        await client.send_message(message.channel, random.choice (["Kisses you <3 https://media.giphy.com/media/3obegyJLaSb0tKPQXo/giphy.gif",
                                                                   "Kisses you <3 https://media.giphy.com/media/fdzUxG2NWezLFVftaZ/giphy.gif",
                                                                   "Kisses you <3 https://media.giphy.com/media/3YJ5pPYHLoQLQmrWOY/giphy.gif",
                                                                   "Kisses you <3 https://media.giphy.com/media/1AeQmDXYXmGjjE6TsD/giphy.gif",
                                                                   "Kisses you <3 https://media.giphy.com/media/9VrEcC9GOcySGFHDy0/giphy.gif",
                                                                   "Kisses you <3 https://media.giphy.com/media/jbKt8zyiHF3DXpaLUL/giphy.gif",
                                                                   "Kisses you <3 https://media.giphy.com/media/88iHJdUf0EtsAchNwq/giphy.gif",
                                                                   "Kisses you <3 https://media.giphy.com/media/ZgRg3qRXVhR5KV5UUu/giphy.gif",
                                                                   "Kisses you <3 https://media.giphy.com/media/2wh2c0jRNlILwMo0tC/giphy.gif",
                                                                   "Kisses you <3 https://media.giphy.com/media/fxdXBacyHlWAGQnUYB/giphy.gif",
                                                                   "Kisses you <3 https://media.giphy.com/media/1kJ6VcHPLmVtbR0N14/giphy.gif",
                                                                   "Kisses you <3 https://media.giphy.com/media/2aKGDxMliW5kGDZEkC/giphy.gif",
                                                                   "Kisses you <3 https://media.giphy.com/media/4HepfF109Gj550l4DQ/giphy.gif",
                                                                   "Kisses you <3 https://media.giphy.com/media/EBSSg7iBXuXc0ZzZhk/giphy.gif",
                                                                   "Kisses you <3 https://media.giphy.com/media/9V1KQxfnJyDMTGeCvF/giphy.gif",
                                                                   "Kisses you <3 https://media.giphy.com/media/55ojWaw7MGJhmY9VWy/giphy.gif",
                                                                   "Kisses you <3 https://media.giphy.com/media/1k2UWbInw3WwQc7hxc/giphy.gif"]))

    elif message.content.startswith("$poke"):
        await client.send_message(message.channel, random.choice (["I want you attention so POKE https://media.giphy.com/mttps://imedia/7mYTUOUy2C9yj1GSne/giphy.gif",
                                                                   "I want you attention so POKE https://media.giphy.com/media/felNRoKZ7NPqHq8p80/giphy.gif",
                                                                   "I want you attention so POKE https://media.giphy.com/media/4HeSM4bptLBWmblk2n/giphy.gif",
                                                                   "I want you attention so POKE https://media.giphy.com/media/BEtrjinjpm9sK9LkJC/giphy.gif",
                                                                   "I want you attention so POKE https://media.giphy.com/media/fnNxOVUcT8AVezEeCJ/giphy.gif",
                                                                   "I want you attention so POKE https://media.giphy.com/media/7OX3Qro0de2Ug32DmR/giphy.gif",
                                                                   "I want you attention so POKE https://media.giphy.com/media/WwYHLZjvFCDgvGvruf/giphy.gif",
                                                                   "I want you attention so POKE https://media.giphy.com/media/9xnLvIS8Icq3cO7mJs/giphy.gif",
                                                                   "I want you attention so POKE https://media.giphy.com/media/9Dxh33dCpmV6zIISsc/giphy.gif",
                                                                   "I want you attention so POKE https://media.giphy.com/media/2rAKI4mhXaqkREjvPz/giphy.gif",
                                                                   "I want you attention so POKE https://media.giphy.com/media/1UUbrUKuuktAm1hG6H/giphy.gif",
                                                                   "I want you attention so POKE https://media.giphy.com/media/2zco88UUE8QYEqsdnq/giphy.gif",
                                                                   "I want you attention so POKE https://media.giphy.com/media/MWKFXHNG6kNJzJO4Uu/giphy.gif",
                                                                   "I want you attention so POKE https://media.giphy.com/media/4VW0P8ZWiHBWQKlh2t/giphy.gif",
                                                                   "I want you attention so POKE https://media.giphy.com/media/AF1KNTsZRVFYphv8He/giphy.gif",
                                                                   "I want you attention so POKE https://media.giphy.com/media/PQu6uOHps00AQmMLYp/giphy.gif",
                                                                   "I want you attention so POKE https://media.giphy.com/media/2YgJrKrzFw4RbdZZxh/giphy.gif",
                                                                   "I want you attention so POKE https://media.giphy.com/media/jHZekGrRgfv9xG8B7m/giphy.gif",
                                                                   "I want you attention so POKE https://media.giphy.com/media/9FW5ThhXNgwyCjiSaJ/giphy.gif",
                                                                   "I want you attention so POKE https://media.giphy.com/media/2zoIgb6w9HsytCKqEd/giphy.gif",
                                                                   "I want you attention so POKE https://media.giphy.com/media/fMAah7ahN479IdlErV/giphy.gif",
                                                                   "I want you attention so POKE https://media.giphy.com/media/9DAxGRmfXt1klFZT8W/giphy.gif"]))

    elif message.content.startswith("$slap"):
        await client.send_message(message.channel, random.choice (["I'm so mad at you so SLAP!!! https://media.giphy.com/media/tJpCo5cufLkxSoU9xs/giphy.gif",
                                                                   "I'm so mad at you so SLAP!!! https://media.giphy.com/media/cdXxSGvi8QycANUTB1/giphy.gif",
                                                                   "I'm so mad at you so SLAP!!! https://media.giphy.com/media/cdXxSGvi8QycANUTB1/giphy.gif",
                                                                   "I'm so mad at you so SLAP!!! https://media.giphy.com/media/FPr9l7kxjzRAY19azB/giphy.gif",
                                                                   "I'm so mad at you so SLAP!!! https://media.giphy.com/media/xlcR377pGLWddI9hLt/giphy.gif",
                                                                   "I'm so mad at you so SLAP!!! https://media.giphy.com/media/cXRdGCxALzuLnbf1OA/giphy.gif",
                                                                   "I'm so mad at you so SLAP!!! https://media.giphy.com/media/jamNoHlHaympt3FL43/giphy.gif",
                                                                   "I'm so mad at you so SLAP!!! https://media.giphy.com/media/DC5qb6Nbs4YEh8lcjW/giphy.gif",
                                                                   "I'm so mad at you so SLAP!!! https://media.giphy.com/media/1kI8SJM0zil1p9dJ82/giphy.gif",
                                                                   "I'm so mad at you so SLAP!!! https://media.giphy.com/media/834khn5DXjuKwuLFn1/giphy.gif",
                                                                   "I'm so mad at you so SLAP!!! https://media.giphy.com/media/1lALe9y0IkAXCX1Aua/giphy.gif",
                                                                   "I'm so mad at you so SLAP!!! https://media.giphy.com/media/7JKIbWo4qi9mIfeerm/giphy.gif",
                                                                   "I'm so mad at you so SLAP!!! https://media.giphy.com/media/C9E3O8RiWRPlKtsRRp/giphy.gif",
                                                                   "I'm so mad at you so SLAP!!! https://media.giphy.com/media/jx6EHhNjCLK8nf8ROQ/giphy.gif",
                                                                   "I'm so mad at you so SLAP!!! https://media.giphy.com/media/29IeWmTsqElFIVj5cg/giphy.gif",
                                                                   "I'm so mad at you so SLAP!!! https://media.giphy.com/media/1VTF33XB2dBSTNecnH/giphy.gif",
                                                                   "I'm so mad at you so SLAP!!! https://media.giphy.com/media/cYoR0FNB7oFLOhp1FE/giphy.gif",
                                                                   "I'm so mad at you so SLAP!!! https://media.giphy.com/media/U8lT5R5g4RZ7EISvUR/giphy.gif",
                                                                   "I'm so mad at you so SLAP!!! https://media.giphy.com/media/u47uvxPZox0pq81Uuf/giphy.gif",
                                                                   "I'm so mad at you so SLAP!!! https://media.giphy.com/media/1woC1tiECuYElHc6os/giphy.gif",
                                                                   "I'm so mad at you so SLAP!!! https://media.giphy.com/media/OOigrw2Wwu4PVi9xSn/giphy.gif",
                                                                   "I'm so mad at you so SLAP!!! https://media.giphy.com/media/LpFoueq4zvz4tGTE9Y/giphy.gif",
                                                                   "I'm so mad at you so SLAP!!! https://media.giphy.com/media/1SDXMSKngJTvGKQhaM/giphy.gif",
                                                                   "I'm so mad at you so SLAP!!! https://media.giphy.com/media/3XAU2QmqlUvPQS6I0D/giphy.gif",
                                                                   "I'm so mad at you so SLAP!!! https://media.giphy.com/media/2xPSQb3NnvegY1qyPY/giphy.gif",
                                                                   "I'm so mad at you so SLAP!!! https://media.giphy.com/media/felNRoKZ7NPqHq8p80/giphy.gif"]))
        
    elif message.content.startswith("$pat"):
        await client.send_message(message.channel, random.choice (["There, there it's alright https://media.giphy.com/media/8BkpilCUQzCf2fdpiZ/giphy.gif",
                                                                   "There, there it's alright https://media.giphy.com/media/EpNd51E8KV9IvTlugk/giphy.gif",
                                                                   "There, there it's alright https://media.giphy.com/media/4TcHPtYkXxMimFluDV/giphy.gif",
                                                                   "There, there it's alright https://media.giphy.com/media/1Qi7DU0cpEgOMqlSHc/giphy.gif",
                                                                   "There, there it's alright https://media.giphy.com/media/fRakOz8PkVQ9QhURVG/giphy.gif",
                                                                   "There, there it's alright https://media.giphy.com/media/3d77xsH1i0Ipx7V6DW/giphy.gif",
                                                                   "There, there it's alright https://media.giphy.com/media/5YbSoel7MK5fekP4Tc/giphy.gif",
                                                                   "There, there it's alright https://media.giphy.com/media/1zlC3Vi6kBhowJznEj/giphy.gif",
                                                                   "There, there it's alright https://media.giphy.com/media/5tw5CTmLNDRAqeo9O6/giphy.gif",
                                                                   "There, there it's alright https://media.giphy.com/media/mnrNnsxQ2Yh8bAFDrH/giphy.gif",
                                                                   "There, there it's alright https://media.giphy.com/media/47D5afaVnaY9Ui6AvJ/giphy.gif",
                                                                   "There, there it's alright https://media.giphy.com/media/toWDEDevwQNZo3NAQl/giphy.gif",
                                                                   "There, there it's alright https://media.giphy.com/media/5YiGX9Vdv3GZXdJNw6/giphy.gif",
                                                                   "There, there it's alright https://media.giphy.com/media/ulK120XupD3Ei9pvyi/giphy.gif",
                                                                   "There, there it's alright https://media.giphy.com/media/ZO7nJvbaZtqSRvKTvN/giphy.gif",
                                                                   "There, there it's alright https://media.giphy.com/media/5sYyc1v7DIVKitX8GL/giphy.gif",
                                                                   "There, there it's alright https://media.giphy.com/media/1dPFnWNWXZYPPvq8CY/giphy.gif",
                                                                   "There, there it's alright https://media.giphy.com/media/ckTr4jtYggwpOmZtmr/giphy.gif",
                                                                   "There, there it's alright https://media.giphy.com/media/8ZkdwScCgdwLJRAxmO/giphy.gif",
                                                                   "There, there it's alright https://media.giphy.com/media/443DajoyrETzXzhi40/giphy.gif",
                                                                   "There, there it's alright https://media.giphy.com/media/21JyRmC4I74AU8157C/giphy.gif",
                                                                   "There, there it's alright https://media.giphy.com/media/5UI4v1zvStBl8U0Sl6/giphy.gif",
                                                                   "There, there it's alright https://media.giphy.com/media/3BjlOCKxEM7fyNtsfi/giphy.gif"]))
                                                                


    elif message.content.startswith("$popcorn"):
        await client.send_message(message.channel, random.choice ([":popcorn: anyone...? https://media.giphy.com/media/jnUJbfQ7atI2l8JxnC/giphy.gif",
                                                                   ":popcorn: anyone...? https://media.giphy.com/media/5th9AXWLduy8tiee79/giphy.gif",
                                                                   ":popcorn: anyone...? https://media.giphy.com/media/iOecBbnAoM7oBgj4Ql/giphy.gif",
                                                                   ":popcorn: anyone...? https://media.giphy.com/media/8FuLD7udi0LBMBtDXD/giphy.gif",
                                                                   ":popcorn: anyone...? https://media.giphy.com/media/3YHy2YmTrudO81XfHK/giphy.gif",
                                                                   ":popcorn: anyone...? https://media.giphy.com/media/iNKJcVp3cgQJtReV4z/giphy.gif",
                                                                   ":popcorn: anyone...? https://media.giphy.com/media/iNxi3EBgqXpQJNIOaF/giphy.gif",
                                                                   ":popcorn: anyone...? https://media.giphy.com/media/3ba6CBs83z90clOz5z/giphy.gif",
                                                                   ":popcorn: anyone...? https://media.giphy.com/media/1ipKDXGyl5oZJNVaHR/giphy.gif",
                                                                   ":popcorn: anyone...? https://media.giphy.com/media/m9cg2GSbQEsMSKWtwZ/giphy.gif",
                                                                   ":popcorn: anyone...? https://media.giphy.com/media/fHujNhh5BfDMymeG5r/giphy.gif",
                                                                   "T:popcorn: anyone...? https://media.giphy.com/media/RIW8aISkVsQH7AMBof/giphy.gif",
                                                                   ":popcorn: anyone...? https://media.giphy.com/media/8Ff4F0woCBDyEXDt7w/giphy.gif"]))

    elif message.content.startswith("$stfu"):
        await client.send_message(message.channel, random.choice (["JUST SHUT UP ALREADY!!!! https://media.giphy.com/media/65VK7kBbhHpsVgaBTd/giphy.gif",
                                                                   "JUST SHUT UP ALREADY!!!! https://media.giphy.com/media/7FgI8OGvQmJRO30LXV/giphy.gif",
                                                                   "JUST SHUT UP ALREADY!!!! https://media.giphy.com/media/1zJUxWUeLLWQ06qi0G/giphy.gif",
                                                                   "JUST SHUT UP ALREADY!!!! https://media.giphy.com/media/29HWHjBTvxkiAm9ejS/giphy.gif",
                                                                   "JUST SHUT UP ALREADY!!!! https://media.giphy.com/media/xiNWajyOVXqPzIipgp/giphy.gif",
                                                                   "JUST SHUT UP ALREADY!!!! https://media.giphy.com/media/2jvQ9tM6Ud5v5RfrjO/giphy.gif",
                                                                   "JUST SHUT UP ALREADY!!!! https://media.giphy.com/media/8vZU5CI9iM85mzmR2x/giphy.gif",
                                                                   "JUST SHUT UP ALREADY!!!! https://media.giphy.com/media/2UJnryid8eTqrRNHk5/giphy.gif",
                                                                   "JUST SHUT UP ALREADY!!!! https://media.giphy.com/media/c6W456VKZ7dQkTpUwH/giphy.gif",
                                                                   "JUST SHUT UP ALREADY!!!! https://media.giphy.com/media/lzDaZZpTAak9Lb8BtS/giphy.gif",
                                                                   "JUST SHUT UP ALREADY!!!! https://media.giphy.com/media/u0aX5a6x5NjGQif3f8/giphy.gif"]))


        
client.run("Mzg0NzA4OTQ2ODI2NjI1MDM1.DP2vpA.lkuzj_99tjAGqzDZfBaBhx9pF-g")
