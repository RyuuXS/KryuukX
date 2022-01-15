import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from GreyCilik.events import register
from GreyCilik import telethn as tbot


PHOTO = "https://te.legra.ph/file/20546b0718eff5862030f.jpg"

@register(pattern=("/alive"))
async def awake(event):
  GREY = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm KryuukX.** \n\n"
  GREY += f"𖣘 **I'm Working Properly** \n\n"
  GREY += f"𖣘 **My Master : [RyuuShin](https://t.me/RYUUSHINNI)** \n\n"
  GREY += f"𖣘 **Library Version :** `{telever}` \n\n"
  GREY += f"𖣘 **Telethon Version :** `{tlhver}` \n\n"
  GREY += f"𖣘 **Pyrogram Version :** `{pyrover}` \n\n"
  GREY += "**Thanks For Adding Me Here ❤️**"
  BUTTON = [[Button.url("ʜᴇʟᴘ​", "https://t.me/KryuukX_bot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ​", "https://t.me/helpforRYUU")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=GREY,  buttons=BUTTON)
