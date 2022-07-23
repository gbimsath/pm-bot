import os 
from pyrogram import Client, filters

bot = Client

@bot.on_message(filters.command("stickerid"))
async def sticker_id(client, message):
    reply = message.reply_to_message
    if not reply:
        return await message.reply("Reply to a sticker.")
    if not reply.sticker:
        return await message.reply("Reply to a sticker.")
    await message.reply_text(f"`{reply.sticker.file_id}`")
