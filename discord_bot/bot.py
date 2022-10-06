from multiprocessing.connection import wait
import discord
import os # default module
import time
import requests

from dotenv import load_dotenv
from datetime import datetime
from turtle import st
from unicodedata import name
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions
from itertools import cycle

#for linux
#load_dotenv('../.env')
#for windows
load_dotenv('./.env')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='.', intents=intents)

count = 0
statusloop = cycle(['not set'])
data = {}

MAP_URL = {
    'carentan':'https://cdn.discordapp.com/attachments/645036946976145409/733387685502386296/Carentan_TacMap01.jpg',
    'foy':'https://cdn.discordapp.com/attachments/645036946976145409/869216440199290940/hll_Map_Foy_StrongPoints.png',
    'hill400':'https://cdn.discordapp.com/attachments/537027868904128512/705371518552768574/Hill400_TacMap01.png',
    'hurtgenforest':'https://cdn.discordapp.com/attachments/645036946976145409/869330403733930075/HurtgenV2_TacMap01.png',
    'kursk':'https://cdn.discordapp.com/attachments/645036946976145409/865713430882287626/Kursk_TacMap03.png',
    'omahabeach':'https://cdn.discordapp.com/attachments/645036946976145409/1008504025446092820/Omaha_TacMap02_StrongPoints.png',
    'purpleheartlane':'https://cdn.discordapp.com/attachments/645036946976145409/738895043993272320/PHL_TacMap01.jpg',
    'remagen':'https://cdn.discordapp.com/attachments/645036946976145409/954506491279335424/hll_Map_Remagen_StrongPoints.png',
    'stalingrad':'https://cdn.discordapp.com/attachments/645036946976145409/858312040714993664/Stalingrad_TacMap03.png',
    'stmariedumont':'https://cdn.discordapp.com/attachments/645036946976145409/852915706310688808/SMDMV2_TacMap01_SP.png',
    'stmereeglise':'https://cdn.discordapp.com/attachments/645036946976145409/784042616043864134/TacMap_SME_SP.png',
    'utahbeach':'https://cdn.discordapp.com/attachments/645036946976145409/707529224310751272/UtahUpdate6_TacMap01.png'
}

MAP_NAME_TO_URL = {
    'foy_warfare':'foy',
    'foy_offensive_ger':'foy',
    'foy_offensive_us':'foy',
    'stmariedumont_warfare':'stmariedumont',
    'stmariedumont_off_us':'stmariedumont',
    'stmariedumont_off_ger':'stmariedumont',
    'hurtgenforest_warfare_V2':'hurtgenforest',
    'hurtgenforest_offensive_ger':'hurtgenforest',
    'hurtgenforest_offensive_US':'hurtgenforest',
    'utahbeach_warfare':'utahbeach',
    'utahbeach_offensive_us':'utahbeach',
    'utahbeach_offensive_ger':'utahbeach',
    'omahabeach_offensive_us':'omahabeach',
    'stmereeglise_warfare':'stmereeglise',
    'stmereeglise_offensive_ger':'stmereeglise',
    'stmereeglise_offensive_us':'stmereeglise',
    'purpleheartlane_warfare':'purpleheartlane',
    'purpleheartlane_offensive_us':'purpleheartlane',
    'purpleheartlane_offensive_ger':'purpleheartlane',
    'hill400_warfare':'hill400',
    'hill400_offensive_US':'hill400',
    'hill400_offensive_ger':'hill400',
    'carentan_warfare':'carentan',
    'carentan_offensive_us':'carentan',
    'carentan_offensive_ger':'carentan',
    'kursk_warfare':'kursk',
    'kursk_offensive_rus':'kursk',
    'kursk_offensive_ger':'kursk',
    'stalingrad_warfare':'stalingrad',
    'stalingrad_offensive_rus':'stalingrad',
    'stalingrad_offensive_ger':'stalingrad',
    'remagen_warfare':'remagen',
    'remagen_offensive_ger':'remagen',
    'remagen_offensive_us':'remagen',
    'foy_warfare_night':'foy',
    'hurtgenforest_warfare_V2_night':'hurtgenforest',
    'kursk_warfare_night':'kursk',
    'purpleheartlane_warfare_night':'purpleheartlane',
    'remagen_warfare_night':'remagen',
    'omahabeach_warfare':'omahabeach',
    'omahabeach_offensive_ger':'omahabeach',
}

LONG_HUMAN_MAP_NAMES = {
    'foy_warfare': 'Foy',
    'foy_offensive_ger': 'Foy Offensive (GER)',
    'foy_offensive_us': 'Foy Offensive (US)',
    'stmariedumont_warfare': 'St Marie du Mont',
    'stmariedumont_off_us': 'St Marie Du Mont Offensive (US)',
    'stmariedumont_off_ger': 'St Marie Du Mont Offensive (GER)',
    'hurtgenforest_warfare_V2': 'Hurtgen Forest',
    'hurtgenforest_offensive_ger': 'Hurtgen Forest Offensive (GER)',
    'hurtgenforest_offensive_US': 'Hurtgen Forest Offensive (US)',
    'utahbeach_warfare': 'Utah beach',
    'utahbeach_offensive_us': 'Utah Beach Offensive (US)',
    'utahbeach_offensive_ger': 'Utah Beach Offensive (GER)',
    'omahabeach_offensive_us': 'Omaha Beach Offensive (US)',
    'stmereeglise_warfare': 'St Mere Eglise',
    'stmereeglise_offensive_ger': 'St Mere Eglise Offensive (GER)',
    'stmereeglise_offensive_us': 'St Mere Eglise Offensive (US)',
    'purpleheartlane_warfare': 'Purple Heart Lane',
    'purpleheartlane_offensive_us': 'Purple Heart Lane Offensive (US)',
    'purpleheartlane_offensive_ger': 'Purple Heart Lane Offensive (GER)',
    'hill400_warfare': 'Hill 400',
    'hill400_offensive_US': 'Hill 400 Offensive (US)',
    'hill400_offensive_ger': 'Hill 400 Offensive (GER)',
    'carentan_warfare': 'Carentan',
    'carentan_offensive_us': 'Carentan Offensive (US)',
    'carentan_offensive_ger': 'Carentan Offensive (GER)',
    'kursk_warfare': 'Kursk',
    'kursk_offensive_rus': 'Kursk Offensive (RUS)',
    'kursk_offensive_ger': 'Kursk Offensive (GER)',
    'stalingrad_warfare': 'Stalingrad',
    'stalingrad_offensive_rus': 'Stalingrad Offensive (RUS)',
    'stalingrad_offensive_ger': 'Stalingrad Offensive (GER)',
    'remagen_warfare': 'Remagen',
    'remagen_offensive_ger': 'Remagen Offensive (GER)',
    'remagen_offensive_us': 'Remagen Offensive (US)',
    'foy_warfare_night': 'Foy (Night)',
    'hurtgenforest_warfare_V2_night': 'Hurtgen Forest (Night)',
    'kursk_warfare_night': 'Kursk (Night)',
    'purpleheartlane_warfare_night': 'Purpleheartlane (Night)',
    'remagen_warfare_night': 'Remagen (Night)',
    'omahabeach_warfare': 'Omaha Beach',
    'omahabeach_offensive_ger': ' Omaha Beach Offensive (GER)',
}

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game("Welcome to the Jungle"))
    print('bot ready.')

@bot.command()
async def start(ctx):
    await startBot(ctx)

@bot.command()
async def stop(ctx):
    await stopBot(ctx)

@bot.command()
async def restart(ctx):
    await stopBot(ctx)
    time.sleep(10.0)
    await startBot(ctx)
    

async def startBot(ctx):
    if not rconApiCall.is_running():
        rconApiCall.start()
    if not change_status.is_running():
        change_status.start()
    if not autostatus.is_running():
        autostatus.start(ctx)

async def stopBot(ctx):
    if rconApiCall.is_running():
        rconApiCall.stop()
    if change_status.is_running():
        change_status.stop()
    if autostatus.is_running(): 
        autostatus.stop()
    await deleteAll(ctx, False)
    await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game("Welcome to the Jungle"))



@bot.command()
async def clean(ctx):
    await deleteAll(ctx, True)
    await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game("Welcome to the Jungle"))

async def deleteAll(ctx, flag):
    guild = ctx.guild
    category = None
    for categoryChannel in guild.categories:
        if categoryChannel.name == '📊Hell Let Loose Server Status':
            category = discord.utils.get(guild.categories,id=categoryChannel.id)
            break

    channels = category.channels # Get all channels of the category

    for channel in channels: # We search for all channels in a loop
        try:
            await channel.delete() # Delete all channels
        except AttributeError: # If the category does not exist/channels are gone
            pass
    if(flag):
        await category.delete()


@tasks.loop(seconds=5)
async def change_status():
    global statusloop
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(next(statusloop)))

@tasks.loop(minutes=1)
async def autostatus(ctx):
    guild = ctx.guild
    category = None
    for categoryChannel in guild.categories:
        if categoryChannel.name == '📊Hell Let Loose Server Status':
            category = discord.utils.get(guild.categories,id=categoryChannel.id)
            break

    if category == None:   
        category = await guild.create_category('📊Hell Let Loose Server Status') 

    statusChannel = None
    for channel in category.channels:
        if channel.name == "server-1":
            statusChannel = discord.utils.get(category.channels,id=channel.id)
            break 

    if statusChannel == None:
        statusChannel = await guild.create_text_channel("server-1  ",category = category)
    
    await statusChannel.purge(limit=100)

    status = discord.Embed(
        #title = data['serverName'],
        # description='desc',
        colour=discord.Colour.green()
    )
    
    status.set_author(name=data['serverName'])
    status.add_field(name='En jeu', value=data['playerCount'] ,inline= False)
    status.add_field(name='Carte commencée depuis', value=data['gameDuration'] ,inline= False)
    status.add_field(name='Carte actuelle', value=LONG_HUMAN_MAP_NAMES[data['currentMap']] ,inline= False)
    status.add_field(name='Prochaine carte', value=LONG_HUMAN_MAP_NAMES[data['nextMap']] ,inline= False)
    status.set_footer(text='Map tactique')
    status.set_image(url=MAP_URL[MAP_NAME_TO_URL[data['currentMap']]])
    status.set_thumbnail(url='https://jungle-hll.fr/wp-content/uploads/2022/06/Logo-v1.jpg')

    await bot.get_channel(statusChannel.id).send(embed=status)



@tasks.loop(minutes=1)
async def rconApiCall():       
    global statusloop
    global data

    public_info = requests.get('http://' + os.environ.get("HLL_RCON_HOST_1") + '/api/public_info').json()

    data = {
        'serverName' : public_info['result']['name'],
        'starttime' : datetime.utcfromtimestamp(public_info['result']['current_map']['start']).strftime('%Y-%m-%d %H:%M:%S'),
        'gameDuration' : convert(time.time() - public_info['result']['current_map']['start'] ),
        'currentMap' : public_info['result']['map'],
        'nextMap' : public_info['result']['next_map'],
        'playerCount' : public_info['result']['nb_players'],
    }

    statusloop = cycle(['Game started :' + data['gameDuration'] ,  'Current Map: ' + LONG_HUMAN_MAP_NAMES[data['currentMap']] , 'Players: ' + data['playerCount'], 'Next Map: ' + LONG_HUMAN_MAP_NAMES[data['nextMap']]])
      
def convert(seconds): 
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    if hour != 0:
        return "%dh%02d" % (hour, minutes)
    else:
        return "%2d min" % (minutes)


bot.run(os.environ.get("BOT_TOKEN"))
