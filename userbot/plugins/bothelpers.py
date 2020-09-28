import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

n = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"

I = ("╭━╮╭━╮╱╱╭╮\n"
"╰╮╰╯╭╯╱╱┃┃\n"
"╱╰╮╭╯╭━━┫┃╭━━┳╮╭╮╭╮\n"
"╱╭╯╰╮┃╭━┫┃┃╭╮┃╰╯╰╯┃\n"
"╭╯╭╮╰┫╰━┫╰┫╰╯┣╮╭╮╭╯N\n"
"╰━╯╰━┻━━┻━┻━━╯╰╯╰╯\n"
" you mah piro Master\n") 

L = ("╭━━━┳━━━╮\n" 
"┃╭━╮┃╭━╮┃\n" 
"┃┃╱╰┫┃┃┃┣━━┳━━━╮\n"
"┃┃╱╭┫┃┃┃┃╭╮┣━━┃┃\n"
"┃╰━╯┃╰━╯┃╰╯┃┃━━┫4SH\n"
"╰━━━┻━━━┫╭━┻━━━╯\n"
"╱╱╱╱╱╱╱╱┃┃\n"
"╱╱╱╱╱╱╱╱╰╯\n"
"A guy who knows infinity\n")

A  = ("╭━━━┳╮╱╱╭╮╭╮╭╮\n"
"┃╭━━┫╰╮╭╯┣╯┃┃┃\n"
"┃╰━━╋╮┃┃╭┻╮┃┃┃\n"
"┃╭━━╯┃╰╯┃╱┃┃┃┃╱╭╮\n"
"┃╰━━╮╰╮╭╯╭╯╰┫╰━╯┃\n"
"╰━━━╯╱╰╯╱╰━━┻━━━╯\nClow3n\n"
"this man is lit_af.........\n"
"lawla ka sarkaar hai 🤪\n")

B =("LEGENDARY 😎😎\n"
"╭╮╭━╮\n"
"┃┃┃╭╯\n"
"┃╰╯╯╭━━┳╮╱╭┳━━╮\n"
"┃╭╮┃┃┃━┫┃╱┃┃━━┫\n"
"┃┃┃╰┫┃━┫╰━╯┣━━┃\n"
"╰╯╰━┻━━┻━╮╭┻━━╯\n"
"╱╱╱╱╱╱╱╭━╯┃\n"
"╱╱╱╱╱╱╱╰━━╯\n"
"our Graphic designer\n")

C=("╭━━━╮╱╱╱╱╭┳╮\n" 
"┃╭━╮┃╱╱╱╱┃┃┃\n" 
"┃╰━━┳╮╭┳━╯┃╰━╮\n" 
"╰━━╮┃┃┃┃╭╮┃╭╮┃\n"
"┃╰━╯┃╰╯┃╰╯┃┃┃┃\n"
"╰━━━┻━━┻━━┻╯╰╯\n"
"helper and adaymn cool person\n")

D= ("╭━╮╱╭╮╱╱╱╱╱╱╱╭╮\n"
"┃┃╰╮┃┃╱╱╱╱╱╱╱┃┃\n"
"┃╭╮╰╯┣━━┳━╮╭━╯┣╮╱╭╮\n"
"┃┃╰╮┃┃╭╮┃╭╮┫╭╮┃┃╱┃┃\n"
"┃┃╱┃┃┃╭╮┃┃┃┃╰╯┃╰━╯┃\n"
"╰╯╱╰━┻╯╰┻╯╰┻━━┻━╮╭╯\n"
"╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃\n"
"╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯\n"
"thanks for your help sir :)\n")

E = ("╭╮╱╱╭╮╱╱╭╮\n"
"┃╰╮╭╯┃╱╱┃┃\n"
"╰╮┃┃╭╋━━┫╰━┳━╮╭╮╭╮\n"
"╱┃╰╯┣┫━━┫╭╮┃╭╮┫┃┃┃\n"
"╱╰╮╭┫┣━━┃┃┃┃┃┃┃╰╯┃\n"
"╱╱╰╯╰┻━━┻╯╰┻╯╰┻━━╯\n"
"Thanks for helping us sir, ur awesome \n")

F = ("╭━━━╮╱╱╱╭╮╱╭━━━╮\n" "┃╭━╮┃╱╱╱┃┃╱┃╭━╮┃\n" 
"┃┃╱╰╋╮╱╭┫╰━╋╯╭╯┣━╮\n" "┃┃╱╭┫┃╱┃┃╭╮┣╮╰╮┃╭╯\n"
"┃╰━╯┃╰━╯┃╰╯┃╰━╯┃┃\n"
"╰━━━┻━╮╭┻━━┻━━━┻╯M4f1A\n"
"╱╱╱╱╭━╯┃\n"
"╱╱╱╱╰━━╯\n"
"daymn why this name is here xD\n"
"forget it not much imp\n")

G = ("╭━━╮\n"
"╰┫┣╯\n"
"╱┃┃╭━━┳━╮\n"
"╱┃┃┃╭╮┃╭╮╮\n"
"╭┫┣┫╰╯┃┃┃┃\n"
"╰━━┻━━┻╯╰╯\n"
"Thanks for ur suggestion \n"
"U also helped us alot \n")

@borg.on(admin_cmd(pattern=r"ion"))
async def bluedevilion(ion):
        await ion.edit(G) 

@borg.on(admin_cmd(pattern=r"keys"))
async def bluedevilkeys(keys): 
        await keys.edit(B) 

@borg.on(admin_cmd(pattern=r"sudh"))
async def bluedevilsudh(sudh): 
        await sudh.edit(C)

@borg.on(admin_cmd(pattern=r"nandy"))
async def bluedevilnandy(nandy): 
        await nandy.edit(D) 

@borg.on(admin_cmd(pattern=r"vishnu"))
async def bluedevilvshnu(vishnu): 
        await vishnu.edit(E) 

@borg.on(admin_cmd(pattern=r"cyber"))
async def bluedevilcyber(cyber): 
        await cyber.edit(F) 

@borg.on(admin_cmd(pattern=r"lawla"))
async def bluedevillawla(lawla): 
        await lawla.edit(A) 

@borg.on(admin_cmd(pattern=r"cop"))
async def bluedevilcop(cop): 
        await cop.edit(L) 

@borg.on(admin_cmd(pattern=r"boss"))
async def bluedevilboss(boss): 
        await boss.edit(I)