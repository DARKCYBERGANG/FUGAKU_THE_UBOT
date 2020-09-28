"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
#IMG CREDITS: @LegendaryKeys
import asyncio
from telethon import events
from uniborg.util import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/10bf70ca1eec87ab3025b.png"
pm_caption = "`FUGAKU IS ON:` **FIRE 🔥**\n\n"
pm_caption += "**SYSTEM STATUS**\n"
pm_caption += "`TELETHON VERSION:` **6.0.9**\n`Python:` **3.7.4**\n"
pm_caption += "`DATABASE STATUS:` **Functional**\n"
pm_caption += "**Current Branch** : `master`\n"
pm_caption += "**KALI amd64** : `2020.03`\n"
pm_caption += f"**My Master** : {DEFAULTUSER} \n"
pm_caption += "**Fugaku** : Always for my Master \n"
pm_caption += "**Heroku Database** : `AWS - Working Properly`\n"
pm_caption += "**Log chat** : Connected \n"
pm_caption += "**Sudo** : Fully accessible \n"
pm_caption += "**SpamProtect** : True \n\n"
pm_caption += "**License** : [GNU Licence](github.com/DARKCYBERGANG/FUGAKU_THE_UBOT/blob/master/LICENSE)\n"
pm_caption += "Copyright : By [DARKCYBER@Github](GitHub.com/DARKCYBERGANG)\n"
pm_caption += "Stay updated with us : join @Fugaku_Userbot_Official"

@borg.on(admin_cmd(pattern=r"alive"))
async def friday(alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete()

    
@borg.on(admin_cmd(pattern=r"Alive", allow_sudo=True))
async def friday(alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)

    
