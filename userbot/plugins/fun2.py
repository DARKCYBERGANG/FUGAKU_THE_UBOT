import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd


n = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"

#@command(outgoing=True,pattern="^.ded$")
@borg.on(admin_cmd(pattern=r"ded"))
async def bluedevilded(ded):
         await ded.edit(n + " == |\n　　　　　|" "\n　　　　　| \n"
"　　　　　| \n"
"　　　　　| \n"
"　　　　　| \n"
"　　　　　| \n"
"　　　　　| \n"
"　　　　　| \n"
"　／￣￣＼| \n"
"＜ ´･ 　　 |＼ \n"
"　|　３　 | 丶＼ \n"
"＜ 、･　　|　　＼ \n"
"　＼＿＿／∪ _ ∪) \n"
"　　　　　 Ｕ Ｕ\n")

M = ("▄███████▄\n"
"█▄█████▄█\n"
"█▼▼▼▼▼█\n"
"██________█▌\n"
"█▲▲▲▲▲█\n"
"█████████\n"
"_████\n")
P = ("┈┈┏━╮╭━┓┈╭━━━━╮\n"
"┈┈┃┏┗┛┓┃╭┫ⓞⓘⓝⓚ┃\n"
"┈┈╰┓▋▋┏╯╯╰━━━━╯\n"
"┈╭━┻╮╲┗━━━━╮╭╮┈\n"
"┈┃▎▎┃╲╲╲╲╲╲┣━╯┈\n"
"┈╰━┳┻▅╯╲╲╲╲┃┈┈┈\n"
"┈┈┈╰━┳┓┏┳┓┏╯┈┈┈\n"
"┈┈┈┈┈┗┻┛┗┻┛┈┈┈┈\n")

D = ("╥━━━━━━━━╭━━╮━━┳\n"
"╢╭╮╭━━━━━┫┃▋▋━▅┣\n"
"╢┃╰┫┈┈┈┈┈┃┃┈┈╰┫┣\n"
"╢╰━┫┈┈┈┈┈╰╯╰┳━╯┣\n"
"╢┊┊┃┏┳┳━━┓┏┳┫┊┊┣\n"
"╨━━┗┛┗┛━━┗┛┗┛━━┻\n")

H = ("▬▬▬.◙.▬▬▬ \n"
"═▂▄▄▓▄▄▂ \n"
"◢◤ █▀▀████▄▄▄▄◢◤ \n"
"█▄ █ █▄ ███▀▀▀▀▀▀▀╬ \n"
"◥█████◤ \n""══╩══╩══ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ Hello, my friend :D \n"
"╬═╬☻/ \n"
"╬═╬/▌ \n"
"╬═╬/ \\n")

L = ("╱┏┓╱╱╱╭━━━╮┏┓╱╱╱╱ \n"
"╱┃┃╱╱╱┃╭━╮┃┃┃╱╱╱╱\n"
"╱┃┗━━┓┃╰━╯┃┃┗━━┓╱\n"
"╱┗━━━┛╰━━━╯┗━━━┛╱\n")

O = ("╭╭━━━╮╮┈┈┈┈┈┈┈┈┈┈\n"
"┈┃╭━━╯┈┈┈┈▕╲▂▂╱▏┈\n"
"┈┃┃╱▔▔▔▔▔▔▔▏╱▋▋╮┈\n"
"┈┃╰▏┃╱╭╮┃╱╱▏╱╱▆┃┈\n"
"┈╰━▏┗━╰╯┗━╱╱╱╰┻┫┈\n"
"┈┈┈▏┏┳━━━━▏┏┳━━╯┈\n"
"┈┈┈▏┃┃┈┈┈┈▏┃┃┈┈┈┈\n")

F = ("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\n"
"████▌▄▌▄▐▐▌█████\n"
"████▌▄▌▄▐▐▌▀████\n"
"▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀\n")

A = ("┈┈┈╱▔▔▔▔╲┈╭━━━━━\n"
"┈┈▕▂▂▂▂▂▂▏┃HEY!┊😀`\n"
"┈┈▕▔▇▔▔┳▔▏╰┳╮HEY!┊\n"
"┈┈▕╭━╰╯━╮▏━╯╰━━━\n"
"╱▔▔▏▅▅▅▅▕▔▔╲┈┈┈┈\n"
"▏┈┈╲▂▂▂▂╱┈┈┈▏┈┈┈\n")

B = ("┈┈┈╭━━━━━╮┈┈┈┈┈\n"
"┈┈┈┃┊┊┊┊┊┃┈┈┈┈┈\n"
"┈┈┈┃┊┊╭━╮┻╮┈┈┈┈\n"
"┈┈┈╱╲┊┃▋┃▋┃┈┈┈┈\n"
"┈┈╭┻┊┊╰━┻━╮┈┈┈┈\n"
"┈┈╰┳┊╭━━━┳╯┈┈┈┈\n"
"┈┈┈┃┊┃╰━━┫┈NIGGA U GEY\n"
"┈┈┈┈┈┈┏━┓┈┈┈┈┈┈\n")

C = ("╲╲╭━━━━╮\n"
"╭╮┃▆┈┈▆┃╭╮\n" 
"┃╰┫▽▽▽┣╯┃\n"
"╰━┫△△△┣━╯\n"
"╲╲┃┈┈┈┈┃\n"  
"╲╲┃┈┏┓┈┃\n")

E = ("┈╭╮╭╮\n"
"┈┃┃┃┃\n"
"╭┻┗┻┗╮\n"
"┃┈▋┈▋┃\n"
"┃┈╭▋━╮━╮\n"
"┃┈┈╭╰╯╰╯╮\n"
"┫┈┈  NoU\n"
"┃┈╰╰━━━━╯\n"
"┗━━┻━┛\n")


@borg.on(admin_cmd(pattern=r"monster"))
async def bluedevilmonster(monster): 
        await monster.edit(M)

@borg.on(admin_cmd(pattern=r"pig"))
async def bluedevipig(pig): 
        await pig.edit(P)

@borg.on(admin_cmd(pattern=r"dog"))
async def bluedevidog(dog): 
        await dog.edit(D)

@borg.on(admin_cmd(pattern=r"hmf"))
async def bluedevihmf(hmf): 
        await hmf.edit(H)

@borg.on(admin_cmd(pattern=r"lool"))
async def bluedevihmf(lool): 
        await lool.edit(L)

@borg.on(admin_cmd(pattern=r"loool"))
async def bluedevihmf(loool):  
        await loool.edit(O)

@borg.on(admin_cmd(pattern=r"fail"))
async def bluedevihmf(fail): 
        await fail.edit(F)

@borg.on(admin_cmd(pattern=r"hoi"))
async def bluedevihmf(hoi): 
        await hoi.edit(A)

@borg.on(admin_cmd(pattern=r"gay"))
async def bluedevihmf(gay): 
        await gay.edit(B)

@borg.on(admin_cmd(pattern=r"botnike"))
async def bluedevihmf(botnike): 
        await botnike.edit(C)

@borg.on(admin_cmd(pattern=r"tommy"))
async def bluedevihmf(tommy): 
        await tommy.edit(E)
