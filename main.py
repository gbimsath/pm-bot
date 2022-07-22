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

#=======================================Song-Download========================================
import requests
import yt_dlp as youtube_dl
from youtube_search import YoutubeSearch

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))

@bot.on_message(filters.command('song') & ~filters.forwarded)
def song(client, message):

    user_id = message.from_user.id 
    user_name = message.from_user.first_name 
    rpk = "["+user_name+"](tg://user?id="+str(user_id)+")"

    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    print(query)
    m = message.reply("🔎 Searching...")
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        #print(results)
        title = results[0]["title"][:40]       
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f'thumb{title}.jpg'
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, 'wb').write(thumb.content)
        
        performer = f"〢ImSithijaBot〣"  
        duration = results[0]["duration"]
        url_suffix = results[0]["url_suffix"]
        views = results[0]["views"]

    except Exception as e:
        m.edit(
            "❌ Cannot find song use another keywords"
        )
        print(str(e))
        return
    m.edit("📥 Downloading...")
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = (f"""
🏷 **Title:** [{title}]({link})
⏳ **Duration:** `{duration}`
👀 **Views:** `{views}` 
👤**Requested By**: {message.from_user.mention()}
📤 **Uploaded By: [❦Iᴛ'ꜱ Mᴇ Sɪᴛʜɪᴊᴀ❦](https://t.me/ItsMeSithija)**
        """)
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
        s = message.reply_audio(audio_file, caption=rep, performer=performer, thumb=thumb_name, title=title, duration=dur)
        m.delete()
    except Exception as e:
        m.edit('❌ Error occurred.')
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)
#=======================================Song-Download========================================




print(f"""
╭━━╮╱╱╱╭━━━┳╮
╰┫┣┫╱╱╱┃╭━╮┃┃
╱┃┃┣╮╭╮┃┃╱┃┃┃╭┳╮╭┳━━╮
╱┃┣┫╰╯┃┃╰━╯┃┃┣┫╰╯┃┃━┫
╭┫┣┫┃┃┃┃╭━╮┃╰┫┣╮╭┫┃━┫
╰━━┻┻┻╯╰╯╱╰┻━┻╯╰╯╰━━╯""")

bot.run()
