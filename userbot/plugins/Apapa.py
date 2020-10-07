"""
import random, re
from uniborg.util import admin_cmd
import asyncio
from telethon import events

@borg.on(admin_cmd(pattern="(.mafia*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("Sunn be lawde")
        await asyncio.sleep(0.7)
        await event.edit("Baap Baap hota hai")
        await asyncio.sleep(1)
        await event.edit("Baap ke samne Bakchodi nhi")
        await asyncio.sleep(0.8)
        await event.edit("Aur tera Baap Kaun h janta h na")
        await asyncio.sleep(0.9)
        await event.edit("Nhi janta to jaan le")
        await asyncio.sleep(1)
        await event.edit("Mai hu tera baap")
        await asyncio.sleep(0.8)
        await event.edit("Naam M4f1aClow3n")
        await asyncio.sleep(0.7)
        await event.edit("** M4f1aClow3n PAPA**")
        await asyncio.sleep(1)
        await event.edit("`Abb Nikal yaha se madarchod`")

@borg.on(events.NewMessage(pattern=r"\.amafia", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("`Ek hi hai baap tum sabka. Naam hai M4f1aClow3n`")
    await asyncio.sleep(999)
