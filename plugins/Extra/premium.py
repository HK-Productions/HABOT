from datetime import timedelta
from asyncio import sleep 
import pytz
import datetime, time
from info import ADMINS, LOG_CHANNEL, PAYMENT_QR , OWNER_UPI_ID
from Script import script 
from utils import get_seconds, temp
from database.users_chats_db import db 
from pyrogram import Client, filters 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors.exceptions.bad_request_400 import MessageTooLong
import traceback

@Client.on_message(filters.command("bought") & filters.private)
async def bought(client, message):
    msg = await message.reply('Wait im checking...')
    replyed = message.reply_to_message
    if not replyed:
        await msg.edit("<b>Please reply with the screenshot of your payment for the premium purchase to proceed.\n\nFor example, first upload your screenshot, then reply to it using the '/bought' command</b>")
    if replyed and replyed.photo:
        await client.send_photo(
            photo=replyed.photo.file_id,
            chat_id=LOG_CHANNEL,
            caption=f'<b>User - {message.from_user.mention}\nUser id - <code>{message.from_user.id}</code>\nusername - <code>{message.from_user.username}</code>\nUser Name - <code>{message.from_user.first_name}</code></b>',
            reply_markup=InlineKeyboardMarkup(
                [
                    
                    [
                        InlineKeyboardButton(
                            "Close", callback_data="close_data"
                        )
                    ]
                    
                ]
            )
        )
        await msg.edit_text('<b>Your screenshot has been sent to Admins</b>')
