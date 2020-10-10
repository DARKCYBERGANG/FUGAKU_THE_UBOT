"""Emoji

Available Commands:

.k"""

from telethon import events

import asyncio

from userbot.utils import admin_cmd

@borg.on(admin_cmd("k"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0,36)
    #input_str = event.pattern_match.group(1)
   # if input_str == "ok":
    await event.edit("ok")
    animation_chars = [
 "OK",
            "BOSS",
            "OK MAN",
            "OK SIR",
            "Ok All",
            "GO AND SAY OK",
            "OK LOL",
            "YAA OK",
            "Haha Ok",
            "OK",
            "Boss",
            "Yeahhhhhh",
            "O",
            "K",
           "keem 💗",
           "okay🌝🌚🌝",
        ]

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])
