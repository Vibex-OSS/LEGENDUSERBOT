"""Emoji

Available Commands:

.deploy"""

from telethon import events

import asyncio

from uniborg.util import admin_cmd

from userbot import ALIVE_NAME


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "LEGENDBOT-User"

@borg.on(admin_cmd(pattern=r"deploy"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 10

    animation_ttl = range(0, 12)

   # input_str = event.pattern_match.group(1)



    await event.edit("Deploying...")

    animation_chars = [
        
            "**Heroku Connecting To Latest Github Build (LEGEND-OSS/RaganarokBot)**",
            "**Build started by user** **{DEFAULTUSER}**",
            "**Deploy** `475a9df0` **by user** **{MY BOSS}**",
            "**Booting up Heroku Server...**",
            "**State changed from up to starting**",    
            "**Stopping all processes with SIGTERM**",
            "**Process exited with** `status 321`",
            "**Starting process with command** `python3 -m stdborg`",
            "**State changed from starting to up**",
            "__INFO:LEGENDBOT:Logged in as 99524630__",
            "__INFO:LEGENDBOT:Successfully loaded all plugins__",
            "**Build Succeeded**"

 ]

    for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 12])
