import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

n = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"


G = ("🌺✨✨🌺✨🌺🌺🌺✨\n"
"🌺✨✨🌺✨✨🌺✨✨\n"
"🌺🌺🌺🌺✨✨🌺✨✨\n"
"🌺✨✨🌺✨✨🌺✨✨\n"
"🌺✨✨🌺✨🌺🌺🌺✨\n")

I = ("☁☁🌞      ☁           ☁\n"
"☁  ✈         ☁    🚁    ☁    ☁        ☁          ☁     ☁   ☁\n"

"🏬🏨🏫🏢🏤🏥🏦🏪🏫\n"
 "             🌲/     l🚍\🌳👭\n"
"           🌳/  🚘 l  🏃 \🌴 👬\n" 
" 👬  🌴/            l  🚔       \🌲\n"
"      🌲/   🚖     l                  🌳\n"
"        /🚶           |   🚍         \ 🌴🚴🚴\n"
"🌴/                    |                     \🌲\n")

J = ("💐💐😉😊💐💐\n"
"☕ Cheer Up  🍵\n"
"🍂 ✨ )) ✨  🍂\n"
"🍂┃ (( * ┣┓ 🍂\n"
"🍂┃*💗 ┣┛ 🍂 \n"
"🍂┗━━┛  🍂🎂 For YOU  🍰\n"
"💐💐😌😚💐💐\n")

K = ("💚~🍀🍀🍀🍀🍀\n"
"🍀╔╗╔╗╔╗╦╗✨🍀\n"
"🍀║╦║║║║║║👍🍀\n"
"🍀╚╝╚╝╚╝╩╝。 🍀\n"
"🍀・・ⓁⓊⒸⓀ🍀\n"
"🍀🍀🍀 to you💚\n")

N = ("🌹🌹🌹🌹🌹🌹🌹🌹\n"
"🌹😷😢😓😷😢💨🌹\n"
"🌹💝💉🍵💊💐💝🌹\n"
"🌹 GetBetter Soon! 🌹\n"
"🌹🌹🌹🌹🌹🌹🌹🌹\n")

Q = ("✨.•*¨*.¸.•*¨*.¸¸.•*¨*• ƸӜƷ\n"
"🌸🌺🌸🌺🌸🌺🌸🌺\n"
" Sprinkled with love❤\n"
"🌷🌻🌷🌻🌷🌻🌷🌻\n"
" ¨*.¸.•*¨*. ¸.•*¨*.¸¸.•*¨`*•.✨\n"
"🌹🍀🌹🍀🌹🍀🌹🍀\n")

R = ("╔┓┏╦━╦┓╔┓╔━━╗\n"
"║┗┛║┗╣┃║┃║X X║\n"
"║┏┓║┏╣┗╣┗╣╰╯║\n"
"╚┛┗╩━╩━╩━╩━━╝\n")

S = ("───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───\n"
"───█▒▒░░░░░░░░░▒▒█───\n"
"────█░░█░░░░░█░░█────\n"
"─▄▄──█░░░▀█▀░░░█──▄▄─\n"
"█░░█─▀▄░░░░░░░▄▀─█░░█\n"
"█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n"
"█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█\n"
"█░░║║║╠─║─║─║║║║║╠─░░█\n"
"█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█\n"
"█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")

T = ("⣿⣿⣿⣿⣿⣍⠀⠉⠻⠟⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠓⠀⠀⢒⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⣿\n"
"⣿⡿⠋⠋⠀⠀⠀⠀⠀⠀⠈⠙⠻⢿⢿⣿⣿⡿⣿⣿⡟⠋⠀⢀⣩\n"
"⣿⣿⡄⠀⠀⠀⠀⠀⠁⡀⠀⠀⠀⠀⠈⠉⠛⢷⣭⠉⠁⠀⠀⣿⣿\n"
"⣇⣀. INDIA🇮🇳INDIA🇮🇳⠆⠠..⠘⢷⣿⣿⣛⠐⣶⣿⣿\n"
"⣿⣄⠀⣰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢀⣠⣿⣿⣿⣾⣿⣿⣿\n"
"⣿⣿⣿⣿⠀⠀⠀⠀⡠⠀⠀⠀⠀⠀⢀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠄⠀⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⣠⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⠀⠀⠂⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣇⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⡆⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣿⣦⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
".   🇮🇳PROUD TO BE AN INDIAN🇮🇳\n")







@borg.on(admin_cmd(pattern=r"hola"))
async def bluedevihmf(hola): 
       await hola.edit(G)

@borg.on(admin_cmd(pattern=r"city"))
async def bluedevihmf(city): 
        await city.edit(I)

@borg.on(admin_cmd(pattern=r"cheer"))
async def bluedevihmf(cheer): 
        await cheer.edit(J)
@borg.on(admin_cmd(pattern=r"luck"))
async def bluedevihmf(luck): 
        await luck.edit(K)

@borg.on(admin_cmd(pattern=r"better"))
async def bluedevihmf(better): 
        await better.edit(N)

@borg.on(admin_cmd(pattern=r"sprinkle"))
async def bluedevihmf(sprinkle): 
        await sprinkle.edit(Q)

@borg.on(admin_cmd(pattern=r"henlo"))
async def bluedevihmf(henlo): 
        await henlo.edit(R)

@borg.on(admin_cmd(pattern=r"welcome"))
async def bluedevihmf(welcome): 
        await welcome.edit(S)

@borg.on(admin_cmd(pattern=r"india"))
async def bluedevihmf(india): 
        await india.edit(T)


