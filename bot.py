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

    elif message.content.startswith("$gone"):
        emb = (discord.Embed(title="My commands are in these 3 categories", url='https://justjeff-official.webnode.com/hatsune-miku-bot/', color=0x3f35f9))
        emb.add_field(name="So here are all my general commands", value='$commands, $construction, $invite, $jeff, $serverinfo, $userinfo, $owner, $ban, $mute, $unmute, $kick, $cleanup and $contact', inline=True)
        emb.add_field(name='These are all my fun commands', value='$ping, $8ball, $kiss, $meme, $hugs, $pat, $slap, $poke, $holdhands, $hello, $tsundere, $flip, $rps, $urban, $choose, $gif, $gifr, $imgur, $louise, $raziel, $sagiri, $miku and $koneko', inline=True)
        emb.add_field(name='With these commands you can controll the music', value='$play, $pause, $resume, $prev, $repeat, $resume, $shuffle, $skip, $song, $stop $playlist and $queue', inline=True)
        emb.set_author(name="Hatsune Miku Bot")
        emb.set_author(name="Hatsune Miku Bot", url='http://bit.ly/2G7mB7Y')
        emb.set_image(url='https://i.imgur.com/MUzvy9j.png')
        emb.set_thumbnail(url='https://i.imgur.com/7Moz5io.png')
        await client.send_message(message.channel, embed=emb)

    elif message.content.startswith("$commands"):
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
        
    elif message.content.startswith("$."):
        await client.send_message(message.channel, random.choice (["Hello *hugs* {0.author.mention}".format(message),
                                                                   "Hii I missed you {0.author.mention}".format(message),
                                                                   "You want to talk to me?{0.author.mention}".format(message)]))
    elif message.content.startswith("$.."):
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
        await client.send_message(message.channel, random.choice (["Here is your Koneko pic {0.author.mention} https://cdn.discordapp.com/attachments/379675847747174410/379676169483583498/232c995f3a08b1f51d04f374dc8ad0ff98d64dda_hq.jpg".format(message),
                                                                  "Here is your Koneko pic {0.author.mention} https://cdn.discordapp.com/attachments/379675847747174410/379676170477764609/16bd8e7879ec7d52133e8d849e49facc259c04e7_hq.gif".format(message),
                                                                  "Here is your Koneko pic {0.author.mention} https://cdn.discordapp.com/attachments/379675847747174410/379676178497404929/81883a9ade5ae30bb40a8a82f197a4e3.jpg".format(message),
                                                                  "Here is your Koneko pic {0.author.mention} https://cdn.discordapp.com/attachments/379675847747174410/379676188156624906/305274.jpg".format(message),
                                                                  "Here is your Koneko pic {0.author.mention} https://cdn.discordapp.com/attachments/379675847747174410/379676203159912448/393882.jpg".format(message),
                                                                  "Here is your Koneko pic {0.author.mention} https://cdn.discordapp.com/attachments/379675847747174410/379676208306061312/715076.jpg".format(message),
                                                                  "Here is your Koneko pic {0.author.mention} https://cdn.discordapp.com/attachments/379675847747174410/379676213377237002/1306917.jpg".format(message),
                                                                  "Here is your Koneko pic {0.author.mention} https://cdn.discordapp.com/attachments/379675847747174410/379676219064451072/3363536-0032038455-Konek.jpg".format(message),
                                                                  "Here is your Koneko pic {0.author.mention} https://cdn.discordapp.com/attachments/379675847747174410/379676221249814558/3363703-7491654825-png-7.png".format(message),
                                                                  "Here is your Koneko pic {0.author.mention} https://cdn.discordapp.com/attachments/379675847747174410/379676246298198016/d375136cda3e741c050f03674f2451ec9e6791f0_hq.jpg".format(message),
                                                                  "Here is your Koneko pic {0.author.mention} https://cdn.discordapp.com/attachments/379675847747174410/379676255081070594/download.jpg".format(message),
                                                                  "Here is your Koneko pic {0.author.mention} https://cdn.discordapp.com/attachments/379675847747174410/379676259048751105/FJZI2KH.jpg".format(message),
                                                                  "Here is your Koneko pic {0.author.mention} https://cdn.discordapp.com/attachments/379675847747174410/379676263322877952/High_School_DD_Vol.4_Colored_LN_Illustration.jpg".format(message),
                                                                  "Here is your Koneko pic {0.author.mention} https://cdn.discordapp.com/attachments/379675847747174410/379676267999395851/how_draw_koneko-toujou_high_school_dxd_11.jpg".format(message),
                                                                  "Here is your Koneko pic {0.author.mention} https://cdn.discordapp.com/attachments/379675847747174410/379676270717435915/images_1.jpg".format(message),
                                                                  "Here is your Koneko pic {0.author.mention} https://cdn.discordapp.com/attachments/379675847747174410/379676276346060800/images.jpg".format(message),
                                                                  "Here is your Koneko pic {0.author.mention} https://cdn.discordapp.com/attachments/379675847747174410/379676290208497664/Koneko_finding_comfort_on_Isseis_Lap.gif".format(message),
                                                                  "Here is your Koneko pic {0.author.mention} https://cdn.discordapp.com/attachments/379675847747174410/379676291663921154/Koneko_Kawaiii_Chinadress_Render.png".format(message),
                                                                  "Here is your Koneko pic {0.author.mention} https://cdn.discordapp.com/attachments/379675847747174410/379676304020078592/Koneko_Nekomata_Form2_during_Loki_Battle.jpg".format(message),
                                                                  "Here is your Koneko pic {0.author.mention} https://cdn.discordapp.com/attachments/379675847747174410/379676306914148364/koneko_toujou_by_ashleyxoxrose-d9aebqu.jpg".format(message),
                                                                  "Here is your Koneko pic {0.author.mention} https://cdn.discordapp.com/attachments/379675847747174410/379676322399649794/Koneko-1.png".format(message),
                                                                  "Here is your Koneko pic {0.author.mention} https://cdn.discordapp.com/attachments/379675847747174410/379676331283316736/maxresdefault_1.jpg".format(message),
                                                                  "Here is your Koneko pic {0.author.mention} https://cdn.discordapp.com/attachments/379675847747174410/379676340737277952/maxresdefault.jpg".format(message)]))

    elif message.content.startswith("$louise"):
        await client.send_message(message.channel, random.choice (["Here is your Louise pic {0.author.mention} https://cdn.discordapp.com/attachments/379705513103065098/385525389356695590/zero_no_tsukaima_louise_francoise_le_blanc_de_la_valliere_siesta_girl_maid_wand_34325_602x339.jpg".format(message),
                                                                  "Here is your Louise pic {0.author.mention} https://cdn.discordapp.com/attachments/379705513103065098/385525385724690432/zero_no_tsukaima_louise_francoise_le_blanc_de_la_valliere_henrietta_de_tristain_girl_pose_look_36699.jpg".format(message),
                                                                  "Here is your Louise pic {0.author.mention} https://cdn.discordapp.com/attachments/379705513103065098/385525381391712256/zero_no_tsukaima_louise_francoise_le_blanc_de_la_valliere_girl_look_sky_39854_1920x1080.jpg".format(message),
                                                                  "Here is your Louise pic {0.author.mention} https://cdn.discordapp.com/attachments/379705513103065098/385525374907449344/zero_no_tsukaima_louise_francoise_le_blanc_de_la_valliere_girl_blush_waiter_37373_1920x1080.jpg".format(message),
                                                                  "Here is your Louise pic {0.author.mention} https://cdn.discordapp.com/attachments/379705513103065098/385525372613165056/Zero.no.Tsukaima.full.737362.jpg".format(message),
                                                                  "Here is your Louise pic {0.author.mention} https://cdn.discordapp.com/attachments/379705513103065098/385525364199260161/zero.jpg".format(message),
                                                                  "Here is your Louise pic {0.author.mention} https://cdn.discordapp.com/attachments/379705513103065098/385525359191392276/Zero_2.0.jpg".format(message),
                                                                  "Here is your Louise pic {0.author.mention} https://cdn.discordapp.com/attachments/379705513103065098/385525355152408576/xingyueyaoshi_zero_no_tsukaima_louise_francoise_le_blanc_de_la_valliere_girl_pink_hair_anger_35019_1.jpg".format(message),
                                                                  "Here is your Louise pic {0.author.mention} https://cdn.discordapp.com/attachments/379705513103065098/385525347321643008/tumblr_n0huf5iV5M1s4q4eyo1_500.jpg".format(message),
                                                                  "Here is your Louise pic {0.author.mention} https://cdn.discordapp.com/attachments/379675847747174410/379676246298198016/d375136cda3e741c050f03674f2451ec9e6791f0_hq.jpg".format(message),
                                                                  "Here is your Louise pic {0.author.mention} https://cdn.discordapp.com/attachments/379705513103065098/385525340912615434/e3d434d43ab3782cc76f2c9b1b26a893.jpg".format(message),
                                                                  "Here is your Louise pic {0.author.mention} https://cdn.discordapp.com/attachments/379705513103065098/385525333576777728/download.jpg".format(message),
                                                                  "Here is your Louise pic {0.author.mention} https://cdn.discordapp.com/attachments/379705513103065098/385525331257196554/c0671d675ffc90c43383ffd0df3092b9.gif".format(message),
                                                                  "Here is your Louise pic {0.author.mention} https://cdn.discordapp.com/attachments/379705513103065098/385525325867646977/c0bf6afda065af99c50ae7f3af18a434--jpg-wedding.jpg".format(message),
                                                                  "Here is your Louise pic {0.author.mention} https://cdn.discordapp.com/attachments/379705513103065098/385525321027420181/bc2ac117f53cc742a99e985ecb573eec.jpg".format(message),
                                                                  "Here is your Louise pic {0.author.mention} https://cdn.discordapp.com/attachments/379705513103065098/385525315859906560/b6b9ac28194d01e9d577791706e166c0.jpg".format(message),
                                                                  "Here is your Louise pic {0.author.mention} https://cdn.discordapp.com/attachments/379705513103065098/385525313460895754/848951.jpg".format(message),
                                                                  "Here is your Louise pic {0.author.mention} https://cdn.discordapp.com/attachments/379705513103065098/385525309421912070/696063.jpg".format(message),
                                                                  "Here is your Louise pic {0.author.mention} https://cdn.discordapp.com/attachments/379705513103065098/385525307806842881/321492.jpg".format(message),
                                                                  "Here is your Louise pic {0.author.mention} https://cdn.discordapp.com/attachments/379705513103065098/385525299636469761/128849.jpg".format(message),
                                                                  "Here is your Louise pic {0.author.mention} https://cdn.discordapp.com/attachments/379705513103065098/385525291990384641/128843.jpg".format(message),
                                                                  "Here is your Louise pic {0.author.mention} https://cdn.discordapp.com/attachments/379705513103065098/385525286055313408/109299.jpg".format(message),
                                                                  "Here is your Louise pic {0.author.mention} https://cdn.discordapp.com/attachments/379705513103065098/385525275955429400/8362be9d22567de77a5d850e39019c3a1332646235_full.png".format(message),
                                                                  "Here is your Louise pic {0.author.mention} https://cdn.discordapp.com/attachments/379705513103065098/385525268766392320/81aab12bc87e6dd65749e142ed0dacaa--favori-queen-of.jpg".format(message),
                                                                  "Here is your Louise pic {0.author.mention} https://cdn.discordapp.com/attachments/379705513103065098/385525263045361664/25fbe237485992c455da78a05ef5f7c6.jpg".format(message),
                                                                  "Here is your Louise pic {0.author.mention} https://cdn.discordapp.com/attachments/379705513103065098/385525259383603200/6mjHU.jpg".format(message)]))


    elif message.content.startswith("$raziel"):
        await client.send_message(message.channel, random.choice (["Here is your Raziel pic {0.author.mention} https://cdn.discordapp.com/attachments/364775449932333057/385546620709765124/001.png".format(message),
                                                                   "Here is your Raziel pic {0.author.mention} https://cdn.discordapp.com/attachments/364775449932333057/385546528573358081/Ashtar_V1.png".format(message),
                                                                   "Here is your Raziel pic {0.author.mention} https://cdn.discordapp.com/attachments/364775449932333057/385546477579141121/TRASHANDTRASH2.jpg".format(message),
                                                                   "Here is your Raziel pic {0.author.mention} https://cdn.discordapp.com/attachments/364775449932333057/385546444741804062/biohazard.png".format(message),
                                                                   "Here is your Raziel pic {0.author.mention} https://cdn.discordapp.com/attachments/364775449932333057/385546404766023680/Raziel.png".format(message),
                                                                   "Here is your Raziel pic {0.author.mention} https://cdn.discordapp.com/attachments/364775449932333057/385546397077864459/Raziel_x3.png".format(message)]))

    elif message.content.startswith("$meme"):
        await client.send_message(message.channel, random.choice (["The meme lord has spoken, {0.author.mention} https://i.imgur.com/dMb4EJh.jpg".format(message),
                                                                   "The meme lord has spoken, {0.author.mention} https://i.imgur.com/8DYtXvq.jpg".format(message),
                                                                   "The meme lord has spoken, {0.author.mention} https://i.imgur.com/9bwyTne.jpg".format(message),
                                                                   "The meme lord has spoken, {0.author.mention} https://i.imgur.com/Suhx5tF.jpg".format(message),
                                                                   "The meme lord has spoken, {0.author.mention} https://i.imgur.com/jYQbSTO.jpg".format(message),
                                                                   "The meme lord has spoken, {0.author.mention} https://i.imgur.com/L9JV5hv.jpg".format(message),
                                                                   "The meme lord has spoken, {0.author.mention} https://i.imgur.com/q0YBtGp.jpg".format(message),
                                                                   "The meme lord has spoken, {0.author.mention} https://i.imgur.com/uR4dcAT.jpg".format(message),
                                                                   "The meme lord has spoken, {0.author.mention} https://i.imgur.com/6YjueJn.jpg".format(message),
                                                                   "The meme lord has spoken, {0.author.mention} https://i.imgur.com/UZcaFCl.jpg".format(message),
                                                                   "The meme lord has spoken, {0.author.mention} https://i.imgur.com/JucUYo5.jpg".format(message),
                                                                   "The meme lord has spoken, {0.author.mention} https://i.imgur.com/1662G65.jpg".format(message),
                                                                   "The meme lord has spoken, {0.author.mention} https://i.imgur.com/yjjy8xE.jpg".format(message),
                                                                   "The meme lord has spoken, {0.author.mention} https://i.imgur.com/kG05ZoV.jpg".format(message),
                                                                   "The meme lord has spoken, {0.author.mention} https://i.imgur.com/V4TA0kQ.jpg".format(message),
                                                                   "The meme lord has spoken, {0.author.mention} https://i.imgur.com/5GozBs9.jpg".format(message),
                                                                   "The meme lord has spoken, {0.author.mention} https://i.imgur.com/JYVZMSM.jpg".format(message),
                                                                   "The meme lord has spoken, {0.author.mention} https://i.imgur.com/9qn66Xd.jpg".format(message),
                                                                   "The meme lord has spoken, {0.author.mention} https://i.imgur.com/B5jLmvs.jpg".format(message),
                                                                   "The meme lord has spoken, {0.author.mention} https://i.imgur.com/1pbBJFK.jpg".format(message),
                                                                   "The meme lord has spoken, {0.author.mention} https://i.imgur.com/KtUxPnN.jpg".format(message),
                                                                   "The meme lord has spoken, {0.author.mention} https://i.imgur.com/jOIeIuH.jpg".format(message),
                                                                   "The meme lord has spoken, {0.author.mention} https://i.imgur.com/nqJDdd3.jpg".format(message),
                                                                   "The meme lord has spoken, {0.author.mention} https://i.imgur.com/JPxtdHU.jpg".format(message)]))

    elif message.content.startswith("$sagiri"):
        await client.send_message(message.channel, random.choice (["Here is the loli Sagiri {0.author.mention} https://imgur.com/xKAGGcl".format(message),
                                                                   "Here is the loli Sagiri {0.author.mention} https://imgur.com/YUaJcnm".format(message),
                                                                   "Here is the loli Sagiri {0.author.mention} https://imgur.com/JaNophQ".format(message),
                                                                   "I just got to say YEAH! {0.author.mention} https://imgur.com/8D5kYgX".format(message),
                                                                   "Are you just as happy as me? {0.author.mention} https://imgur.com/SMSI6R7".format(message),
                                                                   "Here is the loli Sagiri {0.author.mention} https://imgur.com/FnUhpe5".format(message),
                                                                   "Can you draw like me? {0.author.mention} https://imgur.com/iKELRa5".format(message),
                                                                   "You can hear me now right... {0.author.mention} https://imgur.com/wLruw7d".format(message),
                                                                   "I'm cold could you hold me? {0.author.mention} https://imgur.com/9NjjuKR".format(message),
                                                                   "Come dance with me!! {0.author.mention} https://imgur.com/0M0gZTS".format(message),
                                                                   "Dont stare at me ^////^ {0.author.mention} https://imgur.com/aypPW42".format(message),
                                                                   "BAKA!! {0.author.mention} https://imgur.com/I9gZJId".format(message),
                                                                   "Here is the loli Sagiri {0.author.mention} https://imgur.com/Y0zocc6".format(message),
                                                                   "Me and the gang ^^ {0.author.mention} https://imgur.com/vprV2v2".format(message),
                                                                   "I'm tired... {0.author.mention} https://imgur.com/beV26N0".format(message),
                                                                   "Be mean and I scratch you!! {0.author.mention} https://imgur.com/AL2cLb4".format(message),
                                                                   "Here is the loli Sagiri {0.author.mention} https://imgur.com/Q4eaRTI".format(message),
                                                                   "Here is the loli Sagiri {0.author.mention} https://imgur.com/IM0Z0Ge".format(message),
                                                                   "I will wash my own clothes this time Onii-Chan {0.author.mention} https://imgur.com/7wmpxtSg".format(message),
                                                                   "Give me one weird look and I shall kill you!! {0.author.mention} https://imgur.com/a6SJlNr".format(message),
                                                                   "Here is the loli Sagiri {0.author.mention} https://imgur.com/vJDPC9p".format(message),
                                                                   "Here is the loli Sagiri {0.author.mention} https://imgur.com/hchSSR3".format(message),
                                                                   "I'm so happy! {0.author.mention} https://imgur.com/lc4fdgR".format(message),
                                                                   "Wait am I mixed with Sistine now O.O {0.author.mention} https://imgur.com/mBuArvz".format(message),
                                                                   "That look I give to you... {0.author.mention} https://imgur.com/HnaGeG3".format(message),
                                                                   "Here is the loli Sagiri {0.author.mention} https://imgur.com/cOEnroW".format(message),
                                                                   "Here is the loli Sagiri {0.author.mention} https://imgur.com/LrfLhOY".format(message),
                                                                   "Here is the loli Sagiri {0.author.mention} https://imgur.com/XINvpdU".format(message),
                                                                   "Here is the loli Sagiri {0.author.mention} https://imgur.com/JKGN24g".format(message),
                                                                   "Me when I decide to go outisde... {0.author.mention} https://imgur.com/pHubVdF".format(message),
                                                                   "ONII-CHAN {0.author.mention} https://imgur.com/Am3eN1p".format(message),
                                                                   "Dont look to me like that Onii-Chan {0.author.mention} https://imgur.com/ZCxl0k1".format(message),
                                                                   "Here is the loli Sagiri {0.author.mention} https://imgur.com/92Telnz".format(message),
                                                                   "Onii-Chan you PERV! {0.author.mention} https://imgur.com/6x99vKd".format(message),
                                                                   "Here is the loli Sagiri {0.author.mention} https://imgur.com/qwhcxxc".format(message),
                                                                   "I shall kill you for looking at me weird {0.author.mention} https://imgur.com/lCQNE8a".format(message),
                                                                   "The gang and I {0.author.mention} https://imgur.com/LgOZknI".format(message),
                                                                   "The gang and I {0.author.mention} https://imgur.com/atWgvAV".format(message),
                                                                   "My plushie not yours.... {0.author.mention} https://imgur.com/yX5lKy9".format(message),
                                                                   "Here is the loli Sagiri {0.author.mention} https://imgur.com/7Weg9LQ".format(message),
                                                                   "Me when I was just a little kid {0.author.mention} https://imgur.com/kBRINe0".format(message),
                                                                   "Here is the loli Sagiri {0.author.mention} https://imgur.com/Q2Ikkh1".format(message),
                                                                   "I'm so happy with you Onii-Chan {0.author.mention} https://imgur.com/ParrGKy".format(message),
                                                                   "Here is the loli Sagiri {0.author.mention} https://imgur.com/msP0baI".format(message),
                                                                   "Me is so happy in this picture {0.author.mention} https://imgur.com/fomPhuE".format(message),
                                                                   "Here is the loli Sagiri {0.author.mention} https://imgur.com/FDGdFZC".format(message),
                                                                   "Here is the loli Sagiri {0.author.mention} https://imgur.com/JwWUpqe".format(message),
                                                                   "Here is the loli Sagiri {0.author.mention} https://imgur.com/MhVAQUF".format(message),
                                                                   "Here is the loli Sagiri {0.author.mention} https://imgur.com/ul02JYY".format(message),
                                                                   "Here is the loli Sagiri {0.author.mention} https://imgur.com/tXTS0Tg".format(message),
                                                                   "Here is the loli Sagiri {0.author.mention} https://imgur.com/XsA4rpc".format(message)]))

    elif message.content.startswith("$miku"):
        await client.send_message(message.channel, random.choice (["The cute Hatsune Miku is here {0.author.mention} https://imgur.com/hOxLRSd".format(message),
                                                                   "The cute Hatsune Miku is here {0.author.mention} https://imgur.com/EgaUY6R".format(message),
                                                                   "The cute Hatsune Miku is here {0.author.mention} https://imgur.com/JWkzplC".format(message),
                                                                   "The cute Hatsune Miku is here {0.author.mention} https://imgur.com/6pNi4R5".format(message),
                                                                   "The cute Hatsune Miku is here {0.author.mention} https://imgur.com/JdnOtLI".format(message),
                                                                   "The cute Hatsune Miku is here {0.author.mention} https://imgur.com/JdnOtLI".format(message),
                                                                   "The cute Hatsune Miku is here {0.author.mention} https://imgur.com/8hhD0GQ".format(message),
                                                                   "The cute Hatsune Miku is here {0.author.mention} https://imgur.com/yB97wE2".format(message),
                                                                   "The cute Hatsune Miku is here {0.author.mention} https://imgur.com/PAaB6n0".format(message),
                                                                   "The cute Hatsune Miku is here {0.author.mention} https://imgur.com/yAKq051".format(message),
                                                                   "The cute Hatsune Miku is here {0.author.mention} https://imgur.com/bKBvy8L".format(message),
                                                                   "The cute Hatsune Miku is here {0.author.mention} https://imgur.com/1TAKYGG".format(message),
                                                                   "The cute Hatsune Miku is here {0.author.mention} https://imgur.com/jtrdBR3".format(message),
                                                                   "The cute Hatsune Miku is here {0.author.mention} https://imgur.com/1zFfMeD".format(message),
                                                                   "The cute Hatsune Miku is here {0.author.mention} https://imgur.com/gnyKIHF".format(message),
                                                                   "The cute Hatsune Miku is here {0.author.mention} https://imgur.com/N52IWUV".format(message),
                                                                   "The cute Hatsune Miku is here {0.author.mention} https://imgur.com/L1egP2W".format(message),
                                                                   "The cute Hatsune Miku is here {0.author.mention} https://imgur.com/hTMLVgD".format(message),
                                                                   "The cute Hatsune Miku is here {0.author.mention} https://imgur.com/Gr3Oq7s".format(message),
                                                                   "The cute Hatsune Miku is here {0.author.mention} https://imgur.com/gfS6nbJ".format(message),
                                                                   "The cute Hatsune Miku is here {0.author.mention} https://imgur.com/BrvEP8C".format(message),
                                                                   "The cute Hatsune Miku is here {0.author.mention} https://imgur.com/7RTX1Eq".format(message),
                                                                   "The cute Hatsune Miku is here {0.author.mention} https://imgur.com/wem51aa".format(message),
                                                                   "The cute Hatsune Miku is here {0.author.mention} https://imgur.com/WejSAoO".format(message),
                                                                   "The cute Hatsune Miku is here {0.author.mention} https://imgur.com/s6OxozN".format(message),
                                                                   "The cute Hatsune Miku is here {0.author.mention} https://imgur.com/m5jQvoD".format(message),
                                                                   "The cute Hatsune Miku is here {0.author.mention} https://imgur.com/8VnNH6g".format(message),
                                                                   "The cute Hatsune Miku is here {0.author.mention} https://imgur.com/T83rbUz".format(message),
                                                                   "The cute Hatsune Miku is here {0.author.mention} https://imgur.com/rrEQPRf".format(message),
                                                                   "The cute Hatsune Miku is here {0.author.mention} https://imgur.com/jqeCoYJ".format(message),
                                                                   "The cute Hatsune Miku is here {0.author.mention} https://imgur.com/fnx9jMA".format(message),
                                                                   "The cute Hatsune Miku is here {0.author.mention} https://imgur.com/59w3HB1".format(message),
                                                                   "The cute Hatsune Miku is here {0.author.mention} https://imgur.com/gBKCnfI".format(message),
                                                                   "The cute Hatsune Miku is here {0.author.mention} https://imgur.com/QGYNiIo".format(message)]))

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

    elif message.content.startswith("$hugs"):
        await client.send_message(message.channel, random.choice (["Hugs you ^-^ https://imgur.com/1Cnmqjl",
                                                                   "Hugs you ^-^ https://imgur.com/clDkQuR",
                                                                   "Hugs you ^-^ https://imgur.com/T9CVfaZ",
                                                                   "Hugs you ^-^ https://imgur.com/fow0Zzm",
                                                                   "Hugs you ^-^ https://imgur.com/JIx1REY",
                                                                   "Hugs you ^-^ https://imgur.com/lKrYsP2",
                                                                   "Hugs you ^-^ https://imgur.com/BT4AsTb",
                                                                   "Hugs you ^-^ https://imgur.com/HWO6NEu",
                                                                   "Hugs you ^-^ https://imgur.com/ck2G2jL",
                                                                   "Hugs you ^-^ https://imgur.com/Hq6IpXV",
                                                                   "Hugs you ^-^ https://imgur.com/fVLRx3c",
                                                                   "Hugs you ^-^ https://imgur.com/44r5Gle",
                                                                   "Hugs you ^-^ https://imgur.com/Kc8vJ6b",
                                                                   "Hugs you ^-^ https://imgur.com/nc7Js5I",
                                                                   "Hugs you ^-^ https://imgur.com/T7lrD6q",
                                                                   "Hugs you ^-^ https://imgur.com/Zbwsq1K",
                                                                   "Hugs you ^-^ https://imgur.com/c9EDyd0",
                                                                   "Hugs you ^-^ https://imgur.com/tmR1WA3",
                                                                   "Hugs you ^-^ https://imgur.com/o5jcgw7",
                                                                   "Hugs you ^-^ https://imgur.com/fOcrnW8",
                                                                   "Hugs you ^-^ https://imgur.com/XirHk6h",
                                                                   "Hugs you ^-^ https://imgur.com/aFog6a8",
                                                                   "Hugs you ^-^ https://imgur.com/s5uPOi6",
                                                                   "Hugs you ^-^ https://imgur.com/tAG0Esb",
                                                                   "Hugs you ^-^ https://imgur.com/AMLeiSg",
                                                                   "Hugs you ^-^ https://imgur.com/tMx6k44",
                                                                   "Hugs you ^-^ https://imgur.com/RReS9Lo",
                                                                   "Hugs you ^-^ https://imgur.com/ja90Q1P",
                                                                   "Hugs you ^-^ https://imgur.com/0kfiTXx",
                                                                   "Hugs you ^-^ https://imgur.com/0b6ApFi",
                                                                   "Hugs you ^-^ https://imgur.com/bzNCj3p",
                                                                   "Hugs you ^-^ https://imgur.com/LDN7SAZ",
                                                                   "Hugs you ^-^ https://imgur.com/zcvwIkx",
                                                                   "Hugs you ^-^ https://imgur.com/2Ihh3qR",
                                                                   "Hugs you ^-^ https://imgur.com/kYXvIzN",
                                                                   "Hugs you ^-^ https://imgur.com/5Eydwlf",
                                                                   "Hugs you ^-^ https://imgur.com/vxsGjIS",
                                                                   "Hugs you ^-^ https://imgur.com/j3KgmM3",
                                                                   "Hugs you ^-^ https://imgur.com/g5mryMC",
                                                                   "Hugs you ^-^ https://imgur.com/zM76iMy",
                                                                   "Hugs you ^-^ https://imgur.com/x7kLBTG",
                                                                   "Hugs you ^-^ https://imgur.com/VMKxUyh",
                                                                   "Hugs you ^-^ https://imgur.com/rcToOno",
                                                                   "Hugs you ^-^ https://imgur.com/nRYFBlD",
                                                                   "Hugs you ^-^ https://imgur.com/ykVxevt",
                                                                   "Hugs you ^-^ https://imgur.com/4bgsaLs",
                                                                   "Hugs you ^-^ https://imgur.com/neG2Ik7",
                                                                   "Hugs you ^-^ https://imgur.com/bGA0OBZ",
                                                                   "Hugs you ^-^ https://imgur.com/76fWYLz",
                                                                   "Hugs you ^-^ https://imgur.com/Pdebgro",
                                                                   "Hugs you ^-^ https://imgur.com/meJLSjx",
                                                                   "Hugs you ^-^ https://imgur.com/fuLzIK7",
                                                                   "Hugs you ^-^ https://imgur.com/wbQXWcA",
                                                                   "Hugs you ^-^ https://imgur.com/lfKBFla",
                                                                   "Hugs you ^-^ https://imgur.com/dCXBLhw",
                                                                   "Hugs you ^-^ https://imgur.com/w2SlioR",
                                                                   "Hugs you ^-^ https://imgur.com/uknfctH",
                                                                   "Hugs you ^-^ https://imgur.com/eZ1i7LY",
                                                                   "Hugs you ^-^ https://imgur.com/DWMAKTX",
                                                                   "Hugs you ^-^ https://imgur.com/zrmvc9l",
                                                                   "Hugs you ^-^ https://imgur.com/CmKoHkH",
                                                                   "Hugs you ^-^ https://imgur.com/btIhY9R",
                                                                   "Hugs you ^-^ https://imgur.com/QTGv16b",
                                                                   "Hugs you ^-^ https://imgur.com/7Z2Mhq1",
                                                                   "Hugs you ^-^ https://imgur.com/dX0slho",
                                                                   "Hugs you ^-^ https://imgur.com/ZkkzDgT",
                                                                   "Hugs you ^-^ https://imgur.com/GWlcZck"]))

    elif message.content.startswith("$holdhands"):
        await client.send_message(message.channel, random.choice (["Holds your hand ^^ https://imgur.com/ItuonVA",
                                                                   "Holds your hand ^^ https://imgur.com/B5DiHKI",
                                                                   "Holds your hand ^^ https://imgur.com/vztQjW0",
                                                                   "Holds your hand ^^ https://imgur.com/YFQddHY",
                                                                   "Holds your hand ^^ https://imgur.com/UWMfGcX",
                                                                   "Holds your hand ^^ https://imgur.com/UzBUTza",
                                                                   "Holds your hand ^^ https://imgur.com/ArNfnNf",
                                                                   "Holds your hand ^^ https://imgur.com/HkLyCIt",
                                                                   "Holds your hand ^^ https://imgur.com/LbWnrPZ",
                                                                   "Holds your hand ^^ https://imgur.com/yBnRpb8",
                                                                   "Holds your hand ^^ https://imgur.com/XLD5hK2",
                                                                   "Holds your hand ^^ https://imgur.com/bzlauYH",
                                                                   "Holds your hand ^^ https://imgur.com/MOJdEIq",
                                                                   "Holds your hand ^^ https://imgur.com/YJSJLGk",
                                                                   "Please hold my hand ;-; https://imgur.com/7dtM43d",
                                                                   "Holds your hand ^^ https://imgur.com/97jf9EA",
                                                                   "Holds your hand ^^ https://imgur.com/1QzdbRx",
                                                                   "Holds your hand ^^ https://imgur.com/h93vx9O",
                                                                   "Holds your hand ^^ https://imgur.com/bfiCKjy",
                                                                   "Holds your hand ^^ https://imgur.com/60PTrhk",
                                                                   "Holds your hand ^^ https://imgur.com/njU70Hb",
                                                                   "Holds your hand ^^ https://imgur.com/yrDyrEZ",
                                                                   "Holds your hand ^^ https://imgur.com/kCGMyrB",
                                                                   "Dont hold my hand :rage: https://imgur.com/nIfuALR",
                                                                   "Holds your hand ^^ https://imgur.com/4UlBx8z",
                                                                   "Holds your hand ^^ https://imgur.com/X2WZcRg",
                                                                   "Holds your hand ^^ https://imgur.com/Dhfqynl",
                                                                   "Holds your hand ^^ https://imgur.com/Rg0rwUg",
                                                                   "Holds your hand ^^ https://imgur.com/SuRD68X",
                                                                   "Holds your hand ^^ https://imgur.com/W5aUN5e",
                                                                   "Holds your hand ^^ https://imgur.com/yl0CoHB",
                                                                   "Holds your hand ^^ https://imgur.com/kfnnfAK",
                                                                   "Holds your hand ^^ https://imgur.com/YAxbO8j",
                                                                   "Holds your hand ^^ https://imgur.com/UVARqUO",
                                                                   "Holds your hand ^^ https://imgur.com/AxM32T3"]))

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
                                                                

    elif message.content.startswith("$test"):
        await client.send_message(message.channel, random.choice (["https://i.imgur.com/aRXAIXr.gifv"]))
        
client.run("Mzg0NzA4OTQ2ODI2NjI1MDM1.DP2vpA.lkuzj_99tjAGqzDZfBaBhx9pF-g")
        
client.login(os.environ.get("BOT_TOKEN"))
