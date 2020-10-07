"""Bye Plugin 
Command:
.by  """

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 2

    animation_ttl = range(0, 7)

    input_str = event.pattern_match.group(1)

    if input_str == "by":

        await event.edit(input_str)

        animation_chars = [
        
            "`Bye 🙂🙂`",
            "`Goodbye`",    
            "`See You Soon`",
            "`I Know No One Would Miss Me 😔😔`",
             "`I Know No One Would Remember Me 🤧🤧`",
             "`Until They Have A Work 🌝🌝`",
             "`But A Good Bye To You 😃😃`",
            "`Goodbye Until I Come Back`",
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 15])
