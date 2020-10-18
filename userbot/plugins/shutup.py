#ported from X-TRA-TELEGRAM by @Unbornkiller

import random, re
import asyncio
from telethon import events
from userbot.events import register
from asyncio import sleep
import time
from userbot import CMD_HELP


@register(pattern=".shut")

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 103)

    #input_str = event.pattern_match.group(1)

    #if input_str == "shut":

    await event.edit("Shut up ")

    animation_chars = [

            "Shut",

            "Ur mouth",

            "Or else",

            "I will",

            "Kick",

            "Ur",

            "Ass",

            "And will",

            "Ban from",

            "Group",
        
            "Shut ur mouth or else i will kick ur ass and will ban from group"

        ]

    for i in animation_ttl:
        
        await asyncio.sleep(animation_interval)
        
        await event.edit(animation_chars[i % 103])

CMD_HELP.update({
  "shut":
   "`.shut`\
\nUsage: Plugin for shutting someones mouth."
})            
