import os
import asyncio
import datetime
import discord
from discord.ext import commands
from dotenv import load_dotenv
from . import calendar
from . import logging

logging.init()
bot = commands.Bot(command_prefix='?')

def main():
    load_dotenv()
    
    global events_channel
    bot.loop.create_task(check_schedule())
    bot.run(os.getenv("DISCORD_TOKEN"))

'''
@bot.check
async def is_admin(ctx):
    # Check role for MLH or Lead Mentor
    pass
'''

async def check_schedule():
    await bot.wait_until_ready()
    global events_channel
    events_channel = bot.get_channel(int(os.getenv("DISCORD_EVENTS_ID")))

    while True:
        session = calendar.get_next_session()
        announcement_time_first = (session.start - datetime.timedelta(minutes=30))
        announcement_time_last = (session.start - datetime.timedelta(minutes=10))
        if check_times(announcement_time_first):
            await send_long_announcement(session)
        elif check_times(announcement_time_last):
            await send_short_announcement(session)
        await asyncio.sleep(60)

async def send_long_announcement(session):
    global events_channel
    embed = discord.Embed(title=session.title,
                          description=session.description)
    await events_channel.send(embed=embed)

async def send_short_announcement(session):
    global events_channel
    await events_channel.send(f'Just 10 minutes until we have {session.title}! :tada:\n {session.url}\n@Fellow')

def check_times(announcement_time):
    current_time = datetime.datetime.now()
    current_year = current_time.strftime("%Y")
    current_month = current_time.strftime("%m")
    current_day = current_time.strftime("%d")
    current_hour = current_time.strftime("%H")
    current_minute = current_time.strftime("%M")

    announcement_year = announcement_time.strftime("%Y")
    announcement_month = announcement_time.strftime("%m")
    announcement_day = announcement_time.strftime("%d")
    announcement_hour = announcement_time.strftime("%H")
    announcement_minute = announcement_time.strftime("%M")

    if current_year == announcement_year and current_month == announcement_month and current_day == announcement_day:
        if current_hour == announcement_hour and current_minute == announcement_minute:
            return True
        else:
            return False
    else:
        return False

@bot.command(description="Displays next event")
async def next_session(ctx):
    session = calendar.get_next_session()
    await ctx.send(str(session))
