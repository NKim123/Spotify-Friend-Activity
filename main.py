from friendApi import getWebAccessToken, getFriendActivity
from dotenv import load_dotenv
from discord.ext import commands
import discord
import os
import datetime


#https://discord.com/api/oauth2/authorize?client_id=999172844703457310&permissions=536964096&scope=bot

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='spotify')
async def giveActivity(ctx):
    print("something")
    token = os.getenv('SPOTIFY_TOKEN2')
    accessToken = getWebAccessToken(token)
    friendActivity = getFriendActivity(accessToken)
    
    #creating the embed
    embed = discord.Embed(title="Recent Activity")

    #adding the embed fields
    for (i, friend) in enumerate(reversed(friendActivity["friends"])):
        embed.add_field(name=friend['user']['name'], value=(f'{i+1}. {friend["track"]["name"]} by {friend["track"]["artist"]["name"]} at {(datetime.datetime.fromtimestamp(int(friend["timestamp"])/1000)).strftime("%Y-%m-%d %H:%M:%S")}'), inline=False)
    
    await ctx.send(embed=embed)

def main():
    bot.run(TOKEN)

if __name__ == "__main__":
    main()