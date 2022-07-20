import time
from pyrogram import *
from config import *
from pyrogram.types import *
from pyrogram import Client, filters

API_ID = "8657438"
API_HASH = "ea8263e0393b6c06d4cf83ca6c5014ad"
BOT_TOKEN = "5472928911:AAFd9SW8PlCb45KRDCsUp9KjfCAnAipLXkM"

bot = Client(
    name="Pm bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


# start_cmd
@bot.on_message(filters.command("start"))
async def start_cmd(client, message):
    await message.delete()
    await bot.send_chat_action(message.chat.id, enums.ChatAction.CHOOSE_STICKER)
    time.sleep(1)
    await bot.send_sticker(message.from_user.id, S_STICKER)
    await bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    time.sleep(1)
    await message.reply_text(f"Hello {message.from_user.mention}")


# help _cmd
@bot.on_message(filters.command("help"))
async def help_cmd(client, message):
    await message.delete()
    await bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    time.sleep(1)
    await message.reply_text("This is help menu of bot")


# about_cmd
@bot.on_message(filters.command("about"))
async def about_cmd(client, message):
    await message.delete()
    await bot.send_chat_action(message.chat.id, enums.ChatAction.CHOOSE_STICKER)
    time.sleep(1)
    await bot.send_sticker(message.from_user.id, A_STICKER)
    await message.reply_photo(
        photo="https://telegra.ph/file/5b7032c04e994f5319e07.jpg",
        caption=f"HI {message.from_user.mention}",
        reply_markup=START_BTN

    )


# hello_filter
@bot.on_message(filters.private)
def command1(client, message):
    msg = message.text
    if msg.lower() == "hello":
        message.reply_sticker(sticker="CAACAgIAAxkBAAEVcyZiuoTbdeM4MmwcauArA6_woivwpQACPgcAAkb7rASvXDpewRmI9ikE",
                              reply_to_message_id=message.id)
    elif "hi" in message.text or "mk" in message.text:
        message.reply_text("හොඳයි", reply_to_message_id=message.id)


@bot.on_message(filters.command("stickerid") & filters.sticker)
async def stickerid(client, message):
    await message.reply(
            f"**Sticker ID is**  \n `{message.reply_to_message.sticker.file_id}` \n \n ** Unique ID is ** \n\n`{message.reply_to_message.sticker.file_unique_id}`",
            quote=True)
    


print(f"""
╭━━╮╱╱╱╭━━━┳╮
╰┫┣┫╱╱╱┃╭━╮┃┃
╱┃┃┣╮╭╮┃┃╱┃┃┃╭┳╮╭┳━━╮
╱┃┣┫╰╯┃┃╰━╯┃┃┣┫╰╯┃┃━┫
╭┫┣┫┃┃┃┃╭━╮┃╰┫┣╮╭┫┃━┫
╰━━┻┻┻╯╰╯╱╰┻━┻╯╰╯╰━━╯""")

bot.run()
