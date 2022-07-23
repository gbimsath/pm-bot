from pyrogram import Client. filters
from pyrogram.types import *
from config import *

bot = Client

#=========================start_cmd===============================#
@bot.on_message(filters.command("start"))
async def start_cmd(client, message):
    await bot.send_sticker(message.from_user.id, S_STICKER)
    await bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    await message.reply_text(f"Hello {message.from_user.mention}", reply_to_message_id=message.id)


# help _cmd
@bot.on_message(filters.command("help"))
async def help_cmd(client, message):
    await message.delete()
    await bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    await message.reply_text("This is help menu of bot")


# about_cmd
@bot.on_message(filters.command("about"))
async def about_cmd(client, message):
    await message.delete()
    await bot.send_chat_action(message.chat.id, enums.ChatAction.CHOOSE_STICKER)
    await bot.send_sticker(message.from_user.id, A_STICKER)
    await message.reply_photo(
        photo="https://telegra.ph/file/5b7032c04e994f5319e07.jpg",
        caption=f"HI {message.from_user.mention}",
        reply_markup=START_BTN

    )
