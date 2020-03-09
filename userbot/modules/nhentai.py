# created by SANA :*
# @keselekpermen69
# remove this = gay


import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot import bot, CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^.nhentai(?: |$)(.*)")
async def hentai(event):
    if event.fwd_from:
       return
    input_str = event.pattern_match.group(1)
    if not input_str:
       await event.edit("I need a valid link.")
       return
    chat = "@nHentaiBot"
    await event.edit("`Processing`")
    
    async with bot.conversation(chat) as conv:
       try:     
            response = conv.wait_event(events.NewMessage(incoming=True,from_users=424466890))
            await bot.forward_messages(chat, input_str)
            response = await response 
       except YouBlockedUserError: 
            await event.reply("```Please unblock @nHentaiBot and try again```")
            return
       if response.text.startswith("Sorry"):
            await event.edit("I think this is not a valid link.")
       else: 
            await event.delete()   
            await bot.forward_messages(event.chat_id, response.message)

CMD_HELP.update({
        "nhentai": 
        ".nhentai <link> \
          \nUsage: make the nhentai link to telegra.ph\n"
    })
