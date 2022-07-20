import os
from pyrogram import*
from pyrogram.types import*

START_BTN = InlineKeyboardMarkup([[
        InlineKeyboardButton("Tᴇʟᴇɢʀᴀᴍ🚀", url="https://t.me/gbimsath")
    ],
    [ 
        InlineKeyboardButton("Iɴsᴛɢʀᴀᴍ👁‍🗨", url="https://instagram.com/gavesh_bimsath")
    ],
    [ 
        InlineKeyboardButton("Tᴡɪᴛᴛᴇʀ🐦", url="https://twitter.com/gbimsath") 
    ],
    [ 
        InlineKeyboardButton("Gɪᴛʜᴜʙ🐱", url="https://github.com/gbimsath")
    ],
    [ 
        InlineKeyboardButton("Oғғɪᴄɪᴀʟ Wᴇʙsɪᴛᴇ🌐", url="https://gbimsath.ml/")
]])


S_STICKER = "CAACAgUAAxkBAAIafmLU5kfTTn3R_3A1Idvhl_C4RrTyAAINBgACOrN4Vew-nzcII0_JHgQ"

A_STICKER = "CAACAgUAAxkBAAIagWLU66B7EeCVWadNycgjQ8pgNErlAALIBQACYL1pVSe3PY_Lys3SHgQ"

HELP_MSG  = f" _{message.from_user.mention}_ , **This is Help Menu of @gbimsath_bot** \n Commands \n `/start` - see the start message \n `help` - see this message \n `/about` see the about message "