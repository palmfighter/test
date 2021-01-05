
import asyncio
import random
import discord
from random import choice 
from discord.ext import commands, tasks
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO
from random import choice

bot = commands.Bot(command_prefix='!t')
again_true = False

bot.remove_command('help')

@bot.command()
async def ping(ctx):
	await ctx.send('pong')

@bot.command()
async def h(ctx):
    await ctx.send("'play <songname>' or 'p <songname>' --> Play a song")
    await ctx.send("'pause' or 'pp' --> Pause the song")
    await ctx.send("'resume' or 'pr' --> Resume the song")
    await ctx.send("'looptrack' or 'lt' --> Loops the current song - beta")
    await ctx.send("'dc' --> disconnect me from the voice channel")

@bot.command()
async def smash(ctx):

	rando = random.randint(1, 10)
	if rando < 6:
		await ctx.send('Awww, you missed the smash, there goes your chance....')
	if rando > 8:
		await ctx.send('Good job! You smashed perfectly! He did not stand a chance')
	if rando >= 6 and rando <= 8:
		again_true == True
		await ctx.send('You smashed! But he blocked it.....type !tagain')
		await bot.smash(ctx)
@bot.command()
async def again(ctx):
		rando = random.randint(1, 10) 
		if rando < 6:
                	await ctx.send('Awww, you missed the smash, there goes your second chance...')
		if rando > 6:
                	await ctx.send('Good job! You smashed perfectly! He did not stand your second blow')


@bot.event
async def on_ready():
	change_status.start()
	print('Bot online.')


@bot.command(pass_context=True)
async def help(ctx):
	author = ctx.message.author

	embed = discord.Embed(
		colour = discord.Colour.red()
	)
	embed.set_author(name='Help')
	embed.add_field(name='!tping', value='Returns Pong', inline=False)
	embed.add_field(name='!tsmash', value='Smash the ball!', inline=False)
	embed.add_field(name='!tavatar + @USER', value="Show the mentioned user's avatar", inline=False)
	embed.add_field(name='!tmatch + 2 @USERS', value='Play and see who would win a match of table tennis.', inline=False)

	await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def avatar(ctx, *, member: discord.Member=None): # set the member object to None
    if not member: # if member is no mentioned
        member = ctx.message.author # set member as the author
    userAvatar = member.avatar_url
    await ctx.send(userAvatar)

@bot.command()
async def match(ctx, member: discord.Member, member2: discord.Member=None): # set the member object $
    if not member: # if member is no mentioned
        member = ctx.message.author # set member as the author
    luck = random.randint(1,2)
    lost = random.randint(0,9)
    revive = 0
    revive2 = 0

    if luck == 1:
         revive = 11
         revive2 = lost
         gewon = True
    if luck == 2:
         revive2 = 11
         revive = lost
         gewon = False



    author = ctx.message.author

    embed = discord.Embed(
                colour = discord.Colour.red()
    )

    userAvatar = member.avatar_url_as(size=128)
    userAvatar2 = member2.avatar_url_as(size=128)

    wanted = Image.open("download2.jpeg")
    data = BytesIO(await userAvatar.read())
    pfp = Image.open(data)

    pfp = pfp.resize((312,312))
    wanted.paste(pfp, (60,600))
    data2 = BytesIO(await userAvatar2.read())
    pfp2 = Image.open(data2)
    pfp2 = pfp2.resize((312, 312))
    wanted.paste(pfp2, (974,600))


    wanted.save("lmao.jpg")
    image = Image.open("lmao.jpg")
    draw = ImageDraw.Draw(image)
    font_type = ImageFont.truetype('Anton-Regular.ttf',250)
    font_type2 = ImageFont.truetype('Anton-Regular.ttf',150)

    draw.text((130, 250),f"{revive}",fill=(0,0, 0), font=font_type)
    draw.text((1050, 250),f"{revive2}",fill=(0,0, 0), font=font_type)
    if gewon == True:
       draw.text((275, 30),f"{member.display_name} Won!",fill=(0,0, 0), font=font_type2)
    if gewon == False:
       draw.text((275,30),f"{member2.display_name} Won!",fill=(0,0,0), font=font_type2)
    image.save("lmao2.jpg")

    embed.set_author(name=f'{member.display_name} vs {member2.display_name}', icon_url=ctx.author.avatar_url)
    file = discord.File("/home/pi/lmao2.jpg", filename="image.jpg")
    embed.set_image(url="attachment://image.jpg")
    if gewon == True:
       embed.add_field(name=f'{member.display_name} Won!', value=f'Congratulations {member.display_name}!', inline=False)
    if gewon == False:
       embed.add_field(name=f'{member2.display_name} Won!', value=f'Congratulations {member2.display_name}!', inline=False)

    await ctx.send(file=file, embed=embed)


@bot.command()
async def flow(ctx):
	await channel.send(file=discord.File('Flow.png'))

@bot.command()
async def failed(ctx, *, member: discord.Member=None):
	if not member: # if member is no mentioned
		member = ctx.message.author # set member as the author
	await ctx.send(f"{member.display_name} has failed in life")



@bot.command()
async def wanted(ctx, user:discord.Member = None):
    if user == None:
        user = ctx.author
    wanted = Image.open("download.jpeg")
    asset = member.avatar_url_as(size=128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp = pfp.resize((177,177))
    wanted.paste(pfp, (120,212))
    asset2 = member2.avatar_url_as(size=128)
    data2 = BytesIO(await asset.read())
    pfp2 = Image.open(data)
    pfp2 = pfp.resize((177,177))
    wanted.paste(pfp, (120,212))

    wanted.save("profile.jpg")

    await ctx.send(file = discord.File("profile.jpg"))


status = '!thelp for help'



@tasks.loop()
async def change_status():
	await bot.change_presence(activity=discord.Game(status))

bot.run('Nzk1NTc4NzAxNjQzMjUxNzIz.X_LaZw.22fI-fCJ8YjWQ5aHaZ04gV94NuQ')
